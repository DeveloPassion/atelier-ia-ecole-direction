#!/usr/bin/env python3
import html, json, os, re, shutil, sys

"""Build the course site: src/parts/*.md -> one NN-...html per part (src/parts.json) and index.html (reveal.js, offline).

Usage, from the repository root:  python3 tools/build.py
lib/ (reveal.js 5.2.1, Pele 1.13.0, Noto Sans) and theme.css (DeveloPassion theme) are committed and not rebuilt.
"""
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
deck_dir = os.path.join(ROOT, "src", "parts")
outdir = ROOT
meta = json.load(open(os.path.join(ROOT, "src", "parts.json"), encoding="utf-8"))
MAIN = sum(1 for m in meta if not m.get("bonus"))
BONUS = len(meta) - MAIN

FONTS = """
@font-face { font-family: "Noto Sans"; src: url("lib/fonts/NotoSans-Regular.ttf") format("truetype"); font-weight: 400; font-style: normal; }
@font-face { font-family: "Noto Sans"; src: url("lib/fonts/NotoSans-Bold.ttf") format("truetype"); font-weight: 700 900; font-style: normal; }
@font-face { font-family: "Noto Sans"; src: url("lib/fonts/NotoSans-Italic.ttf") format("truetype"); font-weight: 400; font-style: italic; }
"""

BRAND = FONTS + """
:root { --dp-magenta: #e5007d; --dp-pink: #ff1493; --dp-purple: #a855f7; --dp-slate: #37404c;
  --dp-surface: #3f4957; --dp-surface-2: #475363; --dp-well: #2b323c; --dp-green: #4ade80; --dp-yellow: #fbbf24; }
html, body, .reveal-viewport { background: var(--dp-slate); }
.reveal .slides { background: transparent !important; }
.reveal { font-size: 30px; }
.reveal .slides section { text-align: left; }
.reveal h2 { font-size: 1.45em; font-weight: 800; }
/* Titles: the magenta bar goes UNDER the title (brand underline bar), not above it */
.reveal h2::before { display: none !important; }
.reveal h2 { margin: 0 0 0.75em 0; }
.reveal .slides section:not(.hero) h2::after { content: ""; display: block; width: 56px; height: 4px; border-radius: 999px;
  background: var(--dp-magenta); margin-top: 0.32em; }
/* Same top position on every slide (center: false) */
.reveal .slides > section, .reveal .slides > section > section { padding-top: 54px !important; box-sizing: border-box; }
.reveal .slides section.hero { padding-top: 170px !important; }
/* Rhythm between paragraphs and lists */
.reveal p { margin: 0 0 0.6em 0; }
.reveal ul, .reveal ol { margin: 0 0 0 1.15em; padding: 0; }
.reveal li { margin: 0 0 0.38em 0; padding-left: 0.3em; }
.reveal li > ul, .reveal li > ol { margin-top: 0.35em; margin-bottom: 0.1em; font-size: 0.92em; }
.reveal p + ul, .reveal p + ol { margin-top: 0.55em; }
.reveal ul + p, .reveal ol + p, .reveal ul + blockquote, .reveal ol + blockquote, .reveal table + p,
.reveal ul + .diagram, .reveal ol + .diagram, .reveal p + .diagram, .reveal ul + div, .reveal ol + div { margin-top: 1.0em; }
.reveal ul + p.system, .reveal ol + p.system, .reveal p + p.system { margin-top: 1.1em; }
.reveal blockquote { margin: 0.8em 0; }
.reveal table { margin: 0.4em 0 0.6em 0; }
.reveal p, .reveal li { color: rgba(255,255,255,0.92); }
.reveal li::marker, .reveal ol li::marker { color: var(--dp-pink); font-weight: 700; }
.reveal table { font-size: 0.72em; }
.reveal table td { color: rgba(255,255,255,0.9); }
.reveal table tr:hover td { background: rgba(229,0,125,0.08); }
.reveal blockquote { font-style: normal; width: 88%; }
/* Prompts are blockquotes: a copy button in the top right corner */
.reveal blockquote { position: relative; padding-right: 3.6em; box-sizing: border-box; }
.reveal blockquote .copy-btn { position: absolute; top: 0.45em; right: 0.45em; font: 600 0.5em 'Noto Sans', sans-serif;
  color: #fff; background: var(--dp-magenta); border: 0; border-radius: 999px; padding: 0.35em 0.9em; cursor: pointer; }
.reveal blockquote .copy-btn:hover { background: var(--dp-pink); }
.reveal blockquote .copy-btn.done { background: #16a34a; }
@media print { .reveal blockquote .copy-btn { display: none; } }
.reveal strong { font-weight: 700 !important; color: #ff4fa8 !important; }
.reveal p.caption { font-size: 0.72em; color: rgba(255,255,255,0.75); margin-top: 0.3em; } .reveal p.caption .tag { border-radius: 8px; background: rgba(255,255,255,0.1); padding: 0.15em 0.6em; margin-right: 0.4em; font-weight: 600; }
.reveal .chart { margin: 0.2em 0 0.4em 0; } .reveal .chart svg { width: 100%; max-height: 400px; font-family: 'Noto Sans', sans-serif; }
.gradient { background: linear-gradient(90deg, #ff1493, #e5007d, #a855f7); -webkit-background-clip: text; background-clip: text;
  color: transparent !important; filter: drop-shadow(0 0 18px rgba(255,20,147,0.35)); }
.reveal .eyebrow { display: inline-block; border-radius: 999px; background: rgba(229,0,125,0.12); border: 1px solid rgba(229,0,125,0.35);
  color: #ffd1e8; font-size: 0.5em; font-weight: 700; padding: 0.25em 0.9em; margin: 0 0 0.8em 0; letter-spacing: 0.02em; }
/* Section and cover slides: hero wash + particles */
.reveal .slides section.hero, .reveal .slides section:first-child { text-align: left !important; }
.reveal .slides section:first-child h1::after { display: none; }
.loop-step { font-size: 0.85em; }
.reveal .slides section.hero h2 { font-size: 2.3em; line-height: 1.1; }
.reveal .slides section.hero h2::before { display: none; }
.reveal .slides section.hero h2::after { content: ""; display: block; width: 64px; height: 5px; border-radius: 999px; background: var(--dp-magenta); margin-top: 0.35em; }
.reveal .slides section.hero p { color: rgba(255,255,255,0.64); font-size: 1.05em; }
.reveal .backgrounds .slide-background.hero, .slide-background.hero {
  background: radial-gradient(1200px 600px at 85% 10%, rgba(168,85,247,0.18), transparent 60%),
              radial-gradient(900px 500px at 10% 90%, rgba(229,0,125,0.16), transparent 60%), var(--dp-slate) !important; }
.particles { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
.particles i { position: absolute; width: 6px; height: 6px; border-radius: 50%; background: var(--dp-pink); opacity: 0.35; animation: float 9s ease-in-out infinite; }
@keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-18px); } }
@media (prefers-reduced-motion: reduce) { .particles i, .loop-step, .loop::after { animation: none !important; } }
/* System callout */
.reveal p.system { border-left: 4px solid var(--dp-magenta); background: rgba(229,0,125,0.10); border-radius: 0 10px 10px 0;
  padding: 0.5em 0.9em; font-size: 0.8em; margin-top: 0.8em; }
.reveal p.system b { color: var(--dp-pink); }
/* Nav pill */
.nav-home { position: fixed; top: 14px; left: 16px; z-index: 30; font: 600 14px "Noto Sans", sans-serif; color: #fff; text-decoration: none;
  background: rgba(255,255,255,0.1); border-radius: 8px; padding: 6px 12px; }
.nav-home:hover { background: var(--dp-magenta); }
/* Diagrams (Pele) */
.reveal .diagram { text-align: center; margin: 0.4em auto; }
.reveal .diagram svg { max-width: 92%; max-height: 330px; height: auto; }
.pele { --pele-bg: transparent; --pele-fg: #ffffff; --pele-surface: #3f4957; --pele-surface-alt: #475363; --pele-border: rgba(255,255,255,0.28);
  --pele-line: #ff1493; --pele-muted: rgba(255,255,255,0.6); --pele-font: "Noto Sans", sans-serif; }
/* Agentic loop animation */
.loop { display: grid; grid-template-columns: 1fr 1fr; gap: 28px 90px; width: 80%; margin: 30px auto; position: relative; }
.loop-step { border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 18px; text-align: center; background: var(--dp-surface);
  color: #fff; font-weight: 700; animation: lit 8s infinite; }
.loop .s1 { grid-column: 1; grid-row: 1; animation-delay: 0s; }
.loop .s2 { grid-column: 2; grid-row: 1; animation-delay: 2s; }
.loop .s3 { grid-column: 2; grid-row: 2; animation-delay: 4s; }
.loop .s4 { grid-column: 1; grid-row: 2; animation-delay: 6s; }
.loop::after { content: "\\21BB"; position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); font-size: 2.6em; color: var(--dp-pink);
  animation: spin 8s linear infinite; }
@keyframes lit { 0%, 24% { background: var(--dp-magenta); box-shadow: 0 0 24px rgba(229,0,125,0.45); transform: scale(1.05); }
  25%, 100% { background: var(--dp-surface); box-shadow: none; transform: scale(1); } }
@keyframes spin { from { transform: translate(-50%,-50%) rotate(0deg); } to { transform: translate(-50%,-50%) rotate(360deg); } }
/* Lethal trifecta */
.trifecta { display: flex; justify-content: center; margin-top: 10px; }
.trifecta span { width: 210px; height: 210px; border-radius: 50%; display: flex; align-items: center; justify-content: center; text-align: center;
  font-size: 0.66em; font-weight: 700; color: #fff; margin: 0 -28px; padding: 30px; box-sizing: border-box; mix-blend-mode: screen; }
.trifecta span:nth-child(1) { background: rgba(229,0,125,0.55); }
.trifecta span:nth-child(2) { background: rgba(168,85,247,0.55); }
.trifecta span:nth-child(3) { background: rgba(255,20,147,0.40); }
"""


def transform(md, part_no, part_name, dur):
    md = md.replace("\t", "    ")
    md = re.sub(r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", r"![](\1)", md)
    md = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", md)
    md = re.sub(r"\[\[([^\]]+)\]\]", r"\1", md)
    md = re.sub(r"^Pour un système qui vous connaît: (.*)$",
                lambda m: '<p class="system"><b>Pour un système qui vous connaît:</b> ' + html.escape(m.group(1), quote=False) + "</p>", md, flags=re.M)
    slides = md.split("\n---\n")
    out = []
    for i, sl in enumerate(slides):
        s = sl.strip("\n")
        m = re.match(r"## (\d+)\. (.*)", s)
        if (part_no == 1 and i == 0) or m:
            head, _, rest = s.partition("\n")
            title = head[3:]
            words = title.split(" ")
            # gradient on the key word: the last word of the title
            title_html = " ".join(words[:-1]) + (" " if len(words) > 1 else "") + f'<span class="gradient">{words[-1]}</span>'
            eyebrow = ("Bonus" if "bonus" in dur else f"Partie {part_no} sur {MAIN} · {dur}") if part_no > 1 or i > 0 else "Atelier IA · Direction d'école"
            s = f'<!-- .slide: class="hero" data-background-gradient="radial-gradient(1100px 560px at 85% 10%, rgba(168,85,247,0.20), transparent 60%), radial-gradient(900px 500px at 8% 92%, rgba(229,0,125,0.18), transparent 60%), #37404c" -->\n<p class="eyebrow">{eyebrow}</p>\n\n<h2>{title_html}</h2>\n\n{rest}'
        out.append(s)
    return "\n---\n".join(out)


def page(title, body_md, part_no):
    assert "</textarea>" not in body_md and "</script>" not in body_md
    particles = "".join(f'<i style="left:{x}%;top:{y}%;animation-delay:{d}s"></i>' for x, y, d in
                        [(8, 18, 0), (22, 72, 1.5), (40, 12, 3), (63, 80, 0.8), (78, 30, 2.2), (90, 62, 4), (52, 46, 5)])
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="lib/reveal/dist/reset.css">
  <link rel="stylesheet" href="lib/reveal/dist/reveal.css">
  <link rel="stylesheet" href="theme.css">
  <style>{BRAND}</style>
</head>
<body>
  <a class="nav-home" href="index.html">&#8592; Sommaire</a>
  <div class="reveal">
    <div class="slides">
      <section data-markdown data-separator="^---$" data-separator-vertical="^----$" data-separator-notes="^Note:">
        <textarea data-template>
{body_md}
        </textarea>
      </section>
    </div>
  </div>
  <script src="lib/reveal/dist/reveal.js"></script>
  <script src="lib/reveal/plugin/markdown/markdown.js"></script>
  <script src="lib/reveal/plugin/notes/notes.js"></script>
  <script src="lib/pele.iife.js"></script>
  <script>
    const render = (window.Pele && window.Pele.render) || null;
    function drawDiagrams() {{
      if (!render) return;
      document.querySelectorAll('.reveal pre code.mermaid, .reveal pre code.language-mermaid').forEach((code) => {{
        const pre = code.closest('pre');
        try {{ const {{ svg }} = render(code.textContent); const d = document.createElement('div'); d.className = 'diagram pele'; d.innerHTML = svg; pre.replaceWith(d); }}
        catch (e) {{ console.warn('Diagram failed', e); }}
      }});
    }}
    async function copyText(text) {{
      try {{ await navigator.clipboard.writeText(text); return; }} catch (e) {{}}
      const t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select();
      document.execCommand('copy'); t.remove();
    }}
    function addCopyButtons() {{
      document.querySelectorAll('.reveal .slides blockquote').forEach((bq) => {{
        if (bq.closest('aside')) return;
        const text = bq.innerText.trim();
        const b = document.createElement('button');
        b.type = 'button'; b.className = 'copy-btn'; b.textContent = 'Copier'; b.title = 'Copier la demande';
        b.addEventListener('click', async (ev) => {{
          ev.stopPropagation(); await copyText(text);
          b.textContent = 'Copié'; b.classList.add('done');
          setTimeout(() => {{ b.textContent = 'Copier'; b.classList.remove('done'); }}, 2000);
        }});
        bq.appendChild(b);
      }});
    }}
    Reveal.initialize({{ hash: true, slideNumber: 'c/t', transition: 'fade', width: 1280, height: 720, margin: 0.06, center: false,
      plugins: [ RevealMarkdown, RevealNotes ] }}).then(() => {{ drawDiagrams(); document.querySelectorAll('.reveal a[href^="http"]').forEach((a) => {{ a.target = '_blank'; a.rel = 'noopener'; }}); addCopyButtons(); Reveal.layout(); }});
  </script>
</body>
</html>
"""


cards = []
total = 0
for m in meta:
    src = open(os.path.join(deck_dir, m["file"]), encoding="utf-8").read()
    if src.startswith("---\n"):
        src = src[src.index("\n---\n", 4) + 5:]
    body = src[src.index("\n---\n") + 5:]  # drop the H1 line
    out_name = m["html"]
    open(os.path.join(outdir, out_name), "w", encoding="utf-8").write(
        page(f"{m['n']}. {m['name']} - L'IA au service de l'école", transform(body, m["n"], m["name"], m["dur"]), m["n"]))
    m["slides"] = body.count("\n---\n") + 1
    total += m["slides"]
    cards.append(f'<a class="card" href="{out_name}" target="_blank" rel="noopener"><span class="num">{m["n"]}</span>'
                 f'<span class="t">{html.escape(m["name"])}</span><span class="meta">{html.escape(m["dur"])} · {m["slides"]} slides</span></a>')

index = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>L'IA au service de l'école - Sommaire</title>
<style>{FONTS}
:root {{ --m: #e5007d; --p: #ff1493; --v: #a855f7; --s: #37404c; --c: #3f4957; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; min-height: 100vh; font-family: "Noto Sans", "Segoe UI", system-ui, sans-serif; color: #fff;
  background: radial-gradient(1200px 600px at 85% 0%, rgba(168,85,247,0.16), transparent 60%), radial-gradient(900px 500px at 0% 100%, rgba(229,0,125,0.14), transparent 60%), var(--s); }}
main {{ max-width: 1100px; margin: 0 auto; padding: 56px 28px; }}
.eyebrow {{ display: inline-block; border-radius: 999px; background: rgba(229,0,125,0.12); border: 1px solid rgba(229,0,125,0.35);
  color: #ffd1e8; font-size: 14px; font-weight: 700; padding: 5px 14px; }}
h1 {{ font-size: 52px; font-weight: 800; margin: 18px 0 6px; line-height: 1.1; }}
.gradient {{ background: linear-gradient(90deg, #ff1493, #e5007d, #a855f7); -webkit-background-clip: text; background-clip: text; color: transparent; filter: drop-shadow(0 0 18px rgba(255,20,147,0.35)); }}
.bar {{ width: 64px; height: 5px; border-radius: 999px; background: var(--m); margin: 14px 0 18px; }}
p.lead {{ color: rgba(255,255,255,0.64); font-size: 18px; margin: 0 0 30px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 18px; }}
.card {{ display: flex; flex-direction: column; gap: 6px; text-decoration: none; color: #fff; background: var(--c); border: 1px solid rgba(255,255,255,0.1);
  border-radius: 14px; padding: 20px 22px; transition: transform .15s, box-shadow .15s; }}
.card:hover {{ transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0,0,0,0.35); }}
.num {{ font-size: 40px; font-weight: 800; color: var(--p); line-height: 1; }}
.t {{ font-size: 20px; font-weight: 700; }}
.meta {{ color: rgba(255,255,255,0.6); font-size: 14px; }}
footer {{ margin-top: 36px; color: rgba(255,255,255,0.5); font-size: 14px; }}
.sec {{ font-size: 22px; font-weight: 800; margin: 40px 0 14px; }} .sec::after {{ content: ''; display: block; width: 48px; height: 4px; border-radius: 999px; background: #e5007d; margin-top: 8px; }}
kbd {{ background: rgba(255,255,255,0.1); border-radius: 6px; padding: 1px 7px; font-family: inherit; }}
</style></head>
<body><main>
<span class="eyebrow">Atelier IA · Direction d'école</span>
<h1>L'IA au service de <span class="gradient">l'école</span></h1>
<div class="bar"></div>
<p class="lead">Les personnes et les documents de démo sont fictifs: ce support sert à apprendre. {MAIN} parties et {BONUS} bonus, {total} slides, environ 2 heures. Chaque partie s'ouvre dans un nouvel onglet.</p>
<div class="grid">
{chr(10).join(cards)}
</div>
<h2 class="sec">Documents</h2>
<div class="grid docs">
<a class="card" href="documents/Aide-m%C3%A9moire%20-%20Claude%20au%20quotidien.pdf" target="_blank" rel="noopener"><span class="t">Aide-mémoire: Claude au quotidien</span><span class="meta">PDF, 2 pages, à imprimer</span></a>
<a class="card" href="documents/Avant%20l%27atelier%20-%20les%20pr%C3%A9requis.pdf" target="_blank" rel="noopener"><span class="t">Avant l'atelier: les prérequis</span><span class="meta">PDF, 1 page: Claude, Chrome, fichiers de démo</span></a>
<a class="card" href="documents/Feuille%20de%20route%20de%20l%27animateur.pdf" target="_blank" rel="noopener"><span class="t">Feuille de route de l'animateur</span><span class="meta">PDF, 3 pages: quelle démo, quand, avec quels fichiers</span></a>
<a class="card" href="documents/Fiche%20de%20contexte%20pour%20l%27IA.pdf" target="_blank" rel="noopener"><span class="t">Fiche de contexte pour l'IA</span><span class="meta">PDF, 2 pages: les questions, à remplir ou à imprimer</span></a>
<a class="card" href="documents/%C3%80%20propos%20de%20moi.txt" download><span class="t">À propos de moi (fichier texte)</span><span class="meta">Les mêmes questions dans un fichier texte: vos réponses, à donner à l'IA</span></a>
<a class="card" href="documents/Projet%20de%20r%C3%A8gles%20d%27usage%20de%20l%27IA.pdf" target="_blank" rel="noopener"><span class="t">Projet de règles d'usage de l'IA</span><span class="meta">PDF, 1 page, à compléter</span></a>
<a class="card" href="documents/fichiers-de-demo.zip"><span class="t">Fichiers de démo</span><span class="meta">Un zip à télécharger, tous fictifs, avec un LISEZ-MOI</span></a>
</div>
<footer>Dans une partie: <kbd>S</kbd> notes de l'orateur · <kbd>F</kbd> plein écran · <kbd>Échap</kbd> vue d'ensemble. © 2026 Sébastien Dubois · DeveloPassion. Tous droits réservés.</footer>
</main></body></html>
"""
open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(index)
print(f"parts={len(meta)} slides={total} out={outdir}")
