# 2 - Prise en main de Claude

---
## 2. Prise en main
Claude est l'IA de la société Anthropic. Le collège l'utilise en abonnement Entreprise.

- D'autres IA existent: GPT (ChatGPT), Gemini, Mistral, DeepSeek, Qwen, ...
- Elles fonctionnent toutes de la même façon: **ce que vous apprenez ici vaut aussi pour elles**

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

Note: TOUR DE L'APPLICATION (4 min), chacun sur son PC. Suivre les numéros du dessin, et montrer chaque zone en une phrase: 1) les conversations et les projets, 2) la conversation, 3) la zone de saisie, pour écrire, dicter, joindre un fichier, avec ses réglages (slide suivante), 4) les artefacts: un document, une présentation, un tableau, 5) les paramètres: les connecteurs, les skills, la mémoire. Le dessin est un plan: l'écran réel change un peu selon la version. À dire pour la zone 4: un artefact reste dans l'application, chez Anthropic. C'est très bien pour un essai. Pour ce qui doit durer, on demande un fichier dans le dossier de travail (partie 6). Montrer le micro de la zone de saisie et dicter une demande en direct: c'est souvent ce qui surprend le plus. Ouvrir les paramètres et montrer Connecteurs et Skills sans rien changer. Montrer aussi l'extension Claude in Chrome dans Chrome.

---
## Les réglages sous la zone de saisie
- **Le dossier de travail**: le dossier que Claude peut lire et modifier. L'idéal: **toujours le dossier de votre base de connaissances** (partie 7). Pour un essai, une copie. Jamais tout votre OneDrive
- **Le modèle** et **l'effort**: voir les slides suivantes
- **Le mode rapide**: des réponses plus rapides, qui consomment plus de budget
- **Le mode de travail**: comment Claude vous demande la permission avant d'agir

Note: Montrer chaque réglage en direct, chacun sur son PC. Les noms exacts peuvent changer selon la version et la langue de l'application: vérifier avant la séance.

---
## Les modes de travail
- **Manuel**: Claude demande votre accord **avant chaque action**. Le plus sûr pour commencer
- **Accepter les modifications**: il modifie les fichiers du dossier **sans demander à chaque fois**
- **Plan**: il lit, réfléchit et **propose un plan**, sans rien changer. Vous validez, puis il travaille
- **Auto**: il avance seul, et ne demande que pour **les actions risquées**

Mon conseil: **Plan** pour une grosse tâche, **Manuel** au début, et **Auto** seulement sur une copie.

Note: Lien avec la partie 8: plus le mode est automatique, plus il faut un dossier de travail limité et une copie des fichiers. Pour la démo du rangement du dossier (partie 6), utiliser le mode Plan: Claude montre son plan, vous dites oui, puis il range.

---
## Claude s'adapte à la tâche
- Vous écrivez ce que vous voulez. **Claude choisit**: répondre vite, ou faire un travail plus long
- Vous pouvez l'arrêter, le corriger, ou changer l'effort à tout moment
- Il peut continuer une tâche longue pendant que vous faites autre chose

---
## Les commandes
- Tapez **"/"** dans la zone de saisie
- Une liste s'ouvre: les skills et les commandes disponibles
- Choisissez-en une **au lieu de tout réexpliquer**
- Exemple: une skill "mot aux parents" écrit toujours dans le ton de l'école

Note: Montrer le menu "/" en direct. Si aucune skill n'est installée sur leur compte, le dire et revenir aux skills dans la partie 4.

---
## Les modèles
| Modèle | Pour quoi |
|---|---|
| **Sonnet 5.5** | Les tâches simples: un mail, une reformulation, un résumé court |
| **Opus 5.5** | Le gros du travail: une circulaire, un tableau, un dossier |
| Haiku | Rapide et léger |
| Fable | Le plus puissant, mais **très coûteux**, et vos données sont **gardées au moins 30 jours** (voir la partie 8) |

Le modèle est **le premier levier de coût**: Opus coûte 2 fois plus que Sonnet, et Fable 4 fois plus (bonus 18).

**Ça bouge très vite**: de nouveaux modèles sortent **toutes les semaines**. Cette recommandation date de novembre 2026.

Note: Sur Entreprise, l'usage se paie au volume (bonus 18). Vérifier avant la séance que l'admin autorise Sonnet 5.5 et Opus 5.5. Fable 5, 5.1 et 5.2 (la version actuelle, ajoutée à la liste le 09/11/2026) sont des "Covered Models" chez Anthropic: conservation des données d'au moins 30 jours, examinées par des systèmes de sécurité automatiques, et pas de zéro conservation (ZDR) pour les organisations Claude Enterprise (centre d'aide d'Anthropic, article "Covered Models", vérifié le 12/11/2026). L'article parle d'une option ZDR limitée dans le temps pour certains clients: à voir avec Anthropic, ne pas compter dessus. Conseil: Fable seulement pour une tâche qui le justifie, et jamais avec des données personnelles.

---
## Le niveau d'effort
L'effort dit **combien de travail** Claude met dans une tâche.

- **Effort bas**: rapide. Une première version, à corriger ensemble
- **Effort haut**: plus long. Il vérifie, il teste, il décide plus de choses seul
- Sur une grosse tâche, Claude peut **travailler des heures sans s'arrêter**: il lit, essaie, vérifie et recommence, pendant que vous faites autre chose
- Plus d'effort prend plus de temps et plus de **tokens**, donc plus de budget (voir la partie 5)
- On donne 1 heure pour une tâche: on rend une première version. On donne 12 heures: on vérifie tout. Claude lit l'effort de la même façon

Note: Analogie de Thariq Shihipar (Anthropic), article "Spending your effort", 2026-09-25. Dans ses tests, une même demande a pris 1 minute et demie en effort bas, et plus d'une heure en effort maximum.

---
## Quel effort choisir
- Effort bas: brainstorming, brouillon, petite correction
- Effort moyen: le travail courant
- Effort haut: **ce qui doit être juste** (les dates d'une circulaire, les chiffres d'un tableau)
- Moins vous précisez, plus Claude décide à votre place. **Une demande précise** est le levier le moins cher

Pour un système qui vous connaît: le modèle et l'effort comptent moins quand Claude sait déjà ce que vous voulez.
