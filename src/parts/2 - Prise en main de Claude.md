# 2 - Prise en main de Claude

---
## 2. Prise en main
Claude est l'IA de la société Anthropic.

- D'autres IA existent: GPT (ChatGPT), Gemini, Mistral, DeepSeek, Qwen, ...
- Elles fonctionnent toutes sur le même principe: **ce que vous apprenez ici vaut aussi pour elles**

---
## L'application Claude
<div class="chart tall"><svg viewBox="0 0 960 342" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma de l'application: les conversations à gauche, la conversation au centre, la zone de saisie en bas, les artefacts à droite">
<rect x="20" y="10" width="920" height="322" rx="12" fill="#2b323c" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>
<rect x="20" y="10" width="200" height="322" rx="12" fill="#333b47"/>
<rect x="680" y="10" width="260" height="322" rx="12" fill="#333b47"/>
<circle cx="46" cy="42" r="11" fill="#e5007d"/><text x="46" y="46.5" font-size="13" fill="#fff" font-weight="700" text-anchor="middle">1</text>
<text x="64" y="47" font-size="15" fill="#fff" font-weight="700" text-anchor="start">Vos conversations</text>
<text x="64" y="66" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">et vos projets</text>
<rect x="40" y="88" width="150" height="10" rx="5" fill="rgba(255,255,255,0.15)"/>
<rect x="40" y="110" width="120" height="10" rx="5" fill="rgba(255,255,255,0.15)"/>
<rect x="40" y="132" width="140" height="10" rx="5" fill="rgba(255,255,255,0.15)"/>
<rect x="40" y="154" width="100" height="10" rx="5" fill="rgba(255,255,255,0.15)"/>
<circle cx="46" cy="282" r="11" fill="#e5007d"/><text x="46" y="286.5" font-size="13" fill="#fff" font-weight="700" text-anchor="middle">5</text>
<text x="64" y="287" font-size="15" fill="#fff" font-weight="700" text-anchor="start">Les paramètres</text>
<text x="40" y="307" font-size="12.5" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">connecteurs · skills · mémoire</text>
<circle cx="256" cy="42" r="11" fill="#e5007d"/><text x="256" y="46.5" font-size="13" fill="#fff" font-weight="700" text-anchor="middle">2</text>
<text x="274" y="47" font-size="15" fill="#fff" font-weight="700" text-anchor="start">La conversation</text>
<rect x="450" y="62" width="210" height="30" rx="14" fill="rgba(229,0,125,0.6)"/>
<rect x="240" y="102" width="330" height="62" rx="14" fill="#475363"/>
<rect x="256" y="118" width="250" height="9" rx="4" fill="rgba(255,255,255,0.3)"/>
<rect x="256" y="136" width="200" height="9" rx="4" fill="rgba(255,255,255,0.3)"/>
<rect x="240" y="196" width="420" height="120" rx="12" fill="#3f4957" stroke="#ff4fa8" stroke-width="2"/>
<circle cx="266" cy="222" r="11" fill="#e5007d"/><text x="266" y="226.5" font-size="13" fill="#fff" font-weight="700" text-anchor="middle">3</text>
<text x="284" y="227" font-size="15" fill="#fff" font-weight="700" text-anchor="start">La zone de saisie</text>
<text x="256" y="250" font-size="13.5" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">écrire · dicter au micro · joindre un fichier</text>
<rect x="256" y="264" width="90" height="32" rx="16" fill="#2b323c" stroke="rgba(255,255,255,0.3)"/>
<text x="301" y="285" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Dossier</text>
<rect x="354" y="264" width="90" height="32" rx="16" fill="#2b323c" stroke="rgba(255,255,255,0.3)"/>
<text x="399" y="285" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Modèle</text>
<rect x="452" y="264" width="90" height="32" rx="16" fill="#2b323c" stroke="rgba(255,255,255,0.3)"/>
<text x="497" y="285" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Effort</text>
<rect x="550" y="264" width="90" height="32" rx="16" fill="#2b323c" stroke="rgba(255,255,255,0.3)"/>
<text x="595" y="285" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Mode</text>
<circle cx="706" cy="42" r="11" fill="#e5007d"/><text x="706" y="46.5" font-size="13" fill="#fff" font-weight="700" text-anchor="middle">4</text>
<text x="724" y="47" font-size="15" fill="#fff" font-weight="700" text-anchor="start">Les artefacts</text>
<text x="700" y="66" font-size="13.5" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">ce que Claude crée pour vous</text>
<rect x="700" y="84" width="220" height="230" rx="6" fill="#f5f5f5"/>
<rect x="716" y="102" width="130" height="12" rx="3" fill="#37404c"/>
<rect x="716" y="128" width="188" height="7" rx="3" fill="#b8bec6"/>
<rect x="716" y="144" width="170" height="7" rx="3" fill="#b8bec6"/>
<rect x="716" y="160" width="188" height="7" rx="3" fill="#b8bec6"/>
<rect x="716" y="176" width="120" height="7" rx="3" fill="#b8bec6"/>
<rect x="716" y="202" width="188" height="96" rx="4" fill="#fff" stroke="#b8bec6"/>
<rect x="716" y="202" width="188" height="20" rx="4" fill="#e5007d"/>
<line x1="716" y1="241" x2="904" y2="241" stroke="#b8bec6"/>
<line x1="716" y1="260" x2="904" y2="260" stroke="#b8bec6"/>
<line x1="716" y1="279" x2="904" y2="279" stroke="#b8bec6"/>
<line x1="779" y1="202" x2="779" y2="298" stroke="#b8bec6"/>
<line x1="842" y1="202" x2="842" y2="298" stroke="#b8bec6"/>
</svg></div>

Mon conseil: **dictez**. On parle bien plus vite qu'on écrit, et on donne naturellement plus de contexte.

Note: ESSENTIEL. TOUR DE L'APPLICATION (4 min), chacun sur son PC. Suivre les numéros du dessin, et montrer chaque zone en une phrase: 1) les conversations et les projets, 2) la conversation, 3) la zone de saisie, pour écrire, dicter, joindre un fichier, avec ses réglages (slide suivante), 4) les artefacts: un document, une présentation, un tableau, 5) les paramètres: les connecteurs, les skills, la mémoire. Le dessin est un plan: l'écran réel change un peu selon la version. À dire pour la zone 4: un artefact reste dans l'application, chez Anthropic. C'est très bien pour un essai. Pour ce qui doit durer, on demande un fichier dans le dossier de travail (partie 6). Montrer le micro de la zone de saisie et dicter une demande en direct: c'est souvent ce qui surprend le plus. Ouvrir les paramètres et montrer Connecteurs et Skills sans rien changer. Montrer aussi l'extension Claude in Chrome dans Chrome.

---
## Les réglages sous la zone de saisie
- **Le dossier de travail**: le dossier que Claude peut lire et modifier
- **Le modèle** et **l'effort**: qui réfléchit, et combien
- **Le mode rapide**: des réponses plus rapides, qui consomment plus de budget
- **Le mode de travail**: le niveau de liberté de Claude

Documentation: [Commencer avec Claude Cowork](https://support.claude.com/fr/articles/13345190)

Note: À PASSER si le temps manque. Montrer chaque réglage en direct, chacun sur son PC. Les noms exacts peuvent changer selon la version et la langue de l'application: vérifier avant la séance. Selon le centre d'aide (lu le 13/11/2026), Claude ne lit et n'écrit que dans les dossiers que vous lui avez ouverts; l'application les liste dans ses paramètres ("Trusted folders" dans la version en anglais). La documentation ne nomme pas le bouton qui sert à choisir le dossier: le montrer en direct.

---
## Les modèles Anthropic
| Modèle | Pour quoi |
|---|---|
| Fable 5.2 | Le plus puissant, et le plus cher: seulement pour une tâche qui le justifie |
| **Opus 5.5** | **Le gros du travail**: une circulaire, un tableau, un dossier |
| **Sonnet 5.5** | **Le choix de tous les jours**: un mail, une reformulation, un résumé |
| Haiku 5.5 | Rapide et léger: une question simple, une tâche basique |

- Le modèle est **le premier levier de coût**: Opus coûte environ 2 fois plus que Sonnet
- Avec **Fable 5.2**, vos conversations restent **au moins 30 jours** chez Anthropic, quoi que vous fassiez: **jamais de données sensibles** avec ce modèle
- De nouveaux modèles sortent **très souvent**: cette recommandation date de novembre 2026

Note: ESSENTIEL. Sur Entreprise, l'usage se paie au volume (bonus 18). Vérifier avant la séance que l'admin autorise Sonnet 5.5 et Opus 5.5. Fable 5, 5.1 et 5.2 (la version actuelle, ajoutée à la liste le 09/11/2026) sont des "Covered Models" chez Anthropic: conservation des données d'au moins 30 jours, examinées par des systèmes de sécurité automatiques, et pas de zéro conservation (ZDR) pour les organisations Claude Enterprise (centre d'aide d'Anthropic, article "Covered Models", vérifié le 12/11/2026). L'article parle d'une option ZDR limitée dans le temps pour certains clients: à voir avec Anthropic, ne pas compter dessus. Conseil: Fable seulement pour une tâche qui le justifie, et jamais avec des données personnelles.

---
## Le niveau d'effort
L'effort dit **combien de travail** Claude met dans une tâche.

- **Effort bas**: rapide. Une première version, à corriger ensemble
- **Effort haut**: plus long. Il vérifie, il teste, il décide plus de choses seul
- Sur une grosse tâche, Claude peut **travailler des heures sans s'arrêter**: il lit, essaie, vérifie et recommence, pendant que vous faites autre chose
- Plus d'effort prend plus de temps, et **plus de budget**
- On donne 1 heure pour une tâche: on rend une première version. On donne 12 heures: on vérifie tout. Claude lit l'effort de la même façon

Note: ESSENTIEL. Analogie de Thariq Shihipar (Anthropic), article "Spending your effort", 2026-09-25. Dans ses tests, une même demande a pris 1 minute et demie en effort bas, et plus d'une heure en effort maximum.

---
## Quel effort choisir
- Effort bas: brainstorming, brouillon, petite correction
- Effort moyen: le travail courant
- Effort haut: **ce qui doit être juste** (les dates d'une circulaire, les chiffres d'un tableau)
- Moins vous précisez, plus Claude décide à votre place. **Une demande précise** est le levier le moins cher

Note: À PASSER si le temps manque.

---
## Le mode rapide
- **Le même modèle, la même qualité**, mais des réponses jusqu'à **2,5 fois plus rapides**
- Le prix: **2 fois plus cher**. Seulement avec **Opus 5.5** et **Fable 5.2**
- Sur un compte d'école, il est **coupé au départ**: c'est un propriétaire de l'organisation qui l'active
- Mon conseil: **vous n'en avez pas besoin** pour commencer. Pour aller plus vite, prenez plutôt Sonnet, ou un effort plus bas

Note: À PASSER si le temps manque. Lu le 16/11/2026 dans la documentation de Claude Code ("Speed up responses with fast mode"): le mode rapide garde le même modèle et la même qualité, il répond jusqu'à 2,5 fois plus vite, et il coûte plus cher par token (Opus 5.5: 8 et 40 dollars par million de tokens lus et écrits, contre 4 et 20; Fable 5.2: 16 et 80). Il n'existe pas pour Sonnet ni pour Haiku. Sur Team et Entreprise, il est coupé par défaut: un propriétaire de l'organisation l'active, et il se paie sur les crédits d'usage de l'organisation. La documentation décrit ce mode pour Claude Code (un interrupteur dans le menu du modèle). Elle ne le décrit pas pour le chat de l'application: à vérifier sur leur PC. S'ils ne voient pas ce réglage, passer la slide, et dire que c'est normal.

---
## Le niveau de liberté de Claude
Un réglage, dans la zone de saisie:

- **Manuel**: Claude demande votre accord **avant chaque action**. C'est le réglage de départ sur le compte de l'école, et le bon choix pour commencer
- **Auto**: il avance seul, il vérifie chaque action, et il bloque ce qui lui paraît dangereux. Seulement **sur une copie**
- **Ignorer**: il ne demande rien. Permet de gagner du temps, mais **plus risqué**

Pour une grosse tâche, demandez d'abord **un plan**: "Montre-moi d'abord ton plan, et attends mon accord."{copy}

Note: ESSENTIEL. Noms lus le 13/11/2026 dans le centre d'aide en français ("Commencer avec Claude Cowork"): "Manuel" (avant: "Demander avant d'agir"), "Auto", "Ignorer" (avant: "Agir sans demander"). Sur Entreprise, le réglage de départ est "Manuel", et l'admin peut couper "Auto". Si leur application montre d'autres noms (par exemple "Plan" ou "Accepter les modifications"), le principe reste le même: plus Claude agit seul, plus il faut un dossier de travail limité et une copie des fichiers. À VÉRIFIER sur leur PC avant la séance. Lien avec la partie 8.

---
## Quand Claude demande la permission
<div class="chart"><svg viewBox="0 0 960 176" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dessin: une demande de permission, avec trois boutons: refuser, autoriser une fois, toujours autoriser">
<rect x="150" y="8" width="660" height="160" rx="14" fill="#2b323c" stroke="rgba(255,255,255,0.45)" stroke-width="2"/>
<text x="180" y="44" font-size="19" fill="#fff" font-weight="700" text-anchor="start">Claude veut modifier un fichier</text>
<text x="180" y="72" font-size="16" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">Sorties pédagogiques 2026-2027.xlsx</text>
<rect x="180" y="100" width="150" height="44" rx="22" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="2"/>
<text x="255" y="128" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">Refuser</text>
<rect x="346" y="100" width="210" height="44" rx="22" fill="#e5007d"/>
<text x="451" y="128" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">Autoriser une fois</text>
<rect x="572" y="100" width="210" height="44" rx="22" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="6 5"/>
<text x="677" y="128" font-size="16" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">Toujours autoriser</text>
<text x="677" y="160" font-size="13" fill="#fbbf24" font-weight="700" text-anchor="middle">pas pour l'instant</text>
</svg></div>

- **Lisez** ce qu'il veut faire: quelle action, sur quel fichier ou sur quel site
- **Autoriser une fois**: oui, si c'est bien ce que vous avez demandé. **Toujours autoriser**: pas pour l'instant
- Un doute? **Refusez**, et demandez-lui d'expliquer ce qu'il voulait faire
- Envoyer, supprimer, payer, publier: **c'est vous qui validez**

Note: ESSENTIEL. Le dessin montre le principe: l'écran réel change selon la version, et les boutons peuvent s'appeler autrement. La première vraie demande de permission arrive pendant la démo 2: s'arrêter dessus avec la salle, et la lire à voix haute. Refuser n'abîme rien: Claude explique, et on recommence. Pour supprimer un fichier pour de bon, Claude demande toujours.

---
## Le prompt
Le prompt, c'est la demande que vous écrivez: **une partie du contexte**, pas tout. La recette, en six points:

1. **Qui vous êtes**
2. **Ce que vous voulez**
3. **Pour qui**
4. **Sous quelle forme** (longueur, ton, liste ou texte)
5. **Un exemple**, si vous en avez un
6. **Les règles et les critères** d'un bon résultat

**Commencez simple**: ajoutez des consignes seulement si le résultat ne convient pas.

Note: ESSENTIEL. C'est la même recette partout dans le cours: ici, dans "votre vraie tâche" (partie 6), dans le bonus 11 et sur l'aide-mémoire. Pourquoi commencer simple: les modèles ont besoin de moins en moins d'aide (bonus 11).

---
## Trois astuces pour vos demandes
- Mettez **les informations et les règles importantes à la fin**: la fin d'un long texte est mieux lue que le milieu
- Demandez-lui de **vous poser des questions** avant de commencer: "Pose-moi des questions si besoin."{copy} Il propose souvent des choix à cliquer: c'est très rapide
- Les techniques de prompting (exemples, rôles, étapes, critères): **bonus 11**

Note: À PASSER si le temps manque.
