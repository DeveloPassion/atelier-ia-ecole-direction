# 2 - Prise en main de Claude

---
## 2. Prise en main
Claude est l'IA de la société Anthropic. Le collège l'utilise en abonnement Entreprise.

- D'autres IA existent: GPT (ChatGPT), Gemini, Mistral, DeepSeek, Qwen, ...
- Elles fonctionnent toutes de la même façon: **ce que vous apprenez ici vaut aussi pour elles**

---
## L'application Claude
- À gauche: vos conversations et vos projets
- Au centre: la conversation
- En bas: la zone de saisie, pour écrire ou **dicter** (le micro), joindre un fichier, et ses **réglages** (slide suivante)
- Mon conseil: **dictez**. On parle bien plus vite qu'on écrit, et on donne naturellement plus de contexte
- À droite: **les artefacts**, ce que Claude crée pour vous (document, présentation, tableau)
- Dans les paramètres: les connecteurs, les skills, la mémoire

Note: TOUR DE L'APPLICATION (4 min), chacun sur son PC. Montrer chaque zone en une phrase. Montrer le micro de la zone de saisie et dicter une demande en direct: c'est souvent ce qui surprend le plus. Ouvrir les paramètres et montrer Connecteurs et Skills sans rien changer. Montrer aussi l'extension Claude in Chrome dans Chrome.

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
