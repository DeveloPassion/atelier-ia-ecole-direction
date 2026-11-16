# 14 - Bonus, les skills

---
## 14. Bonus: les skills, vos recettes
Une façon de faire, écrite une fois.

---
## Une skill, c'est une recette
- **Le nom**, et **quand l'utiliser**: "Écrire aux parents: pour tout mot aux parents"
- **Les étapes**, dans l'ordre
- **Les règles**: ce qu'il faut toujours faire, ce qu'il ne faut jamais faire
- **Un exemple** de bon résultat
- **Les critères** pour vérifier le résultat
- Claude la charge **seulement quand il en a besoin**: elle ne prend pas de place le reste du temps

---
## Le processus et la skill: deux choses
- **Le processus**: la description de votre façon de faire. Les étapes, les critères, vos préférences. Écrit pour vous et pour votre équipe
- **La skill**: les instructions pour l'IA. Quand l'utiliser, quoi lire, quoi vérifier, quoi ne jamais faire

Deux façons de les relier:

1. **Tout dans la skill**: la skill contient le processus. Plus simple pour commencer
2. **Séparés**: le processus est une note de votre base, et la skill dit "**lis d'abord** la note du processus, puis suis-la"

En pratique, le résultat est presque le même. Séparés, le processus est **plus facile à modifier**: il n'est pas emmêlé avec les instructions pour l'IA.

---
## Identifier les skills à créer pour vous
Cherchez les tâches **répétitives et fréquentes**:

1. Le mot aux parents
2. Le tri d'une circulaire pour votre niveau
3. La revue du lundi
4. Le compte rendu de réunion
5. L'organisation d'une sortie

La question à se poser: **qu'est-ce que je refais chaque semaine**, de la même façon?

---
## Créer une skill en cinq étapes
1. **Faire**: faites la tâche une fois avec Claude, pas à pas
2. **Écrire**: "Écris la marche à suivre de ce qu'on vient de faire: les étapes, les règles, les critères."{copy} Vous relisez
3. **Tester**, dans une **nouvelle conversation**, sans contexte: "Lis ce processus et exécute-le."{copy} La conversation d'origine cache les trous (partie 5)
4. **Corriger** le texte, pas seulement la réponse. Puis retester
5. **Transformer en skill**: "Transforme ce processus en skill, en respectant la spécification des skills IA: https://agentskills.io/specification.md"{copy}

La spécification sert à ceci: la skill marche avec **d'autres outils d'IA**, sans dépendre d'un fournisseur.

Note: Pourquoi faire d'abord: les petites décisions qu'on prend sans y penser ne sortent pas d'une page blanche, ni d'un entretien. La skill de création de skills s'appelle skill-creator dans l'application. Les quatre premières étapes (faire, écrire, tester, corriger) viennent d'Evelyn Chapman. La cinquième est mon ajout: voir mon article "How I Build AI Skills That Actually Work" (https://www.dsebastien.net/how-i-build-ai-skills-that-actually-work). Un exemple concret pour la salle: plus de 375 skills dans mon système, utilisées chaque jour. Et les skills s'appellent entre elles: la revue du lundi appelle le tri de la circulaire. Avec un système comme celui de la démo, une phrase suffit: "Crée-moi une skill pour...", ou "skillify" après une conversation réussie.

---
## Les erreurs du premier essai sont utiles
- Au premier test, l'IA **se trompe**. C'est normal, et c'est ce qu'on cherche
- Chaque erreur montre **une chose qui n'est pas écrite**: une étape sautée, une valeur par défaut, un choix que vous faites sans y penser
- Quand l'IA se trompe, on **corrige le texte**
- D'après mon expérience, **3 à 5 essais** suffisent en général
- Un chemin plus court existe: demander à Claude de **vous poser des questions** sur votre façon de faire. C'est plus rapide, mais il oublie plus de choses

Note: La demande du chemin court: "Aide-moi à créer une skill pour écrire aux parents, en respectant la spécification des skills IA: https://agentskills.io/specification.md. Pose-moi des questions sur ma façon de faire." Elle marche, mais elle oublie plus de choses: on ne pense pas à dire ce qu'on fait sans y penser.

---
## Une skill dans l'application: comment faire
Dans l'application en français, les skills s'appellent des **"compétences"**.

1. **Personnaliser > Compétences**: vos skills, rangées par origine (créées par vous, de votre organisation, partagées avec vous, d'Anthropic)
2. **Activer ou couper** une skill: le bouton sur sa ligne, ou l'interrupteur en haut de sa page
3. L'utiliser: décrivez la tâche, et Claude charge la skill qui convient. Ou tapez **"/"**, et choisissez-la
4. Avant d'activer une skill qu'on vous a donnée: **ouvrez-la et lisez-la**. Personne ne l'a vérifiée pour vous
5. Avec votre base, la skill peut aussi rester **un dossier de votre base de connaissances**: "Utilise la skill ecrire-aux-parents pour la sortie P4."{copy}

Documentation: [Utiliser les compétences dans Claude](https://support.claude.com/fr/articles/12512180) · [Skills overview (en anglais)](https://claude.com/docs/skills/overview)

Note: Lu le 13/11/2026 dans la documentation de Claude. Dans la version en anglais: "Customize > Skills", l'onglet "Your skills" ("Created by you", "From your organization", "Shared with you", "From Anthropic & Partners"), l'onglet "Discover" pour en ajouter, et le bouton "Turn on". Une condition: la création de fichiers et l'exécution de code sont activées ("Settings > Capabilities"; sur Entreprise, c'est un propriétaire de l'organisation qui l'active). Pour ajouter une skill à soi: un fichier ZIP qui contient le dossier de la skill, avec son fichier SKILL.md dedans. La skill de création de skills (skill-creator) est une skill d'Anthropic: on l'active dans cette liste, puis on demande à Claude de créer ou d'évaluer une skill. Les skills d'Anthropic qui créent des fichiers Excel, Word, PowerPoint et PDF s'activent seules quand il le faut. Pour le point 5, Claude lit simplement le fichier SKILL.md du dossier de travail, comme n'importe quel fichier: c'est la voie de la démo de la partie 7, et celle qui garde vos skills chez vous.

---
## Les commandes
Tapez **"/"** dans la zone de saisie: la liste de vos **skills** et de vos commandes s'ouvre. Quelques lettres suffisent pour filtrer.

| Vous tapez | Ce que Claude fait |
|---|---|
| **/ecrire-aux-parents** sortie P4, le 26 novembre | Le mot aux parents, dans le ton de l'école, avec le talon-réponse |
| **/trier-une-circulaire**, avec le PDF joint | Le tableau des actions pour votre niveau, avec les dates |
| **/compte-rendu**, avec vos notes brutes | Le compte rendu de la réunion, toujours dans la même forme |
| **/skill-creator** | Il vous aide à créer une skill (skill d'Anthropic, à activer) |
| **/nom-du-plugin:commande** | Une commande ajoutée par un plugin |

- Les trois premières sont **des exemples**: elles existent une fois que vous les avez créées
- Une commande, c'est **une ligne au lieu de tout réexpliquer**

Note: Montrer le menu "/" en direct. Si aucune skill n'est installée sur leur compte, le dire: le menu se remplit avec leurs skills. Lu le 15/11/2026 dans la documentation de Claude (page "Plugins", "Use a plugin"): dans le chat, on tape "/" dans la zone de saisie, et le menu liste les skills, avec le nom du plugin d'où chacune vient; les commandes d'un plugin sont dans le même menu; on tape le nom pour filtrer. Dans Cowork: "/nom-du-plugin:commande" lance une commande, ou on décrit la tâche et Claude charge la skill qui convient. Dans le chat, une commande de plugin se charge comme une skill. La documentation ne donne pas de liste de commandes intégrées à l'application: les commandes comme "/clear" ou "/compact" sont celles de Claude Code, l'outil des développeurs. À vérifier sur leur PC: que "skill-creator" apparaît bien dans le menu "/" une fois activée.

---
## Skills et plugins tout faits: d'où viennent-ils?
Un **plugin** est un paquet: des skills, des connecteurs et des commandes, ajoutés en une fois (**Personnaliser > Plugins**).

| D'où ça vient | Qui l'a vérifié |
|---|---|
| **De vous** | Vous: vous savez ce qu'il y a dedans |
| **D'Anthropic**, ou de son annuaire de plugins | Anthropic: un contrôle de sécurité à chaque version |
| **De l'école** | Le propriétaire de l'organisation, qui l'a choisi |
| **D'Internet**: un fichier ZIP, une adresse | **Personne** |

- Une skill, ce sont **des instructions que Claude suit**. Un plugin peut aussi **lancer des commandes sur votre PC**
- Trouvé sur Internet: **vous ne l'ajoutez pas vous-même**. Montrez-le à l'admin, ou écrivez votre propre recette

Documentation: [Plugins (en anglais)](https://claude.com/docs/plugins/overview) · [Claude Marketplace (en anglais)](https://claude.com/marketplace)

Note: Lu le 14/11/2026 dans la documentation de Claude. Le lien avec la démo 4: une skill ou un plugin d'une source inconnue, c'est une instruction cachée que l'on installe soi-même. Ce que dit la documentation: Anthropic contrôle les plugins de son annuaire (validation automatique et contrôle de sécurité à chaque version, et une personne relit chaque nouvelle fiche). Ce contrôle ne couvre pas un plugin ajouté depuis une adresse ou envoyé en fichier: "seulement depuis des sources de confiance". Une skill partagée par quelqu'un, ou envoyée en fichier, n'est pas vérifiée par Anthropic non plus: l'ouvrir et la lire avant de l'activer (slide précédente). Un plugin peut aussi contenir des agents. Dans la version en anglais: "Customize > Plugins", avec "Discover", "Add > Add marketplace" et "Add > Upload plugin"; le nom dans l'application en français est à vérifier. Deux choses portent le nom "marketplace". Dans l'application, une "marketplace" de plugins est un dépôt de code qui contient des plugins. "Claude Marketplace" (claude.com/marketplace) est la vitrine d'Anthropic: des connecteurs et des plugins, des agents et des produits de partenaires, et des sociétés de service. Elle ne liste pas de skills. Sur Entreprise, c'est un propriétaire de l'organisation qui choisit les sources visibles et qui décide si les membres peuvent en ajouter (bonus 18).

---
## Une skill bien construite
Toujours **selon la spécification** (https://agentskills.io/specification.md):

- **Un dossier** au nom de la skill, en minuscules et avec des tirets: `ecrire-aux-parents`
- Dedans, **un fichier SKILL.md**: en haut, le **nom** et une **description** (ce qu'elle fait, et quand l'utiliser)
- Puis **les instructions**: les étapes, les règles, un exemple, les critères
- Si besoin, des dossiers à côté: des documents de référence, des modèles
- Court: **moins de 500 lignes**. Le détail va dans les documents de référence

---
## Exemple: écrire aux parents
```
Quand: pour tout mot aux parents.
Étapes: 1. Vérifie la date, le lieu, le prix et l'échéance.
2. Écris 120 mots maximum, vouvoiement, ton chaleureux et court.
3. Ajoute un talon-réponse si une réponse est attendue.
4. Signe avec mon prénom et ma fonction.
Règles: n'envoie jamais rien. Aucune donnée d'élève.
Critères: la date, le prix et l'échéance sont exacts et visibles.
```

---
## Démo: créer une skill ensemble
Notre première recette: **écrire aux parents**. Le processus est déjà écrit dans la base: la skill **le lit**.

> Aide-moi à créer une skill pour écrire les mots aux parents de mon école, en respectant la spécification des skills IA: https://agentskills.io/specification.md. La skill ne recopie pas mon processus: elle lit d'abord la note "Écrire aux parents (Processus)" de ma base de connaissances, puis elle la suit. Enregistre la skill dans le dossier "Skills" de ma base de connaissances.

Puis on la teste: "Écris le mot aux parents pour la sortie P4 du 26 novembre."{copy}

Ensuite, on change **une ligne du processus**, et on relance: le mot change, sans toucher à la skill.

Note: DÉMO SKILL (5 min), à l'écran, Claude ouvert sur une copie du dossier "Direction Saint-Exemple" (le système de démo). 1) Coller la demande. 2) Montrer le résultat: un dossier "ecrire-aux-parents" avec un fichier SKILL.md (name, description, puis l'instruction de lire la note du processus). 3) Tester avec la sortie P4, dans une nouvelle conversation. 4) Ouvrir la note "Écrire aux parents (Processus)" (dossier Actions/Processus), changer "150 mots maximum" en "80 mots maximum", et enregistrer. 5) Nouvelle conversation, même demande: le mot est plus court. Message: on a changé le processus, pas la skill (bonus 14, "Le processus et la skill: deux choses"). Si quelque chose ne va pas: corriger le texte, pas la réponse. La skill vit dans le dossier de travail (la base de connaissances): rien à installer dans l'application. Pour s'en servir, Claude ouvert sur ce dossier: "Utilise la skill ecrire-aux-parents pour...". La spécification vient de agentskills.io, un format ouvert que d'autres outils IA lisent aussi. Cette démo passe en deuxième séance si le temps manque: elle demande cinq minutes.

---
## Avec votre système, une phrase suffit
- Un système comme celui de la démo **connaît déjà la spécification** et l'endroit où ranger vos skills
- Vous dites simplement: **"Crée-moi une skill pour..."**
- Ou, après une conversation réussie: **"skillify"**. Il transforme ce que vous venez de faire en skill
- Vos recettes s'accumulent dans **votre base de connaissances**: elles vous appartiennent

Note: 

---
## Une skill vit, le processus aussi
- Un résultat ne va pas? **Corrigez la recette**, pour que l'erreur ne revienne pas
- Les deux s'améliorent avec le temps: **le processus** (votre façon de faire) et **la skill** (les instructions pour l'IA)
- Après une utilisation: "**Qu'est-ce qu'on améliore**, dans le processus ou dans la skill? Mets à jour"{copy}. Vous relisez, vous validez
- Un changement peut **casser** une skill qui marchait: gardez **la version d'avant** (une copie datée, dans votre base de connaissances), et retestez après chaque changement
- Relisez vos skills **une fois par trimestre**
- Une bonne skill fait gagner du temps **à chaque fois**, et à toute l'équipe si vous la partagez

---
## Commencez par une seule skill
- **Une seule** skill cette semaine: celle de la tâche que vous refaites le plus
- Utilisez-la plusieurs fois, et corrigez-la
- Puis une autre, la semaine suivante
- Une skill est **un outil**. Vingt skills sont **un système**
