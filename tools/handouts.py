"""Build the handouts in documents/: the fillable context sheet (A4 PDF) and its starter text file, the draft AI usage rules and the prerequisites.

Usage, from the repository root:  uv run --with reportlab python tools/handouts.py [output folder]
The default output folder is documents/. The cheat sheet has its own script: tools/aide_memoire.py.
"""
import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "documents")
os.makedirs(out_dir, exist_ok=True)
W, H = A4
M = 50
NAVY = HexColor("#37404c")
ORANGE = HexColor("#e5007d")
GREY = HexColor("#555555")

# Fonts with French accents: Noto Sans from lib/fonts (in the repo), else DejaVu, else Helvetica
REG, BOLD = "Helvetica", "Helvetica-Bold"
_noto = os.path.join(ROOT, "lib", "fonts")
if os.path.exists(os.path.join(_noto, "NotoSans-Regular.ttf")):
    pdfmetrics.registerFont(TTFont("NS", os.path.join(_noto, "NotoSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("NSB", os.path.join(_noto, "NotoSans-Bold.ttf")))
    REG, BOLD = "NS", "NSB"
for cand in [] if REG == "NS" else ["/usr/share/fonts/TTF/DejaVuSans.ttf", "/usr/share/fonts/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
    if os.path.exists(cand):
        pdfmetrics.registerFont(TTFont("DV", cand))
        pdfmetrics.registerFont(TTFont("DVB", cand.replace("DejaVuSans.ttf", "DejaVuSans-Bold.ttf")))
        REG, BOLD = "DV", "DVB"
        break


def para(c, text, x, y, width, font=REG, size=10, color=GREY, leading=None):
    leading = leading or size * 1.35
    c.setFont(font, size)
    c.setFillColor(color)
    for line in simpleSplit(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def header(c, title, subtitle):
    c.setFillColor(NAVY)
    c.rect(0, H - 80, W, 80, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont(BOLD, 18)
    c.drawString(M, H - 45, title)
    c.setFont(REG, 10)
    c.drawString(M, H - 64, subtitle)


def footer(c, text, page):
    c.setFont(REG, 8)
    c.setFillColor(GREY)
    c.drawString(M, 28, text)
    c.drawRightString(W - M, 28, f"Page {page}")


# ---------- Fiche de contexte ----------
SECTIONS = [
    ("1. Qui je suis", [
        ("role", "Mon rôle et mon école: niveau, nombre de classes et d'élèves, depuis quand.", 3),
        ("perimetre", "Ce qui fait partie de mon rôle, et ce qui revient à d'autres (secrétariat, pouvoir organisateur, autre direction).", 3),
        ("ton", "Mon ton quand j'écris: tutoiement ou vouvoiement, court ou détaillé, formules que j'utilise. Si possible, collez un texte dont vous êtes content.", 4),
    ]),
    ("2. Mes objectifs et mes projets", [
        ("priorites", "Mes trois priorités pour cette année scolaire.", 3),
        ("projets", "Les projets en cours (par exemple le plan de pilotage, une sortie, un projet numérique).", 3),
        ("attente", "Ce que j'attends des autres en ce moment: une réponse, un document, une validation.", 3),
    ]),
    ("3. Mon environnement", [
        ("personnes", "Les personnes avec qui je travaille le plus, et leur rôle.", 3),
        ("outils", "Mes outils et applications (mAGEordome, GEDI-PRO, RAVEL, IT School, OneDrive, Outlook...). Ce que je dois aller vérifier moi-même, sans notification.", 4),
        ("annee", "Les grands moments de l'année scolaire pour moi, et ceux qui me surchargent.", 3),
    ]),
    ("4. Mes processus et mes règles", [
        ("repetitif", "Les tâches répétitives qui me prennent le plus de temps.", 3),
        ("processus", "Une tâche que je fais souvent, expliquée étape par étape (par exemple: organiser une sortie).", 4),
        ("jamais", "Ce que l'IA ne doit jamais faire sans me demander (envoyer, supprimer, répondre à un parent...).", 3),
        ("interdit", "Les dossiers et les données que l'IA ne doit pas voir (par exemple ELEVES).", 2),
    ]),
]


STARTER_NAME = "À propos de moi.txt"
STARTER_URL_TEXT = "developassion.github.io/atelier-ia-ecole-direction/documents/" + STARTER_NAME
STARTER_URL = "https://developassion.github.io/atelier-ia-ecole-direction/documents/" + quote(STARTER_NAME)


def starter(path):
    """Starter text file with the same questions as the context sheet.
    Plain text, not Markdown: the participants are not technical. Windows line ends and a BOM so Notepad opens it well."""
    out = ["À PROPOS DE MOI", "",
           "Ma fiche de contexte pour l'IA. Formation IA, Collège de Bonne-Espérance.",
           "Écrivez votre réponse sous chaque question. Écrivez comme vous parlez: des phrases courtes suffisent.",
           "Ne mettez aucune donnée d'élève. Ensuite, donnez ce fichier à l'IA au début d'une conversation.", ""]
    for title, questions in SECTIONS:
        out += ["", title.upper(), "=" * len(title), ""]
        for _, q, _ in questions:
            out += [q, "", "", ""]
    with open(path, "w", encoding="utf-8-sig", newline="\r\n") as f:
        f.write("\n".join(out).rstrip() + "\n")


def fiche(path):
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("Ma fiche de contexte pour l'IA")
    c.setAuthor("Sébastien Dubois")
    page = 1
    header(c, "Ma fiche de contexte pour l'IA", "Formation IA, Collège de Bonne-Espérance. Ce document vous appartient.")
    y = H - 105
    y = para(c, "À quoi sert cette fiche", M, y, W - 2 * M, BOLD, 11, NAVY)
    y = para(c, "Une IA ne sait rien de vous. Cette fiche vous donne un petit point de départ: qui vous êtes, ce que vous faites, "
             "comment vous travaillez. Avec ce contexte, l'IA comprend mieux ce que vous lui demandez, et ses réponses sont mieux alignées sur votre réalité. "
             "Remplissez-la sur votre PC (les champs se remplissent et s'enregistrent) ou à la main.", M, y - 2, W - 2 * M)
    y = para(c, "Ensuite, copiez vos réponses dans le fichier texte de départ (lien ci-dessous). Il contient les mêmes questions. "
             "C'est la version texte que vous donnerez à l'IA: elle lit un fichier texte beaucoup plus facilement qu'un PDF. "
             "Certains lecteurs de PDF perdent aussi ce que vous avez tapé: le fichier texte est la version sûre. "
             "Il fonctionne avec n'importe quelle IA: donnez-le-lui au début d'une conversation. "
             "Plus tard, il vous permettra aussi d'initialiser votre système IA beaucoup plus facilement.", M, y - 4, W - 2 * M)
    c.setFont(BOLD, 9.5); c.setFillColor(NAVY)
    label = "Fichier de départ: "
    c.drawString(M, y - 2, label)
    lx = M + c.stringWidth(label, BOLD, 9.5)
    c.setFont(REG, 9.5); c.setFillColor(ORANGE)
    c.drawString(lx, y - 2, STARTER_URL_TEXT)
    c.linkURL(STARTER_URL, (lx, y - 5, lx + c.stringWidth(STARTER_URL_TEXT, REG, 9.5), y + 8), relative=0)
    y -= 2 + 9.5 * 1.35
    y = para(c, "Écrivez comme vous parlez. Des phrases courtes suffisent. Ne mettez aucune donnée d'élève.", M, y - 4, W - 2 * M, BOLD, 10, ORANGE)
    y -= 8
    form = c.acroForm
    for title, questions in SECTIONS:
        if y < 170:
            footer(c, "Ma fiche de contexte pour l'IA", page)
            c.showPage(); page += 1
            y = H - 60
        c.setFillColor(NAVY)
        c.setFont(BOLD, 13)
        c.drawString(M, y, title)
        c.setStrokeColor(ORANGE); c.setLineWidth(1.5)
        c.line(M, y - 4, W - M, y - 4)
        y -= 22
        for name, q, lines in questions:
            hbox = 14 * lines + 6
            need = 28 + hbox
            if y - need < 50:
                footer(c, "Ma fiche de contexte pour l'IA", page)
                c.showPage(); page += 1
                y = H - 60
            y = para(c, q, M, y, W - 2 * M, REG, 9.5, HexColor("#222222"))
            y -= 2
            form.textfield(name=name, x=M, y=y - hbox, width=W - 2 * M, height=hbox,
                           borderColor=NAVY, fillColor=HexColor("#f5f7fa"), textColor=HexColor("#111111"),
                           borderWidth=0.8, fontName="Helvetica", fontSize=9, fieldFlags="multiline",
                           forceBorder=True, tooltip=q)
            y -= hbox + 14
    footer(c, "Ma fiche de contexte pour l'IA", page)
    c.save()
    return page


# ---------- Règles d'usage ----------
RULES = [
    ("Les outils autorisés", "Claude Entreprise, avec le compte du collège. Pas de compte personnel ni d'outil gratuit pour des documents de l'école."),
    ("Les données interdites sans accord", "Les données de santé des élèves (bilans logo, rapports médicaux), les dossiers DACCE, les données des parents. Ces données restent hors de portée de l'IA tant que le collège n'a pas validé."),
    ("Ce que l'IA ne fait jamais seule", "Envoyer un message, supprimer un fichier, décider pour un élève. L'IA prépare et résume, une personne décide. Évaluer des élèves peut être un usage à haut risque au sens de l'AI Act."),
    ("Toujours vérifier", "Les faits, les chiffres, les dates et les sources se vérifient dans le document d'origine avant tout usage. La personne qui signe reste responsable."),
    ("Un registre simple", "Pour chaque usage régulier: quel outil, pour quoi faire, quelles données. Une page partagée suffit."),
    ("Le DPO valide", "Le délégué à la protection des données (DPO) du pouvoir organisateur valide les usages qui touchent des données personnelles. La circulaire 9757 finance cette mission."),
    ("La prudence avec les agents", "Ne jamais donner en même temps à un agent l'accès à des données privées, du contenu non fiable (pages web, mails reçus) et un moyen d'envoyer des données dehors. Lire chaque demande de permission avant de dire oui."),
]
TODO = [
    "Vérifier le contrat avec Anthropic: l'accord de traitement des données (DPA), le lieu de traitement et de stockage (États-Unis), la durée de conservation, et les modèles à éviter avec des données personnelles (Fable: 30 jours de conservation au moins).",
    "Choisir la base légale de chaque traitement de données personnelles (RGPD).",
    "Faire une analyse d'impact (AIPD) avant tout usage avec des données sensibles.",
    "Décider s'il faut informer les parents, et comment.",
    "Désigner qui tient le registre et qui le revoit, par exemple une fois par an.",
    "Faire valider ces règles par le pouvoir organisateur.",
]


def regles(path):
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("Projet de règles d'usage de l'IA")
    c.setAuthor("Sébastien Dubois")
    header(c, "Projet de règles d'usage de l'IA", "Formation IA, Collège de Bonne-Espérance. Un point de départ, à compléter par le collège.")
    y = H - 108
    for k, (t, d) in enumerate(RULES, 1):
        c.setFillColor(ORANGE); c.setFont(BOLD, 12); c.drawString(M, y, f"{k}.")
        y2 = para(c, t, M + 20, y, W - 2 * M - 20, BOLD, 11, NAVY)
        y = para(c, d, M + 20, y2 - 1, W - 2 * M - 20, REG, 9.5) - 9
    y -= 4
    c.setStrokeColor(NAVY); c.setLineWidth(1); c.line(M, y + 6, W - M, y + 6)
    y = para(c, "À compléter par le collège, pour éviter les problèmes d'audit", M, y - 10, W - 2 * M, BOLD, 11, NAVY) - 2
    for t in TODO:
        y = para(c, "•  " + t, M + 6, y, W - 2 * M - 6, REG, 9.5) - 2
    y = para(c, "Ce document n'est pas un avis juridique. Il sert de base de discussion avec le pouvoir organisateur et le DPO.",
             M, y - 10, W - 2 * M, REG, 8.5, GREY)
    footer(c, "Projet de règles d'usage de l'IA", 1)
    c.save()


p = fiche(os.path.join(out_dir, "Fiche de contexte pour l'IA.pdf"))
starter(os.path.join(out_dir, STARTER_NAME))
regles(os.path.join(out_dir, "Projet de règles d'usage de l'IA.pdf"))
print("fiche pages", p, "font", REG)


# ---------- Prérequis ----------
STEPS = [
    ("L'application Claude (Claude Desktop)", [
        "Allez sur claude.ai/download et choisissez Windows (ou Mac).",
        "Lancez l'installateur, puis ouvrez Claude.",
        "Cliquez sur \"Se connecter\" et utilisez votre compte Claude Entreprise du collège.",
        "En bas à gauche, vérifiez votre nom et l'organisation du collège: pas un compte personnel.",
    ]),
    ("Google Chrome et l'extension Claude in Chrome", [
        "Utilisez Google Chrome, même si vous travaillez dans Edge: l'extension ne marche officiellement que dans Chrome. "
        "Si Chrome n'est pas sur votre PC, installez-le: google.com/chrome",
        "Dans Chrome, allez sur claude.com/chrome et cliquez sur \"Ajouter à Chrome\".",
        "Épinglez l'extension: l'icône en forme de pièce de puzzle, puis la punaise à côté de Claude.",
        "Cliquez sur l'icône Claude et connectez-vous avec le même compte.",
        "Acceptez les permissions demandées.",
        "Dans Chrome, connectez-vous une fois aux sites que vous utilisez avec Claude (Outlook, OneDrive).",
    ]),
    ("Les fichiers de démo", [
        "Téléchargez le zip: developassion.github.io/atelier-ia-ecole-direction/documents/fichiers-de-demo.zip",
        "Dézippez-le sur le Bureau, pas dans OneDrive. Tous les fichiers sont fictifs.",
    ]),
    ("Un test de deux minutes", [
        "Dans l'application Claude: \"Bonjour, dis-moi en une phrase ce que tu peux faire.\"",
        "Dans Chrome: ouvrez une page web, cliquez sur Claude et demandez \"Résume cette page en trois points.\"",
    ]),
]


LINKS = [("claude.ai/download", "https://claude.ai/download"), ("claude.com/chrome", "https://claude.com/chrome"),
         ("google.com/chrome", "https://www.google.com/chrome/"),
         ("fichiers-de-demo.zip", "https://developassion.github.io/atelier-ia-ecole-direction/documents/fichiers-de-demo.zip")]


def prerequis(path):
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("Avant l'atelier IA du mardi 17 novembre")
    c.setAuthor("Sébastien Dubois")
    header(c, "Avant l'atelier IA", "Mardi 17 novembre 2026 à 10h, au collège. Environ 15 minutes de préparation.")
    y = H - 108
    y = para(c, "Merci de faire ces étapes avant mardi. Si quelque chose bloque, ce n'est pas grave: on le règle ensemble "
             "juste avant le début.", M, y, W - 2 * M, REG, 10.5, HexColor("#222222")) - 8
    for k, (t, items) in enumerate(STEPS, 1):
        c.setFillColor(ORANGE); c.setFont(BOLD, 13); c.drawString(M, y, f"{k}.")
        y = para(c, t, M + 22, y, W - 2 * M - 22, BOLD, 12, NAVY) - 2
        for it in items:
            top = y + 10
            y = para(c, "\u2022  " + it, M + 28, y, W - 2 * M - 28, REG, 10) - 2
            for dom, url in LINKS:
                if dom in it:
                    c.linkURL(url, (M + 28, y + 6, W - M, top), relative=0, thickness=0)
        y -= 8
    c.setStrokeColor(NAVY); c.setLineWidth(1); c.line(M, y + 4, W - M, y + 4)
    y = para(c, "Trois questions, avant l'atelier", M, y - 12, W - 2 * M, BOLD, 12, NAVY) - 2
    y = para(c, "Répondez en quelques lignes par mail à seb@dsebastien.net. Vos réponses rendent l'atelier plus utile pour vous.",
             M + 6, y, W - 2 * M - 6, REG, 10) - 2
    top = y + 22
    c.linkURL("mailto:seb@dsebastien.net", (M + 6, y + 4, W - M, top), relative=0, thickness=0)
    for k, it in enumerate(["Quelle tâche répétitive vous prend le plus de temps? Choisissez-en une, sans données sensibles: on la fera ensemble à la fin de l'atelier.",
                            "Qu'avez-vous déjà essayé avec l'IA, et qu'en avez-vous pensé?",
                            "Qu'est-ce qui vous inquiète ou vous freine avec l'IA?"], 1):
        y = para(c, f"{k}.  " + it, M + 6, y, W - 2 * M - 6, REG, 10) - 2
    y -= 6
    c.line(M, y + 4, W - M, y + 4)
    y = para(c, "Le jour même", M, y - 12, W - 2 * M, BOLD, 12, NAVY) - 2
    for it in ["Votre PC, chargé, avec son chargeur.", "Chrome et l'application Claude ouverts, et connectés.",
               "Les fichiers de votre vraie tâche, copiés dans un dossier à part (sans données sensibles).",
               "Vos questions: notez-les, on les regarde ensemble."]:
        y = para(c, "\u2022  " + it, M + 6, y, W - 2 * M - 6, REG, 10) - 2
    footer(c, "Avant l'atelier IA du mardi 17 novembre", 1)
    c.save()


prerequis(os.path.join(out_dir, "Avant l'atelier - les prérequis.pdf"))
