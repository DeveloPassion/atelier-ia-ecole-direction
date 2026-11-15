# 1 - Introduction

---
## L'IA au service de l'école
- Claude Entreprise: comprendre, démarrer, **rester maître de ses données**
- Environ 2 heures
- Ce support se relit seul, après la séance
- Les personnes et les documents de démo sont fictifs: ce support sert à apprendre

Note: Se présenter en une phrase. Dire que le support est fait pour continuer seuls: chaque slide porte une idée complète, et la fin dit quoi faire dès demain. Ce qu'on ne voit pas aujourd'hui se relit seul.

---
## Qui suis-je?
<div class="me"><img src="lib/img/sebastien-dubois.jpg" alt="Portrait de Sébastien Dubois"><ul>
<li><strong>Sébastien Dubois</strong>. <strong>Professionnel de l'IT</strong> depuis 20 ans (développement, infrastructure, sécurité, ...)</li>
<li>Je dirige aussi une société IT, <strong>DeveloPassion</strong></li>
<li>J'utilise l'IA <strong>tous les jours</strong>, depuis bientôt 4 ans</li>
<li>À la tête du groupe de travail <strong>IA Agentique</strong> de la Banque nationale de Belgique, où je travaille à temps partiel</li>
<li><strong>Expert et coach</strong> en <strong>gestion des connaissances</strong></li>
</ul></div>
<p class="doc"><b>Me retrouver:</b> <a href="https://www.dsebastien.net">dsebastien.net</a> · <a href="https://www.youtube.com/@dsebastien">YouTube</a> · <a href="https://notes.dsebastien.net">Mes notes publiques</a></p>

Note: ESSENTIEL. Une minute, pas plus. Le but: dire d'où je parle (l'IT, la sécurité, l'IA au quotidien, la gestion des connaissances), pas raconter mon parcours.

---
## Quatre objectifs pour aujourd'hui
1. **Démarrer rapidement avec Claude**: faire une vraie tâche, lui donner le bon contexte, et **vérifier** ce qu'il délivre
2. **Comprendre l'IA agentique et les possibilités de Claude**: ce qu'il peut faire pour vous, et les règles à suivre avec les données de l'école
3. **Découvrir la gestion des connaissances**, et sa valeur pour l'humain et pour l'IA
4. **Comprendre la valeur d'un système IA souverain**: un système qui vous connaît, et **qui vous appartient**

Note: ESSENTIEL. Quatre objectifs seulement: on ne peut pas tout faire en deux heures. Le reste du support se relit seul.

---
## Au programme
1. Introduction
2. Prise en main: l'application, les modèles, l'effort, puis un premier exercice
3. Première démo, sur votre PC: la circulaire
4. Comprendre ce qu'on vient de voir
5. Le contexte et sa gestion
6. Cowork, les démos, et **votre vraie tâche**
7. Un système qui vous connaît, et qui vous appartient
8. Prudence et règles d'usage
9. Démarrer demain, et vos questions

Et 9 parties bonus, à parcourir après la séance.

Note: À PASSER si le temps manque. Timing visé (début à 10h): 0:04 fin de la partie 1, 0:16 fin de la partie 2, 0:26 fin de la circulaire, 0:35 fin de la partie 4, 0:45 fin de la partie 5, pause jusqu'à 0:55, 1:30 fin de la partie 6 (avec leur vraie tâche, 15 minutes), 1:44 fin de la partie 7, 1:49 fin de la partie 8, 2:00 fin de la partie 9 (avec leurs questions). Trois repères à tenir: la pause commence à 0:45; la vraie tâche commence à 1:08 au plus tard; la partie 8 commence à 1:42. Dans chaque partie, les notes disent "ESSENTIEL" ou "À PASSER": en séance, je montre seulement les slides essentielles. Le reste est pour la relecture.

---
## Organisation de l'atelier
- **Chacun sur son PC**: vous faites les démos avec moi
- Le dossier "Fichiers de démo" est sur votre PC. **Tout y est fictif**
- Pendant l'atelier: **aucune donnée d'élève**, aucune donnée sensible
- **N'hésitez pas à m'interrompre**

Note: ESSENTIEL. Dire la règle sur les données maintenant, avant la première démo. Le détail (l'accord de l'école et du DPO, le compte Claude de l'école) est en partie 8. Poser une feuille sur la table pour noter les questions à reprendre à la fin, ou par la suite (par mail, ou dans une deuxième séance). Vérifier que chacun a ouvert l'application Claude et le dossier "Fichiers de démo".

---
## Avant de commencer: les prérequis
1. **L'application Claude** est ouverte. En bas à gauche, vous voyez **le nom de l'école**: c'est le bon compte
2. **Microsoft Edge** (ou Google Chrome) est ouvert, avec l'extension **Claude in Chrome** connectée au même compte
3. Le dossier **"Fichiers de démo"** est sur votre Bureau, **hors OneDrive**: pour l'atelier, il nous faut des fichiers qui sont vraiment sur le PC
4. Modèle sélectionné: **Opus 5.5**

Note: À PASSER si le temps manque. VÉRIFICATION DES PRÉREQUIS (10 minutes avant le début, ou la veille par mail).
Claude Desktop: 1) Aller sur [claude.ai/download](https://claude.ai/download) et choisir Windows (ou Mac). 2) Lancer l'installateur. 3) Ouvrir Claude, cliquer sur "Se connecter", et choisir la connexion de l'école (connexion unique si l'admin l'a activée, sinon l'adresse mail de l'école). 4) En bas à gauche, vérifier le nom et l'organisation de l'école: pas un compte personnel.
Claude in Chrome: on part du principe que l'école utilise Microsoft Edge. L'extension s'installe dans Edge ou dans Google Chrome. Deux sources, lues le 14/11/2026, ne disent pas la même chose. La documentation de Claude Code: l'intégration marche avec Google Chrome et Microsoft Edge. Le centre d'aide ("Getting started with Claude in Chrome"): l'extension n'est pas prise en charge dans les autres navigateurs Chromium. Donc tester dans Edge avant la séance, y compris depuis l'application Claude (Cowork). Plan B si elle ne répond pas dans Edge: Google Chrome ([google.com/chrome](https://www.google.com/chrome/)). 1) Dans Edge ou Chrome, aller sur [claude.com/chrome](https://claude.com/chrome) et cliquer sur "Ajouter à Chrome" (Chrome Web Store). Si Edge le demande, autoriser d'abord les extensions d'autres magasins. 2) Épingler l'extension: icône en forme de pièce de puzzle, puis la punaise (Chrome) ou l'œil (Edge) à côté de Claude. 3) Cliquer sur l'icône Claude et se connecter avec le même compte. 4) Accepter les permissions demandées. Si l'extension est bloquée, l'admin doit l'activer pour l'organisation.
Test rapide: dans l'application, "Bonjour, dis-moi en une phrase ce que tu peux faire". Dans le navigateur, ouvrir une page web et demander "Résume cette page en trois points".
Si un PC bloque l'installation: travailler à deux sur un PC, ou utiliser [claude.ai](https://claude.ai) dans le navigateur (sans les démos sur un dossier). À vérifier en plus sur chaque PC, avec une liste imprimée: Cowork n'est pas coupé par l'admin, Opus 5.5 est permis, l'extension est bien reliée à l'application, et un dossier hors OneDrive s'ouvre comme dossier de travail. Si Cowork est coupé: faire les démos de la partie 6 sur mon écran, et leur vraie tâche dans le chat, avec des fichiers joints.
