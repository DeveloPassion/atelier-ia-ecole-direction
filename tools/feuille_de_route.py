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
    (-30, where(1, "Avant de commencer: les prérequis"), "<b>Prérequis</b> sur chaque PC (10 min), avec une liste imprimée",
     "Application Claude, Chrome et l'extension, le même compte du collège. Le dossier « Fichiers de démo » sur le Bureau, hors OneDrive",
     q(["Bonjour, dis-moi en une phrase ce que tu peux faire.", "Résume cette page en trois points."]),
     "À voir sur chaque PC: le nom du collège en bas à gauche, le choix « Cowork », le modèle Opus 5.5, l'extension reliée à l'application, un dossier hors OneDrive qui s'ouvre comme dossier de travail. Si Cowork est coupé: démos de la partie 6 sur mon écran, et vraie tâche dans le chat"),
    (0, where(1, "1. Le même Claude, deux réponses"), "<b>Exercice: le même Claude, deux réponses</b> (leur PC)",
     "Aucun fichier. Le texte « avec contexte » est sur la slide suivante (à copier tel quel)",
     q(["Écris un mot aux parents pour la sortie scolaire."]) + "<br/>puis le texte de la slide « Avec contexte »",
     "Mettre les deux réponses côte à côte: laquelle est utilisable telle quelle?"),
    (8, where(2, "L'application Claude"), "<b>Tour de l'application</b> (leur PC, 4 min), puis les modèles et l'effort",
     "Aucun fichier",
     "Dicter une demande au micro. Taper « / »",
     "Si la dictée ne marche pas: touche Windows + H. Montrer aussi l'extension Claude in Chrome dans Chrome"),
    (16, where(3, "3. Première démo"), "<b>Démo 1: la circulaire</b> (leur PC, 10 min, Opus 5.5)",
     FD + "Circulaire 9847 - Organisation de l'année scolaire 2026-2027.pdf<br/>Puis la vraie: circulaire 9757 (lien dans les notes de la slide)",
     q(quoted(3, "La circulaire: la demande à copier")[:1]) + "<br/>(slide suivante: une demande par rôle, bouton « Copier »)<br/>Effort haut: pas en direct, montrer le plan B. Toujours faire la 2e circulaire",
     "Vérifier en direct un seul tableau, celui du primaire. 9847: CEB dans CEBSI le 05/03/2027 (piège: le 19/02 est reporté); FUI aux parents de 6e du 11/01 au 22/01/2027; liste PSE le 30/11/2026; EENC le 20/11/2026. 9757: « presque rien n'est pour vous », 24/08/2026 déjà passé.<br/>Plan B: " + PB + "Démo 1 - Actions primaire circulaire 9847.pdf. Corrigés complets: notes de la slide, plan de cours"),
    (26, where(4, "Quand Claude demande la permission"), "<b>Partie 4: les six slides essentielles</b>. Option: la complaisance en direct (1 min)",
     "Aucun fichier",
     "Proposer une idée discutable, puis: « Qu'est-ce qui cloche? »",
     "Finir sur la slide de la permission: elle sert dès la démo 2"),
    (35, where(5, "Ce que Claude voit"), "<b>Partie 5: les huit slides essentielles</b>",
     "Option: l'écran de l'utilisation, dans les paramètres (slide « Le coût, en bref »)", "",
     "<b>Repère: la pause commence à 0:45.</b> Les compléments de la partie 5 sont pour la relecture"),
    (45, "Pause (10 min)", "<b>Préparer la suite</b>",
     "Ouvrir « Fichiers de démo » et le dossier « Plan B ». Chrome avec l'extension, et la page de la ferme ouverte",
     "", "Comparer les deux autres tableaux de la circulaire avec ceux qui le veulent"),
    (55, where(6, "Cowork: quand Claude fait le travail"), "<b>Cowork, les permissions, le dossier de travail</b> (leur PC, 5 min)",
     "Chacun crée un dossier « Base IA » et le choisit comme dossier de travail",
     "", "Bouton « Choose folder », sous la zone de saisie, puis « Open folder... » (dessin sur la slide « Votre dossier de travail »). Réglage « Manuel »"),
    (60, where(6, "Démo 2: créer des fichiers"), "<b>Démo 2: créer des fichiers</b> (leur PC, 8 min)",
     FD + "Notes réunion équipe 2026-11-03 (brut).docx<br/>" + FD + "Sorties pédagogiques 2026-2027 (liste).docx",
     q(quoted(6, "Démo 2: les demandes à copier")) + "<br/>(slide suivante, bouton « Copier »)",
     "S'arrêter sur la première demande de permission, et la lire à voix haute. Ouvrir le Word et la liste « pas clair ». Excel: la sortie à la ferme en P2 a deux prix (12 et 9,50 euros).<br/>Plan B: Démo 2 - Compte rendu (docx), Démo 2 - Sorties (xlsx)"),
    (68, where(6, "Maintenant: votre vraie tâche"), "<b>Leur vraie tâche</b> (leur PC, 15 min)",
     "Leurs fichiers, copiés dans un dossier à part. Leurs tâches: dans leurs réponses aux trois questions (mails)",
     "Leur demande, écrite avec la recette (qui, quoi, pour qui, forme, exemple, règles et critères), et « Pose-moi d'abord tes questions ». À la fin: « Quelle demande t'aurait permis de faire ça du premier coup? »",
     "<b>Repère: commencer à 1:08 au plus tard.</b> Passer de l'un à l'autre. Tâche trop grosse: faire la première étape. Rien apporté: le mot aux parents pour sa classe, ou une vraie circulaire. Finir: « Gardez cette demande: c'est peut-être votre première skill »"),
    (83, where(6, "Un artefact, ou un fichier?"), "<b>Artefact ou fichier</b> (1 min), puis <b>la démo 3</b>, avec le plan B seulement (1 min)",
     PB + "Démo 3 - Dossier rangé (résultat)/ avec INDEX.pdf", "",
     "Ne pas refaire le rangement en direct: montrer le résultat"),
    (85, where(6, "Démo 4: le navigateur"), "<b>Démo 4: le navigateur et l'injection de prompt</b> (écran, 5 min, Chrome)",
     "Aucun fichier. La page fictive de la ferme de la Hulotte (lien sur la slide « à copier »): son formulaire n'envoie rien, et elle cache une instruction pour l'IA",
     q(quoted(6, "Démo 4: les demandes à copier")) + "<br/>(slide suivante, bouton « Copier »)",
     "Formulaire rempli, <b>pas envoyé</b>. Injection: l'a-t-il suivie ou signalée? Bouton « Afficher » en bas de la page. Si le wifi ou l'extension bloque: passer à la slide « Ce qui vient de se passer », puis au plan B.<br/>Plan B: Démo 4 - Comparaison lieux d'excursion (exemple).pdf"),
    (90, where(7, "Démo: Direction Saint-Exemple"), "<b>Partie 7: les slides essentielles</b>, le journal du jour (1 min) et <b>la démo du système</b> (5 min)",
     "Le système Saint-Exemple dans Obsidian (Journal/Quotidien/2026/46/2026-11-09.md), et Claude sur ce dossier",
     q(system_q[:2]) + "<br/>Puis la même question dans un chat vide",
     "Réponses attendues: « DEMO - À demander.txt », à la racine du système. Si la démo bloque: lire les réponses attendues à voix haute. <b>Repère: la partie 8 commence à 1:42</b>"),
    (102, where(8, "Lundi: trois gestes, trois interdits"), "<b>Partie 8: les cinq slides essentielles</b>, et le projet de règles d'usage",
     "Documents à remettre/Projet de règles d'usage de l'IA.pdf", "",
     "Si le collège a déjà une politique, partir de la sienne. Finir sur « Lundi: trois gestes, trois interdits »"),
    (107, where(9, "Un seul pas pour demain"), "<b>Partie 9: à retenir, un seul pas, les documents</b> (5 min)",
     "L'aide-mémoire imprimé (un par personne), la fiche de contexte (PDF), les prérequis",
     "", "Écrire sur chaque aide-mémoire le nom de l'admin du collège et celui du DPO"),
    (112, where(9, "Vos questions"), "<b>Leurs questions</b> (6 min)",
     "La feuille des questions notées pendant la séance", "",
     "Réponses prêtes dans le bonus 17 (fiabilité, remplacement, coût, données, téléphone, ChatGPT ou Copilot, triche, énergie, responsabilité). Coûts: bonus 18"),
    (118, "Fin", "<b>Marge (2 min)</b>", "", "",
     "Leurs réponses aux trois questions (avant l'atelier) servent à la phase 2"),
    ("option", where(5, "Plusieurs conversations en parallèle"), "Deux gestes en direct, s'il y a de l'avance",
     "Conversations en parallèle. Slide « Des conversations courtes »: la longue conversation compactée, préparée avant",
     "Lancer une tâche longue, puis un mail court dans une nouvelle conversation",
     "Le détail des coûts, du cache et de la compaction: bonus 18"),
    ("option", where(6, "Démo 6: une photo"), "Démo 6: la photo (3 min), ou démo 5: la présentation (2 min)",
     "La photo prise sur place, déjà sur le PC. Ou " + FD + "Texte réunion de parents de rentrée.docx",
     q(quoted(6, "Démo 6: la demande à copier") + quoted(6, "Démo 5: les demandes à copier")[:1]) + "<br/>(slides suivantes, bouton « Copier »)",
     "Plan B: Démo 5 - Réunion de parents de rentrée (pptx)"),
    ("option", where(7, "Démo: en vrac ou organisé"), "Démo: en vrac ou organisé (5 min)",
     "Les deux dossiers dézippés: le système « en vrac » et le système « notes seules »",
     q([vrac_q]) + "<br/>Au vrac, puis à l'organisé, puis une 2e fois au vrac",
     "Organisé: Sortie P4 (active), Plan de pilotage (actif), Classes de neige P5 (en pause, bloqué: 690 euros &gt; plafond de 485), photos terminées. Vrac: statuts devinés, la liste change.<br/>Corrigé: question 6 de « DEMO - À demander.txt »"),
    ("séance 2", where(7, "Démo: créer une skill"), "Démo: créer une skill ensemble (5 min)",
     "Claude ouvert sur une copie du système « notes seules ». La note « Écrire aux parents (Processus) », dossier Actions/Processus",
     q([skill_q]) + "<br/>Puis: « Écris le mot aux parents pour la sortie P4 du 26 novembre. »",
     "Résultat: un dossier « ecrire-aux-parents » avec SKILL.md (name, description, puis « lis la note du processus »). Puis changer « 150 mots » en « 80 mots » dans le processus, et relancer: le mot change, pas la skill"),
]

header = [Paragraph(h, HEAD) for h in ["Heure", "Où dans les slides", "Quoi", "Fichiers et lieu", "Demande à taper", "À vérifier, corrigé, plan B"]]
data = [header]
for off, w, what, files, prompt, check in rows:
    data.append([Paragraph(off if isinstance(off, str) else minutes(START, off), CELLB), Paragraph(w, CELL), Paragraph(what, CELL),
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
    Paragraph("Les slides à passer en séance", H2),
    b("Dans chaque partie, les notes marquent les slides «\u00a0ESSENTIEL\u00a0» ou «\u00a0À PASSER\u00a0». En séance, je montre les slides essentielles. À passer: "
      + " ".join(f"<b>partie {n}</b>, slides {', '.join(skippable(n))}." for n in range(1, 10) if skippable(n))),
    Paragraph("Trois repères à tenir", H2),
    b("<b>0:45</b>: la pause commence. <b>1:08</b>: leur vraie tâche a commencé. <b>1:42</b>: la partie 8 commence. En retard à un repère: passer tout de suite à la slide essentielle suivante."),
    Paragraph("La veille et le matin", H2),
    b("Dézipper les deux systèmes de démo, ouvrir « Direction Saint-Exemple » dans Obsidian, ouvrir une fois les slides sans internet."),
    b("Imprimer l'aide-mémoire (un par personne). Préparer la feuille « parking ». Option: une longue conversation compactée."),
    b("Arriver vers 9h30. Écran ou projecteur, wifi, chargeur."),
    b("<b>Avant le jour J</b>: lire les réponses au test des prérequis (Cowork, Opus 5.5, extension, dossier hors OneDrive). Tester la page de la ferme le matin même. Tester la dictée, et Windows + H."),
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
