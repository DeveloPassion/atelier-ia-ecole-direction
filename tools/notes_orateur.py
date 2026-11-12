"""Build the speaker notes as a PDF to print: every slide in order, with its notes.

Usage, from the repository root:
    uv run --with reportlab python tools/notes_orateur.py [OUTPUT_FOLDER]

OUTPUT_FOLDER defaults to documents/ (published on the site). This is the paper plan B for when the
presenter view is not available. The same content is on notes.html (tools/build.py), for a phone or a tablet.
It reads src/parts/*.md, so it stays in step with the slides: rebuild it after each change of the notes.
"""
import json
import os
import re
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "documents")
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "Notes de l'orateur.pdf")

FONTS = os.path.join(ROOT, "lib", "fonts")
pdfmetrics.registerFont(TTFont("NS", os.path.join(FONTS, "NotoSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("NSB", os.path.join(FONTS, "NotoSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("NSI", os.path.join(FONTS, "NotoSans-Italic.ttf")))
pdfmetrics.registerFontFamily("NS", normal="NS", bold="NSB", italic="NSI", boldItalic="NSB")

W, H = A4
M = 42
SLATE, MAGENTA, INK, GREY = HexColor("#37404c"), HexColor("#e5007d"), HexColor("#1f2329"), HexColor("#6b7480")
PART = ParagraphStyle("part", fontName="NSB", fontSize=14, leading=17, textColor=SLATE, spaceBefore=14, spaceAfter=1, keepWithNext=1)
PMETA = ParagraphStyle("pmeta", fontName="NS", fontSize=8, leading=10, textColor=GREY, spaceAfter=5, keepWithNext=1)
TITLE = ParagraphStyle("title", fontName="NSB", fontSize=10.5, leading=13, textColor=INK, spaceBefore=7, spaceAfter=2, keepWithNext=1)
NOTE = ParagraphStyle("note", fontName="NS", fontSize=9.5, leading=12.6, textColor=INK, leftIndent=20, spaceAfter=3)
STEP = ParagraphStyle("step", parent=NOTE, leftIndent=34, firstLineIndent=-14)
NONE = ParagraphStyle("none", fontName="NS", fontSize=8.5, leading=11, textColor=GREY, spaceBefore=1.5)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def markup(line):
    """The Markdown of one line of a note, as reportlab markup: links and bold."""
    t = esc(line)
    t = re.sub(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" color="#b3005f">\1</a>', t)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)


def num(k, color="#e5007d"):
    return f'<font name="NSB" color="{color}">{k}</font>&nbsp;&nbsp;'


story = []
total = with_notes = 0
for m in json.load(open(os.path.join(ROOT, "src", "parts.json"), encoding="utf-8")):
    src = open(os.path.join(ROOT, "src", "parts", m["file"]), encoding="utf-8").read()
    slides = src[src.index("\n---\n") + 5:].split("\n---\n")
    story.append(Paragraph(f'{m["n"]}. {esc(m["name"])}', PART))
    story.append(HRFlowable(width="100%", thickness=1.5, color=MAGENTA, spaceBefore=1, spaceAfter=2))
    story.append(Paragraph(f'{esc(m["dur"])} · {len(slides)} slides', PMETA))
    for k, sl in enumerate(slides, 1):
        total += 1
        vis, _, note = sl.partition("\nNote:")
        t = re.search(r"^## (.+)$", vis, re.M)
        title = esc(t.group(1).strip() if t else "(sans titre)")
        lines = [x.strip() for x in note.strip().split("\n") if x.strip()]
        if not lines:
            story.append(Paragraph(num(k, "#6b7480") + title, NONE))
            continue
        with_notes += 1
        story.append(Paragraph(num(k) + title, TITLE))
        for line in lines:
            story.append(Paragraph(markup(line), STEP if re.match(r"\d+\. ", line) else NOTE))
        story.append(Spacer(0, 2))


def decorate(c, d):
    c.saveState()
    c.setFillColor(SLATE)
    c.rect(0, H - 44, W, 44, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("NSB", 13)
    c.drawString(M, H - 21, "Notes de l'orateur")
    c.setFont("NS", 7.5)
    c.drawString(M, H - 35, "Atelier IA pour une direction d'école. Le plan B sans écran d'orateur. Le numéro est celui de la slide dans sa partie.")
    c.setFillColor(GREY)
    c.setFont("NS", 7)
    c.drawString(M, 16, "Aussi sur une page pour téléphone ou tablette: notes.html, sur le sommaire du support.")
    c.drawRightString(W - M, 16, f"Page {d.page}")
    c.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=56, bottomMargin=34,
                        title="Notes de l'orateur", author="Sébastien Dubois")
doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
print(OUT, f"slides={total} with_notes={with_notes} pages={doc.page}")
