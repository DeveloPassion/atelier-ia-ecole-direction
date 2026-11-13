"""Build a printable PDF of all the slides: light pages, the visuals on a dark card.

Usage, from the repository root (run tools/build.py first):
    uv run --with websocket-client --with pypdf python tools/slides_pdf.py [OUTPUT_FOLDER] [--per-page N]

OUTPUT_FOLDER defaults to documents/ (published on the site). --per-page is 1, 2 (default) or 4 slides on each A4 page;
with 1, each slide is one page at the size of the screen.

How it works: it starts Chrome or Edge without a window, opens each part with reveal.js's print view (?print-pdf), and
asks the browser for a PDF through the DevTools protocol. The command line switch --print-to-pdf is not enough: it
ignores the page size of the print view. Set the CHROME environment variable if the browser is not found.
"""
import base64
import io
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request

import websocket
from pypdf import PdfReader, PdfWriter, Transformation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:]]
PER_PAGE = 2
if "--per-page" in args:
    i = args.index("--per-page")
    PER_PAGE = int(args[i + 1])
    del args[i:i + 2]
assert PER_PAGE in (1, 2, 4), "--per-page must be 1, 2 or 4"
OUT_DIR = os.path.abspath(args[0]) if args else os.path.join(ROOT, "documents")
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "Slides à imprimer.pdf")
SLIDE_W, SLIDE_H = 1280, 720  # the size of a slide in CSS pixels (tools/build.py)


def find_browser():
    cands = [os.environ.get("CHROME"),
             r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
             r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
             "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
             shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser"), shutil.which("chrome")]
    for c in cands:
        if c and os.path.exists(c):
            return c
    sys.exit("Chrome or Edge not found. Set the CHROME environment variable to the path of the browser.")


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


class Tab:
    """A very small DevTools protocol client for one tab."""

    def __init__(self, port):
        deadline = time.time() + 20
        while True:
            try:
                targets = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2))
                page = [t for t in targets if t.get("type") == "page"]
                if page:
                    break
            except OSError:
                pass
            if time.time() > deadline:
                sys.exit("The browser did not start.")
            time.sleep(0.3)
        self.ws = websocket.create_connection(page[0]["webSocketDebuggerUrl"], suppress_origin=True, timeout=120)
        self.n = 0

    def call(self, method, **params):
        self.n += 1
        self.ws.send(json.dumps({"id": self.n, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.n:
                if "error" in msg:
                    sys.exit(f"{method}: {msg['error']}")
                return msg["result"]

    def js(self, expr):
        return self.call("Runtime.evaluate", expression=expr, returnByValue=True)["result"].get("value")


def print_part(tab, html_file, first, total):
    url = "file:///" + os.path.join(ROOT, html_file).replace("\\", "/") + "?print-pdf"
    tab.call("Page.navigate", url=url)
    deadline = time.time() + 40
    # ready when reveal.js built one page per slide and the fonts are loaded
    while not tab.js("document.querySelectorAll('.reveal .pdf-page').length > 0 && document.fonts.status === 'loaded'"):
        if time.time() > deadline:
            sys.exit(f"The print view of {html_file} did not load.")
        time.sleep(0.25)
    time.sleep(0.8)  # the diagrams are drawn just after
    # one numbering for the whole deck: "23 / 186", at the bottom right of each slide
    tab.js("""document.querySelectorAll('.reveal .pdf-page').forEach((page, i) => {
      let n = page.querySelector('.slide-number');
      if (!n) { n = document.createElement('div'); n.className = 'slide-number slide-number-pdf'; page.appendChild(n); }
      n.style.position = 'absolute'; n.style.display = 'block';
      n.textContent = (%d + i) + ' / ' + %d;
    })""" % (first, total))
    pdf = tab.call("Page.printToPDF", printBackground=True, preferCSSPageSize=True, paperWidth=SLIDE_W / 96, paperHeight=SLIDE_H / 96,
                   marginTop=0, marginBottom=0, marginLeft=0, marginRight=0)
    return PdfReader(io.BytesIO(base64.b64decode(pdf["data"])))


def n_up(pages, per_page):
    """Put 2 or 4 slides on each A4 page."""
    a4w, a4h = 595.28, 841.89
    if per_page == 2:
        pw, ph, cols, rows, margin, gap = a4w, a4h, 1, 2, 34, 22
    else:
        pw, ph, cols, rows, margin, gap = a4h, a4w, 2, 2, 26, 16  # landscape
    cell_w = (pw - 2 * margin - (cols - 1) * gap) / cols
    out = PdfWriter()
    sheet = None
    for k, page in enumerate(pages):
        slot = k % per_page
        if slot == 0:
            sheet = out.add_blank_page(width=pw, height=ph)
        w, h = float(page.mediabox.width), float(page.mediabox.height)
        scale = cell_w / w
        cell_h = h * scale
        block_h = rows * cell_h + (rows - 1) * gap
        top = ph - (ph - block_h) / 2
        col, row = slot % cols, slot // cols
        x = margin + col * (cell_w + gap)
        y = top - (row + 1) * cell_h - row * gap
        sheet.merge_transformed_page(page, Transformation().scale(scale).translate(x, y))
    return out


browser = find_browser()
port = free_port()
profile = tempfile.mkdtemp(prefix="slides-pdf-")
proc = subprocess.Popen([browser, "--headless=new", f"--remote-debugging-port={port}", "--remote-allow-origins=*", f"--user-data-dir={profile}",
                         "--no-first-run", "--disable-extensions", "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    tab = Tab(port)
    tab.call("Page.enable")
    meta = json.load(open(os.path.join(ROOT, "src", "parts.json"), encoding="utf-8"))
    # the number of slides of each part, counted in the sources like tools/build.py does
    counts = []
    for m in meta:
        src = open(os.path.join(ROOT, "src", "parts", m["file"]), encoding="utf-8").read()
        counts.append(src[src.index("\n---\n") + 5:].count("\n---\n") + 1)
    pages = []
    for m, count in zip(meta, counts):
        part = print_part(tab, m["html"], len(pages) + 1, sum(counts))
        assert len(part.pages) == count, (m["html"], len(part.pages), count)
        pages += list(part.pages)
        print(f'{m["n"]:>2}. {m["name"]}: {len(part.pages)} slides')
finally:
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
    shutil.rmtree(profile, ignore_errors=True)

if PER_PAGE == 1:
    writer = PdfWriter()
    for p in pages:
        writer.add_page(p)
else:
    writer = n_up(pages, PER_PAGE)
writer.add_metadata({"/Title": "L'IA au service de l'école: les slides", "/Author": "Sébastien Dubois"})
writer.compress_identical_objects()
with open(OUT, "wb") as f:
    writer.write(f)
print(OUT, f"slides={len(pages)} pages={len(writer.pages)} size={os.path.getsize(OUT) // 1024} KB")
