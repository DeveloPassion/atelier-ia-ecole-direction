"""Build the presenter's run sheet: which demo, when, where in the slides, which files, what to type, what to check.

Usage, from the repository root:
    uv run --with reportlab python tools/feuille_de_route.py [OUTPUT_FOLDER] [START_TIME]

OUTPUT_FOLDER defaults to documents/ (published on the site). START_TIME defaults to 10:00.
It only uses what the slides and their speaker notes already say, so it stays in step with src/parts/:
slide numbers and demo prompts are read from the Markdown, and the script stops if a slide title it
needs is missing.
"""
import json
import os
import re
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, KeepTogether

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "documents")
os.makedirs(OUT_DIR, exist_ok=True)
START = sys.argv[2] if len(sys.argv) > 2 else "10:00"
OUT = os.path.join(OUT_DIR, "Feuille de route de l'animateur.pdf")

FONTS = os.path.join(ROOT, "lib", "fonts")
pdfmetrics.registerFont(TTFont("NS", os.path.join(FONTS, "NotoSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("NSB", os.path.join(FONTS, "NotoSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("NSI", os.path.join(FONTS, "NotoSans-Italic.ttf")))
pdfmetrics.registerFontFamily("NS", normal="NS", bold="NSB", italic="NSI", boldItalic="NSB")

SLATE, MAGENTA, INK, SOFT, GREY = HexColor("#37404c"), HexColor("#e5007d"), HexColor("#1f2329"), HexColor("#f6f1f4"), HexColor("#5b6470")
CELL = ParagraphStyle("cell", fontName="NS", fontSize=7.1, leading=8.7, textColor=INK)
CELLB = ParagraphStyle("cellb", parent=CELL, fontName="NSB")
HEAD = ParagraphStyle("head", parent=CELL, fontName="NSB", textColor=white)
H2 = ParagraphStyle("h2", fontName="NSB", fontSize=11, leading=13.5, textColor=MAGENTA, spaceBefore=6, spaceAfter=3)
BODY = ParagraphStyle("body", fontName="NS", fontSize=8, leading=10, textColor=INK, leftIndent=9, bulletIndent=0, spaceAfter=1.5)

# ---------- read the slides
meta = {m["n"]: m for m in json.load(open(os.path.join(ROOT, "src", "parts.json"), encoding="utf-8"))}


def slides(n):
    src = open(os.path.join(ROOT, "src", "parts", meta[n]["file"]), encoding="utf-8").read()
    return src[src.index("\n---\n") + 5:].split("\n---\n")


def find(n, title):
    """(slide number as shown in the deck, slide text) of the slide whose title contains `title`."""
    for i, s in enumerate(slides(n)):
        if re.search(r"^## .*" + re.escape(title), s.strip("\n"), re.M):
            return i + 1, s
    sys.exit(f"Slide not found: part {n}, title containing {title!r}. Update tools/feuille_de_route.py.")


def note(text):
    return text.split("\nNote:", 1)[1] if "\nNote:" in text else ""


def quoted(n, title):
    """The prompts a slide shows in a box (blockquote lines), ready to copy."""
    return re.findall(r"^> (.+?)\r?$", find(n, title)[1], re.M)


def skippable(n):
    """Numbers of the slides of part n whose notes start with the mark 'À PASSER'."""
    return [str(i + 1) for i, sl in enumerate(slides(n)) if note(sl).lstrip().startswith("À PASSER")]


def where(n, title):
    k, _ = find(n, title)
    return f"Partie {n}, slide {k}<br/><i>{title}</i>"


def minutes(clock, add):
    h, m = map(int, clock.split(":"))
    t = h * 60 + m + add
    return f"{t // 60}:{t % 60:02d}"


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def q(texts):
    return "<br/>".join(f"« {esc(t)} »" for t in texts)


# ---------- timeline (minutes after the start, from the "Timing visé" of part 1)
FD = "Fichiers de démo/"
PB = "Fichiers de démo/Plan B - résultats attendus/"
system_q = re.findall(r'\d\) "(.+?)"', note(find(7, "Démo: Direction Saint-Exemple")[1]))
skill_q = re.search(r"^> (.+)$", find(7, "Démo: créer une skill")[1], re.M).group(1)
vrac_q = re.search(r'La même question aux deux: "(.+?)"', find(7, "Démo: en vrac ou organisé")[1]).group(1)
rows = [
    (-30, where(1, "Avant de commencer: les prérequis"), "<b>Prérequis</b> sur chaque PC (10 min)",
     "Application Claude, Chrome et l'extension, le même compte du collège. Le dossier « Fichiers de démo » hors OneDrive",
     q(["Bonjour, dis-moi en une phrase ce que tu peux faire.", "Résume cette page en trois points."]),
     "Si un PC bloque: à deux sur un PC, ou claude.ai dans le navigateur. Feuille « parking » sur la table"),
    (0, where(1, "1. Le même Claude, deux réponses"), "<b>Exercice: le même Claude, deux réponses</b> (leur PC, 2 min par demande)",
     "Aucun fichier. Le texte « avec contexte » est sur la slide suivante (à copier tel quel)",
     q(["Écris un mot aux parents pour la sortie scolaire."]) + "<br/>puis le texte de la slide « Avec contexte »",
     "Mettre les deux réponses côte à côte: laquelle est utilisable telle quelle?"),
    (8, where(2, "L'application Claude"), "<b>Tour de l'application</b> (leur PC, 4 min)",
     "Aucun fichier. Suite: slides « Les réglages », « Les modes de travail », « Les commandes »",
     "Dicter une demande au micro. Ouvrir les paramètres: Connecteurs, Skills. Taper « / »",
     "Montrer aussi l'extension Claude in Chrome dans Chrome"),
    (18, where(3, "3. Première démo"), "<b>Démo 1: la circulaire</b> (leur PC, 10 min, Opus 5.5)",
     FD + "Circulaire 9847 - Organisation de l'année scolaire 2026-2027.pdf<br/>Puis la vraie: circulaire 9757 (lien dans les notes de la slide)",
     q(quoted(3, "La circulaire: la demande à copier")[:1]) + "<br/>(slide suivante: une demande par rôle, bouton « Copier »)<br/>Effort haut: pas en direct, montrer le plan B. Toujours faire la 2e circulaire",
     "9847: CEB dans CEBSI le 05/03/2027 (piège: le 19/02 est reporté); FUI aux parents de 6e du 11/01 au 22/01/2027; liste PSE le 30/11/2026; EENC le 20/11/2026. 9757: « presque rien n'est pour vous », 24/08/2026 déjà passé.<br/>Plan B: " + PB + "Démo 1 - Actions primaire circulaire 9847.pdf. Corrigés complets: notes de la slide, plan de cours"),
    (28, where(4, "La complaisance"), "<b>Option: la complaisance</b> (écran, 1 min)",
     "Aucun fichier",
     "Proposer une idée discutable, puis: « Qu'est-ce qui cloche? » Option « Pas seulement du texte »: « Crée un jeu de calcul mental pour des élèves de 2e primaire, avec un score. »",
     "Seulement si le temps le permet"),
    (38, where(5, "Plusieurs conversations en parallèle"), "<b>Partie 5: deux gestes en direct</b>",
     "Conversations en parallèle; slide « Le coût, en bref »: l'écran de l'utilisation, dans les paramètres. Option, slide « Des conversations courtes »: la longue conversation compactée préparée avant",
     "Lancer une tâche longue (ranger le dossier), puis un mail court dans une nouvelle conversation",
     "La conversation compactée est optionnelle. Le détail des coûts, du cache et de la compaction: bonus 18"),
    (50, "Pause (10 min)", "<b>Préparer les démos</b>",
     "Ouvrir « Fichiers de démo » et le dossier « Plan B ». Chrome avec l'extension. Le dossier « Activités de P1 à P6 (copie en désordre) »",
     "", "Prendre une page écrite à la main (sans données d'élèves) pour la démo photo"),
    (60, where(6, "Démo 2: créer des fichiers"), "<b>Démo 2: créer des fichiers</b> (leur PC, 8 min)",
     FD + "Notes réunion équipe 2026-11-03 (brut).docx<br/>" + FD + "Sorties pédagogiques 2026-2027 (liste).docx",
     q(quoted(6, "Démo 2: les demandes à copier")) + "<br/>(slide suivante, bouton « Copier »)",
     "Ouvrir le Word et la liste « pas clair ». Excel: la sortie à la ferme en P2 a deux prix (12 et 9,50 euros).<br/>Plan B: Démo 2 - Compte rendu (docx), Démo 2 - Sorties (xlsx)"),
    (68, where(6, "Démo 3: ranger un dossier"), "<b>Démo 3: ranger un dossier</b> (écran, 6 min, mode Plan)",
     "Dossier de travail: " + FD + "Activités de P1 à P6 (copie en désordre)/ (36 fichiers)",
     q(quoted(6, "Démo 3: la demande à copier")) + "<br/>(slide suivante, bouton « Copier »)",
     "Lire le plan à voix haute, dire oui. Résultat: un doublon signalé, la garderie dans Divers, la sortie de l'an passé.<br/>Plan B: Démo 3 - Dossier rangé (résultat)/ avec INDEX.pdf"),
    (74, where(6, "Démo 4: le navigateur"), "<b>Démo 4: le navigateur</b> (écran, 4 min, Chrome)",
     "Aucun fichier. La page fictive de la ferme de la Hulotte (lien sur la slide « à copier »): son formulaire n'envoie rien, et elle cache une instruction pour l'IA",
     q(quoted(6, "Démo 4: les demandes à copier")) + "<br/>(slide suivante, bouton « Copier »)",
     "Cliquer un lien pour vérifier un prix. Musée du Carnaval: animations peut-être dès la 5e seulement. Formulaire rempli, <b>pas envoyé</b>. Injection de prompt: l'a-t-il suivie ou signalée? Bouton « Afficher » en bas de la page.<br/>Plan B: Démo 4 - Comparaison lieux d'excursion (exemple).pdf"),
    (78, where(6, "Démo 6: une photo"), "<b>Démo 6: la photo</b> (écran, 3 min) <i>ou</i> <b>démo 5: la présentation</b> (2 min), s'il reste du temps",
     "La photo prise sur place. Ou " + FD + "Texte réunion de parents de rentrée.docx",
     q(quoted(6, "Démo 6: la demande à copier") + quoted(6, "Démo 5: les demandes à copier")[:1]) + "<br/>(slides suivantes, bouton « Copier »)",
     "Sinon, plan B: Démo 5 - Réunion de parents de rentrée (pptx). Puis 1 min sur « Et l'ordinateur » (slide)"),
    (83, where(7, "Le journal du jour"), "<b>Montrer le journal du jour</b> (écran, 1 min)",
     "Système Saint-Exemple dans Obsidian: Journal/Quotidien/2026/46/2026-11-09.md",
     "", "Dézippé avant la séance (version complète sur mon PC, « notes seules » sinon)"),
    (89, where(7, "Démo: en vrac ou organisé"), "<b>Démo: en vrac ou organisé</b> (écran, 5 min)",
     "Les deux dossiers dézippés: « Direction Saint-Exemple en vrac » et « Direction Saint-Exemple »",
     q([vrac_q]) + "<br/>Au vrac, puis à l'organisé, puis une 2e fois au vrac",
     "Organisé: Sortie P4 (active), Plan de pilotage (actif), Classes de neige P5 (en pause, bloqué: 690 euros &gt; plafond de 485), photos terminées. Vrac: statuts devinés, la liste change.<br/>Corrigé: question 6 de « DEMO - À demander.txt »"),
    (94, where(7, "Démo: Direction Saint-Exemple"), "<b>Démo: Direction Saint-Exemple</b> (écran, 5 min)",
     "Le système dans Obsidian, et Claude sur ce dossier",
     q(system_q[:2]) + "<br/>Les autres demandes s'il reste du temps. Puis la même question dans un chat vide",
     "Réponses attendues: « DEMO - À demander.txt », à la racine du système. Montrer le début et une ou deux trouvailles"),
    (99, where(7, "Démo: créer une skill"), "<b>Démo: créer une skill ensemble</b> (écran, 5 min)",
     "Claude ouvert sur une copie du dossier «\u00a0Direction Saint-Exemple\u00a0». La note «\u00a0Écrire aux parents (Processus)\u00a0», dossier Actions/Processus",
     q([skill_q]) + "<br/>Puis: «\u00a0Écris le mot aux parents pour la sortie P4 du 26 novembre.\u00a0»",
     "Résultat: un dossier «\u00a0ecrire-aux-parents\u00a0» avec SKILL.md (name, description, puis «\u00a0lis la note du processus\u00a0»). Puis changer «\u00a0150 mots\u00a0» en «\u00a080 mots\u00a0» dans le processus, et relancer: le mot change, pas la skill. Elle reste dans le dossier: rien à installer. Dire: avec leur système, «\u00a0Crée-moi une skill...\u00a0» ou «\u00a0skillify\u00a0» suffit"),
    (104, where(8, "Des règles d'usage"), "<b>Partie 8: le projet de règles d'usage</b>",
     "Documents à remettre/Projet de règles d'usage de l'IA.pdf", "",
     "Si le collège a déjà une politique, partir de la sienne"),
    (108, where(9, "Trois actions pour demain"), "<b>Partie 9: remettre les documents</b>",
     "L'aide-mémoire imprimé (un par personne), la fiche de contexte (PDF), les prérequis",
     "",
     "Leurs réponses aux trois questions (avant l'atelier) servent à la phase 2"),
    (110, where(9, "Maintenant: votre vraie tâche"), "<b>Leur vraie tâche</b> (leur PC, 6 min)",
     "Leurs fichiers, copiés dans un dossier à part. Leurs tâches: dans leurs réponses aux trois questions (mails)",
     "Leur demande, écrite avec la recette (qui, quoi, pour qui, forme, exemple, règles et critères), et «\u00a0Pose-moi d'abord tes questions\u00a0». À la fin: «\u00a0Quelle demande t'aurait permis de faire ça du premier coup?\u00a0»",
     "Passer de l'un à l'autre. Tâche trop grosse: faire la première étape. Rien apporté: le mot aux parents pour sa classe, ou une vraie circulaire. Finir: «\u00a0Gardez cette demande: c'est peut-être votre première skill\u00a0»"),
    (118, "Fin", "<b>Marge (2 min), feuille « parking »</b>", "", "",
     "Questions probables: réponses prêtes dans le bonus 17 (fiabilité, remplacement, coût, données, téléphone, ChatGPT ou Copilot, triche, énergie, responsabilité). Coûts: bonus 18"),
]

header = [Paragraph(h, HEAD) for h in ["Heure", "Où dans les slides", "Quoi", "Fichiers et lieu", "Demande à taper", "À vérifier, corrigé, plan B"]]
data = [header]
for off, w, what, files, prompt, check in rows:
    data.append([Paragraph(minutes(START, off), CELLB), Paragraph(w, CELL), Paragraph(what, CELL),
                 Paragraph(files, CELL), Paragraph(prompt, CELL), Paragraph(check, CELL)])

W, H = landscape(A4)
M = 22
avail = W - 2 * M
widths = [avail * f for f in (0.05, 0.12, 0.15, 0.2, 0.27, 0.21)]
table = Table(data, colWidths=widths, repeatRows=1)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), SLATE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, SOFT]),
    ("LINEBELOW", (0, 0), (-1, -1), 0.3, HexColor("#e2d6dd")),
    ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
]))


def b(t):
    return Paragraph(t, BODY, bulletText="•")


before = KeepTogether([
    Paragraph("Où trouver quoi", H2),
    b("<b>Les étapes de chaque démo</b>: les notes de l'orateur de la slide (touche <b>S</b> dans la partie). Cette feuille en reprend l'essentiel."),
    b("<b>Plan B sans écran d'orateur</b> (projecteur en mode dupliqué): la page « Notes de l'orateur » (notes.html, sur le sommaire) sur le téléphone ou la tablette, ou le PDF « Notes de l'orateur » imprimé (documents/)."),
    b("<b>Les fichiers</b>: le dossier « Fichiers de démo », copié hors OneDrive (aussi sur le site: documents/fichiers-de-demo.zip). Les résultats attendus: « Plan B - résultats attendus ». Les systèmes de démo: les zips «\u00a0notes seules\u00a0» et «\u00a0en vrac\u00a0» (le système complet avec AI Kit for Obsidian, un produit payant, n'est pas public)."),
    b("<b>Les corrigés</b>: « DEMO - À demander.txt » à la racine du système Saint-Exemple, et les sections « Corrigé » du plan de cours."),
    b("<b>Les slides</b>: le sommaire (index.html) de la copie locale, hors ligne. Toutes les slides restent: je choisis en direct ce que je passe."),
    Paragraph("Si le temps manque: les slides à passer", H2),
    b("Les notes des parties 4, 5 et 7 marquent chaque slide «\u00a0ESSENTIEL\u00a0» ou «\u00a0À PASSER\u00a0». À passer: "
      + " ".join(f"<b>partie {n}</b>, slides {', '.join(skippable(n))}." for n in (4, 5, 7))),
    Paragraph("La veille et le matin", H2),
    b("Dézipper les deux systèmes de démo, ouvrir « Direction Saint-Exemple » dans Obsidian, ouvrir une fois les slides sans internet."),
    b("Imprimer l'aide-mémoire (un par personne). Préparer la feuille « parking ». Option: une longue conversation compactée."),
    b("Arriver vers 9h30. Écran ou projecteur, wifi, chargeur."),
])

doc = SimpleDocTemplate(OUT, pagesize=landscape(A4), leftMargin=M, rightMargin=M, topMargin=48, bottomMargin=26,
                        title="Feuille de route de l'animateur", author="Sébastien Dubois")


def decorate(c, d):
    c.saveState()
    c.setFillColor(SLATE)
    c.rect(0, H - 40, W, 40, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("NSB", 13)
    c.drawString(M, H - 20, "Feuille de route de l'animateur: quelle démo, quand, avec quoi")
    c.setFont("NS", 7.5)
    c.drawString(M, H - 33, f"Début à {START}. Heures indicatives, d'après le timing de la partie 1. Pour l'animateur; les étapes complètes sont dans les notes de l'orateur.")
    c.setFillColor(GREY)
    c.setFont("NS", 7)
    c.drawRightString(W - M, 12, f"Page {d.page}")
    c.restoreState()


doc.build([table, Spacer(0, 6), before], onFirstPage=decorate, onLaterPages=decorate)
print(OUT)
