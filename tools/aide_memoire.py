"""Build the printable cheat sheet: documents/Aide-mémoire - Claude au quotidien.pdf (A4, two pages, three columns).

Usage, from the repository root:  uv run --with reportlab python tools/aide_memoire.py [output folder]
The default output folder is documents/. Keep the content in step with the slides (src/parts/*.md).
"""
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, KeepTogether, PageTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "documents")
os.makedirs(out_dir, exist_ok=True)
OUT = os.path.join(out_dir, "Aide-mémoire - Claude au quotidien.pdf")

FONTS = os.path.join(ROOT, "lib", "fonts")
pdfmetrics.registerFont(TTFont("NS", os.path.join(FONTS, "NotoSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("NSB", os.path.join(FONTS, "NotoSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("NSI", os.path.join(FONTS, "NotoSans-Italic.ttf")))
pdfmetrics.registerFontFamily("NS", normal="NS", bold="NSB", italic="NSI", boldItalic="NSB")

SLATE = HexColor("#37404c")
MAGENTA = HexColor("#e5007d")
INK = HexColor("#1f2329")
SOFT = HexColor("#f6f1f4")
GREY = HexColor("#5b6470")

W, H = A4
M = 22
GAP = 10
TOP = 58          # header band height
BOTTOM = 26
COLS = 3
PAGES = 2
CW = (W - 2 * M - (COLS - 1) * GAP) / COLS

H3 = ParagraphStyle("h3", fontName="NSB", fontSize=9.0, leading=10.8, textColor=MAGENTA, spaceBefore=0, spaceAfter=2.5)
BODY = ParagraphStyle("body", fontName="NS", fontSize=6.95, leading=8.45, textColor=INK, spaceAfter=1.6)
BUL = ParagraphStyle("bul", parent=BODY, leftIndent=8, bulletIndent=0, spaceAfter=1.3)
QUOTE = ParagraphStyle("quote", parent=BODY, fontName="NSI", leftIndent=8, bulletIndent=0, textColor=HexColor("#2b2f36"), spaceAfter=1.4)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=6.6, leading=8.2, textColor=GREY)
CELL = ParagraphStyle("cell", parent=BODY, fontSize=6.6, leading=7.9, spaceAfter=0)
CELLB = ParagraphStyle("cellb", parent=CELL, fontName="NSB")


def b(text):
    return Paragraph(text, BUL, bulletText="•")


def q(text):
    return Paragraph(f"« {text} »", QUOTE, bulletText="›")


def p(text, style=BODY):
    return Paragraph(text, style)


def box(title, items):
    """A titled block that never splits across columns."""
    return KeepTogether([Paragraph(title, H3)] + items + [Spacer(0, 4.5)])


def table(rows, widths):
    data = [[Paragraph(c, CELLB if j == 0 else CELL) for j, c in enumerate(r)] for r in rows]
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [SOFT, white]),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 1.8), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, HexColor("#e2d6dd")),
    ]))
    return t


def decorate(c, doc):
    c.saveState()
    c.setFillColor(SLATE)
    c.rect(0, H - TOP + 8, W, TOP - 8, fill=1, stroke=0)
    c.setFillColor(MAGENTA)
    c.rect(M, H - TOP + 3, 46, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("NSB", 16)
    c.drawString(M, H - 30, "Aide-mémoire: Claude au quotidien")
    c.setFont("NS", 8.2)
    c.drawString(M, H - 44, "Atelier IA pour une direction d'école. À imprimer et à garder à côté du PC. Les noms des menus peuvent changer selon la version de l'application.")
    c.setFillColor(GREY)
    c.setFont("NS", 6.8)
    c.drawString(M, 15, "Novembre 2026: l'IA change vite. Le cours complet: developassion.github.io/atelier-ia-ecole-direction")
    c.drawString(M, 7, "© 2026 Sébastien Dubois · DeveloPassion · Tous droits réservés · seb@dsebastien.net · dsebastien.net · youtube.com/@dsebastien")
    c.drawRightString(W - M, 11, f"Page {doc.page} sur {PAGES}")
    c.restoreState()


story = [
    box("Les cinq règles d'or", [
        b("<b>L'IA prédit, elle ne sait pas.</b> Les faits, les chiffres, les dates et les sources se vérifient toujours."),
        b("<b>Le contexte fait la qualité.</b> Résultat = modèle × contexte. Le contexte est le seul facteur que vous contrôlez."),
        b("<b>Une conversation = un sujet</b>, et une conversation courte."),
        b("<b>Elle propose, vous décidez.</b> Envoyer, supprimer, payer, publier: c'est vous qui validez."),
        b("<b>Votre contexte est votre actif.</b> Gardez-le dans votre base de connaissances, à vous, et sauvegardée."),
    ]),
    box("La recette d'une bonne demande", [
        p("Dites, dans cet ordre si possible:"),
        b("<b>Qui vous êtes</b>: votre rôle, votre école, votre niveau."),
        b("<b>Ce que vous voulez</b>: le résultat, pas la méthode."),
        b("<b>Pour qui</b>: des parents, l'équipe, le pouvoir organisateur."),
        b("<b>Sous quelle forme</b>: longueur, ton, liste, tableau, Word, Excel."),
        b("<b>Un exemple</b>: « écris comme ce mot-ci »."),
        b("<b>Les limites</b>: ce qu'il ne doit pas faire, ce qu'il doit signaler."),
        b("<b>Les critères d'un bon résultat</b>: comment vous allez juger la réponse."),
        p("Mettez <b>les informations et les règles importantes à la fin</b>: la fin d'un long texte est mieux lue que le milieu."),
        p("<b>Dictez</b> (le micro de la zone de saisie): on parle plus vite qu'on écrit, et on donne plus de contexte. Dites beaucoup, quitte à vous répéter: Claude fait le tri."),
    ]),
    box("Des phrases à réutiliser", [
        q("Pose-moi les questions qui te manquent avant de commencer."),
        q("Signale ce que tu ne sais pas au lieu de deviner."),
        q("Pour chaque information, cite la page du document."),
        q("Vérifie tes informations et tes sources, et donne ton niveau de confiance pour chaque résultat."),
        q("Améliore ma demande avant de la faire: qu'est-ce qui manque?"),
        q("Montre-moi d'abord ton plan, et attends mon accord."),
        q("Qu'est-ce qui cloche dans ce plan? Donne-moi les trois meilleures objections."),
        q("Joue l'avocat du diable."),
        q("Essaie de démolir ta propre réponse: failles, dates fausses, oublis."),
        q("Demande à un autre agent de relire ton travail et d'y chercher les erreurs."),
        q("Vérifie chaque date dans le texte."),
        q("Garde le début, refais seulement la fin."),
        q("Plus court. Moins formel. Coupe la slide 4 en deux."),
        q("Donne-moi deux autres versions, très différentes."),
        q("Donne-moi un prompt que je peux passer à un autre agent pour continuer."),
        q("Évalue ta réponse selon ces critères: oui ou non, et pourquoi."),
        q("Utilise mon navigateur Chrome pour..."),
        q("Remplis ce formulaire, mais n'envoie pas."),
    ]),
    box("Choisir le modèle", [
        table([
            ["Sonnet 5.5", "Le simple: un mail, une reformulation, un résumé court."],
            ["Opus 5.5", "Le gros du travail: une circulaire, un tableau, un dossier."],
            ["Haiku", "Rapide et léger."],
            ["Fable", "Le plus puissant, mais très coûteux. Données gardées au moins 30 jours, sans zéro conservation: jamais de données personnelles."],
        ], [CW * 0.27, CW * 0.73]),
        p("De nouveaux modèles sortent très souvent: cette liste date de novembre 2026.", SMALL),
    ]),
    box("Choisir l'effort", [
        b("<b>Bas</b>: brainstorming, brouillon, petite correction. Rapide."),
        b("<b>Moyen</b>: le travail courant."),
        b("<b>Haut</b>: ce qui doit être juste (les dates d'une circulaire, les chiffres d'un tableau). Plus long et plus cher."),
        b("Une <b>demande précise</b> est le levier le moins cher: moins vous précisez, plus Claude décide à votre place."),
    ]),
    box("Les modes de travail", [
        b("<b>Manuel</b>: il demande votre accord avant chaque action. Le plus sûr pour commencer."),
        b("<b>Accepter les modifications</b>: il modifie les fichiers du dossier sans demander chaque fois."),
        b("<b>Plan</b>: il lit et propose un plan, sans rien changer. Vous validez, puis il travaille."),
        b("<b>Auto</b>: il avance seul, et ne demande que pour les actions risquées."),
        p("Conseil: <b>Plan</b> pour une grosse tâche, <b>Manuel</b> au début, <b>Auto</b> seulement sur une copie. Dossier de travail: <b>votre base de connaissances</b> (une copie pour les essais), jamais tout votre OneDrive."),
    ]),
    box("Le contexte, sans se piéger", [
        b("Le contexte, c'est <b>tout ce que Claude voit</b>: vos instructions, la conversation, les documents joints, les pages lues. Le reste, il ne le connaît pas."),
        b("À chaque message, il <b>relit toute la conversation</b>. Entre deux conversations, il ne se souvient de rien, sauf ce qu'il relit: <b>les fichiers de votre base</b>."),
        b("La fenêtre est grande (environ un million de tokens; un token vaut environ trois quarts d'un mot), mais <b>ce qui y tient n'est pas forcément bien lu</b>. Le milieu d'un long texte est moins bien utilisé que le début et la fin."),
        b("Le contexte est <b>limité</b>. Donnez <b>ce qui sert à la tâche</b>, pas tout ce que vous avez: un document inutile peut faire baisser la qualité."),
        b("<b>Signes qu'il faut repartir</b>: il oublie une consigne, se répète, se contredit, invente. Alors: un prompt de passage pour un autre agent, puis une nouvelle conversation."),
        b("<b>La compaction</b> (Claude résume le début d'une conversation trop longue) est <b>peu fiable</b>: beaucoup d'informations se perdent, et les erreurs augmentent. Repartez avant. Ce qui compte va dans votre base."),
        b("Mieux vaut <b>dix conversations courtes</b> qu'une seule longue. Vous pouvez en mener <b>plusieurs en parallèle</b>, une par tâche."),
    ]),
    box("Le coût et les limites", [
        b("On paie en <b>tokens</b>: tout ce que Claude lit, plus tout ce qu'il écrit. Une longue conversation coûte plus à chaque message."),
        b("Opus et l'effort haut coûtent plus que Sonnet et l'effort bas. Le mode rapide aussi."),
        b("Une conversation reprise après une longue pause doit tout relire: elle coûte plus et répond moins bien."),
        b("Regardez votre <b>consommation</b> de temps en temps (dans les paramètres). Si une limite est atteinte, Claude le dit: attendez, ou demandez à l'admin."),
    ]),
    box("Ce que Claude peut faire pour vous", [
        b("<b>Lire</b>: une circulaire de 20 pages, un PDF, une photo d'une page écrite à la main, une capture d'écran."),
        b("<b>Créer des fichiers</b>: un compte rendu Word, un tableau Excel, une présentation PowerPoint, un PDF."),
        b("<b>Ranger un dossier</b>: renommer, trier, écrire un index. Toujours sur une copie, avec le mode Plan."),
        b("<b>Le navigateur</b> (Claude in Chrome): comparer des sites, lire des pages, remplir un formulaire sans l'envoyer."),
        b("<b>L'ordinateur</b>: cliquer et taper dans une application sans connecteur. Plus lent, à surveiller."),
        b("<b>Des artefacts</b> (ce que Claude crée, à droite): un schéma, une affiche simple, un quiz, un petit jeu pour une classe."),
        b("<b>Des connecteurs</b> (MCP, une prise standard entre l'IA et un outil): agenda, mails, fichiers. N'activez que ce qui sert."),
    ]),
    box("Votre base de connaissances", [
        b("<b>Un seul dossier de travail</b> pour l'IA: votre base de connaissances. Des <b>fichiers texte</b> (Markdown: du texte simple, avec # pour les titres)."),
        b("<b>Démarrez chaque conversation</b> dans ce dossier. Pas de projet Claude: tout ce qui doit durer va dans la base. <b>Une seule source de vérité</b>."),
        b("Elle contient le contexte de vos <b>rôles</b>, <b>projets</b>, <b>personnes</b> et <b>processus</b>. La fiche de contexte sert juste de point de départ."),
        b("<b>D'abord pour vous</b>, en bonus pour l'IA: c'est votre second cerveau digital. L'organiser est un travail de long terme, le cœur du système."),
        b("<b>Capturez partout</b> (bureau, téléphone, dictée), puis rangez dans la base. Un journal du jour: un fichier texte par jour."),
        b("<b>La mémoire de Claude: à proscrire.</b> Elle ne vous appartient pas vraiment, elle est peu fiable, et elle retient et ressort des choses un peu au hasard. Désactivez-la."),
    ]),
    box("Sauvegardes", [
        b("<b>Au moins deux copies</b> de la base, dont une hors du PC."),
        b("La synchronisation <b>n'est pas une sauvegarde</b>: une suppression se synchronise aussi."),
        b("Une sauvegarde récente <b>avant</b> de laisser un agent travailler seul. Testez une restauration de temps en temps."),
    ]),
    box("Skills, commandes, styles", [
        b("<b>Une skill</b> est une recette écrite une fois: quand l'utiliser, les étapes, les règles, un exemple, les critères. Claude la suit chaque fois."),
        b("Cherchez les tâches <b>répétitives et fréquentes</b>: mot aux parents, tri des circulaires, revue du lundi, compte rendu."),
        b("Créez-les avec <b>la skill de création de skills</b> (skill-creator), <b>selon la spécification</b> agentskills.io/specification.md: un dossier, un fichier SKILL.md (nom, description, puis les étapes). Corrigez la skill, pas seulement la réponse. Gardez son texte dans votre base."),
        b("<b>Documentez vos processus</b>: l'IA ne fait bien que ce qui est bien décrit."),
        b("<b>Tapez « / »</b> pour la liste des skills et des commandes. Un <b>style</b> d'écriture garde votre ton."),
    ]),
    box("Plusieurs agents, plusieurs regards", [
        b("<b>Diverger, puis converger</b>: « 20 idées, sans juger », puis « classe-les selon ces trois critères, garde les trois meilleures »."),
        b("<b>Débat</b>: un agent défend, un autre attaque, un troisième tranche. Vous décidez."),
        b("<b>Panel</b>: « Relis comme un parent pressé, un parent qui lit mal le français, l'inspection »."),
        b("<b>L'IA comme juge</b>: un agent note le travail d'un autre avec votre grille. Il préfère les réponses longues: gardez le dernier mot."),
    ]),
    box("Prudence: les données de l'école", [
        b("<b>Jamais d'outil gratuit ou personnel</b> (ChatGPT, Gemini, Claude gratuit) pour un document de l'école: aucun contrat, et les données peuvent servir à entraîner les modèles. C'est une fuite de données (RGPD)."),
        b("Seulement <b>le compte Claude du collège</b>. Vérifiez le nom de l'organisation en bas à gauche de l'application."),
        b("<b>Interdit sans accord</b>: la santé des élèves, les dossiers DACCE, les données des parents. Le DPO du pouvoir organisateur valide les usages avec des données personnelles."),
        b("<b>Les biais</b>: les réponses reflètent les préjugés des textes d'entraînement. Prudence avec tout ce qui juge une personne (un élève, un candidat)."),
    ]),
    box("Vos données chez le fournisseur", [
        b("Chez Anthropic, les données sont <b>stockées aux États-Unis</b>; pas d'option Europe dans l'abonnement Entreprise, selon sa documentation."),
        b("Le <b>DPA</b> (accord de traitement des données, RGPD) encadre ce que le fournisseur fait des données. Le <b>ZDR</b> (zéro conservation) existe pour certains usages, pas avec Fable."),
        b("Le collège reste <b>responsable</b> (RGPD). L'<b>AI Act</b> impose la formation du personnel et encadre les usages à haut risque."),
        b("Un <b>pouce levé ou baissé</b> peut autoriser une conservation plus longue: évitez-le avec des données sensibles."),
    ]),
    box("Claude sur le téléphone", [
        b("Le même compte, les mêmes conversations. Idéal pour <b>capturer</b> en dictant."),
        b("Le téléphone <b>n'a pas accès à votre base</b> sur le PC: capturez, puis rangez au bureau. Ou donnez la tâche à Claude sur le PC (Dispatch, selon l'abonnement; le PC reste allumé)."),
        b("<b>Compte du collège</b>, code de verrouillage, pas de photo de documents d'élèves, pas de documents sensibles enregistrés."),
    ]),
    box("Prudence: les agents", [
        b("<b>La triple menace</b>: un agent devient dangereux quand il a les trois en même temps: des <b>données privées</b>, du <b>contenu non fiable</b> (page web, mail reçu, PDF inconnu) et un moyen d'<b>envoyer dehors</b> (mail, formulaire). Ne donnez jamais les trois sans regarder."),
        b("Une page web peut cacher des <b>instructions pour l'IA</b>. Sites de confiance, et regardez ce qu'il fait."),
        b("<b>Lisez chaque demande de permission</b> avant de dire oui."),
        b("Travaillez sur <b>une copie</b> des fichiers, surtout en mode Auto."),
    ]),
    box("Sept erreurs courantes", [
        b("Croire la réponse sans vérifier."),
        b("Mettre des données d'élèves ou de parents sans règle claire."),
        b("Donner trop peu de contexte, puis conclure que « l'IA est nulle »."),
        b("Garder une seule conversation interminable pour tout."),
        b("Laisser un agent agir sur un site web sans regarder."),
        b("Copier-coller sans relire: c'est vous qui signez."),
        b("Juger Claude sur un seul essai, ou prendre la première réponse pour la meilleure. Testez-le sur vos vraies tâches, plusieurs fois."),
    ]),
    box("Gagner du temps chaque semaine", [
        b("Gardez vos <b>meilleures demandes</b> dans un document, et réutilisez-les."),
        b("Pour une grosse tâche: <b>d'abord un plan</b>, validez-le, puis lancez le travail. Faites autre chose pendant qu'il travaille."),
        b("Commencez par les tâches <b>faciles à vérifier</b>: un tableau tiré d'un document, un résumé que vous pouvez relire."),
        b("Corrigez par <b>petites phrases</b> au lieu de tout réécrire. Si ça part mal: nouvelle conversation, avec une demande plus précise."),
        b("<b>Tâches planifiées</b> (selon la version): une seule pour commencer, par exemple la revue du lundi à 7h. Relisez ses résultats."),
        b("Vous décidez <b>quand vous arrêtez</b>: l'IA produit vite, on peut vite en faire trop."),
    ]),
    box("Démarrer dès demain (15 minutes)", [
        Paragraph("Créer le dossier de <b>votre base de connaissances</b>, sauvegardé. Y mettre votre fichier « À propos de moi.txt » (vos réponses à la fiche de contexte), le règlement, le calendrier.", BUL, bulletText="1."),
        Paragraph("Ouvrir Claude <b>sur ce dossier</b> (le dossier de travail).", BUL, bulletText="2."),
        Paragraph("Faire une <b>vraie tâche</b> de la semaine dans ce dossier: un mail, un tableau, une circulaire.", BUL, bulletText="3."),
        p("Puis chaque jour, 2 minutes: le <b>journal du jour</b>, un fichier texte par jour dans la base. Tout y va: appels, idées, décisions, choses à faire. Une fois par semaine, on relit et on range."),
    ]),
    box("L'habitude de noter", [
        b("Noter <b>tout de suite</b>: une idée, une décision, un appel, une chose à faire."),
        b("Noter <b>ce qui compte</b>, pas tout. Et <b>le contexte</b>: pourquoi, avec qui, quelle suite."),
        b("<b>Double gain</b>: votre tête se libère aujourd'hui, et chaque note rend l'IA plus utile demain."),
        b("Questions utiles au journal: « Qu'est-ce que j'ai promis cette semaine? », « Qu'est-ce qui est resté en suspens? »"),
    ]),
    box("Des demandes prêtes pour l'école", [
        p("À copier telles quelles: Claude vous demande ce qui manque. Ajoutez votre rôle si le projet Claude ne le dit pas déjà.", SMALL),
        q("Lis cette circulaire et fais un tableau des actions pour mon niveau (demande-le-moi si tu ne le sais pas): action, date limite, qui, page. Signale les dates déjà passées."),
        q("Fais un compte rendu Word de ces notes de réunion: participants, décisions, puis un tableau des actions (quoi, qui, pour quand)."),
        q("Fais un tableau Excel de ces sorties: date, classe, lieu, prix, payé, réservé. Laisse vide ce que tu ne sais pas."),
        q("Écris un mot aux parents pour une sortie. Pose-moi d'abord tes questions (classe, date, prix, échéance). 120 mots, vouvoiement, avec un talon-réponse."),
        q("Fais une présentation de 10 slides pour la réunion de parents, à partir de ce texte. Une idée par slide."),
        q("Prépare l'ordre du jour de la prochaine réunion d'équipe à partir de ces notes, et ce qui manque pour que chaque action soit claire."),
        q("Ce mail d'un parent est tendu. Propose une réponse calme et ferme, puis dis-moi ce qui pourrait être mal compris."),
        q("Voici une photo de ma page de notes. Fais-en un tableau, et signale ce que tu ne lis pas."),
    ]),
    box("Les réglages à faire une fois", [
        b("Vérifier que l'application est connectée au <b>compte du collège</b> (nom de l'organisation en bas à gauche)."),
        b("<b>Désactiver la mémoire</b> de Claude dans les paramètres."),
        b("Créer le dossier de <b>votre base de connaissances</b>, et le choisir comme <b>dossier de travail</b>. Mettre en place sa <b>sauvegarde</b>."),
        b("Choisir ou créer un <b>style</b> d'écriture à votre ton."),
        b("Installer <b>Google Chrome</b> (même si vous utilisez Edge: l'extension ne marche officiellement que dans Chrome), puis l'extension Claude in Chrome, <b>épinglée</b> et connectée au <b>même compte</b>."),
    ]),
    box("Quand ça ne va pas", [
        b("<b>Réponse générique</b>: il manque du contexte. Dites qui, pour qui, quelle forme, avec un exemple."),
        b("<b>Une erreur</b>: demandez la page ou la source, passez en effort haut, faites relire par un autre agent."),
        b("<b>Il tourne en rond</b>: demandez un prompt de passage pour un autre agent, puis une nouvelle conversation."),
        b("<b>Trop long, trop formel</b>: « plus court », « moins formel », « en trois points »."),
        b("<b>Il vous donne raison sur tout</b>: demandez les objections, ou de jouer l'avocat du diable."),
        b("<b>Limite atteinte</b>: attendez, ou demandez à l'admin. Puis des conversations plus courtes."),
        b("<b>Chrome ne répond pas</b>: Chrome ouvert? Extension connectée au même compte que l'application?"),
    ]),
    box("Vérifier en une minute", [
        b("Ouvrez <b>deux pages citées</b> au hasard et comparez."),
        b("Relisez <b>toutes les dates</b> et <b>tous les montants</b>: ce sont les erreurs les plus fréquentes."),
        b("Vérifiez les <b>noms propres</b>: personnes, lieux, références."),
        b("Demandez: « De quoi n'es-tu pas sûr? »"),
    ]),
    box("Quand ne pas utiliser l'IA", [
        b("Pour <b>décider à la place</b> d'une personne au sujet d'un élève, d'un parent ou d'un membre de l'équipe."),
        b("Avec des <b>données sensibles</b> sans accord du collège et du DPO."),
        b("Quand vous <b>ne pouvez pas vérifier</b> le résultat et qu'il engage l'école."),
        b("Quand un échange humain compte plus qu'un texte bien écrit."),
    ]),
    box("Les mots à connaître", [
        table([
            ["Token", "Un morceau de texte, environ trois quarts d'un mot. L'unité de mesure et de prix."],
            ["Prompt", "Votre demande. Une partie du contexte, pas tout le contexte."],
            ["Contexte", "Tout ce que Claude voit au moment de répondre."],
            ["Hallucination", "Un fait inventé, dit avec aplomb."],
            ["Complaisance", "Sa tendance à vous donner raison. Demandez-lui de critiquer."],
            ["Agent", "Une IA qui agit (fichiers, web, applications), pas seulement qui répond."],
            ["Artefact", "Ce que Claude crée: document, tableau, présentation, petit jeu."],
            ["Compaction", "Le résumé automatique du début d'une longue conversation."],
            ["Cache", "Claude garde le début de la conversation quelques minutes: plus rapide, moins cher."],
            ["Connecteur", "Un accès à un autre outil (agenda, mails), par MCP."],
            ["Fenêtre", "La fenêtre de contexte: le maximum de texte lu en une fois (environ un million de tokens)."],
            ["Effort", "Combien de travail Claude met dans une tâche: bas, moyen, haut."],
            ["Base de connaissances", "Votre dossier de fichiers texte: la source unique de contexte, pour vous et pour l'IA."],
            ["Markdown", "Du texte simple, avec # pour les titres. Lisible par vous et par toutes les IA."],
            ["DPA", "L'accord de traitement des données entre le collège et le fournisseur (RGPD)."],
            ["ZDR", "Zéro conservation: le fournisseur ne garde rien après la réponse."],
            ["Skill", "Une façon de faire écrite une fois, que Claude suit chaque fois."],
            ["LLM", "Grand modèle de langage: il prédit la suite la plus probable d'un texte."],
        ], [CW * 0.33, CW * 0.67]),
    ]),
]


def build():
    doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=TOP, bottomMargin=BOTTOM,
                          title="Aide-mémoire: Claude au quotidien", author="Sébastien Dubois",
                          subject="Atelier IA pour une direction d'école")
    fh = H - TOP - BOTTOM - 4
    frames = [Frame(M + i * (CW + GAP), BOTTOM, CW, fh, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id=f"c{i}")
              for i in range(COLS)]
    doc.addPageTemplates([PageTemplate(id="p", frames=frames, onPage=decorate)])
    doc.build(story)
    return doc.page


pages = build()
print(f"{OUT} pages={pages}")
if pages != PAGES:
    print(f"WARNING: the cheat sheet must fit on {PAGES} pages, it has {pages}", file=sys.stderr)
    sys.exit(1)
