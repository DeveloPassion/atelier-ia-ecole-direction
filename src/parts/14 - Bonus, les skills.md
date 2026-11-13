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
## Documenter vos processus
- Ce qui est clair dans votre tête **ne l'est pas pour l'IA**, ni pour un remplaçant
- Un processus écrit se **transmet**, s'**améliore** et se **vérifie**
- L'IA ne fait bien que ce qui est **bien décrit**: un processus flou donne un résultat flou
- Vos processus écrits sont une partie de **votre base de connaissances**

---
## Le processus et la skill: deux choses
- **Le processus**: la description de votre façon de faire. Les étapes, les critères, vos préférences. Écrit pour vous et pour votre équipe
- **La skill**: les instructions pour l'IA. Quand l'utiliser, quoi lire, quoi vérifier, quoi ne jamais faire

Deux façons de les relier:

1. **Tout dans la skill**: la skill contient le processus. Plus simple pour commencer
2. **Séparés**: le processus est une note de votre base, et la skill dit "**lis d'abord** la note du processus, puis suis-la"

En pratique, le résultat est presque le même. Séparés, le processus est **plus facile à modifier**: il n'est pas emmêlé avec les instructions pour l'IA.

---
## Trouver vos skills
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
5. **Transformer en skill**, avec la skill de création de skills: "Transforme ce processus en skill, en respectant la spécification des skills IA: https://agentskills.io/specification.md"{copy}

La spécification sert à ceci: la skill marche avec **d'autres outils d'IA**, sans dépendre d'un fournisseur.

Note: Pourquoi faire d'abord: les petites décisions qu'on prend sans y penser ne sortent pas d'une page blanche, ni d'un entretien. La skill de création de skills s'appelle skill-creator dans l'application. Les quatre premières étapes (faire, écrire, tester, corriger) viennent d'Evelyn Chapman. La cinquième est mon ajout: voir mon article "How I Build AI Skills That Actually Work" (https://www.dsebastien.net/how-i-build-ai-skills-that-actually-work). Un exemple concret pour la salle: plus de 375 skills dans mon système, utilisées chaque jour. Et les skills s'appellent entre elles: la revue du lundi appelle le tri de la circulaire. Avec le système de la phase 2, une phrase suffit: "Crée-moi une skill pour...", ou "skillify" après une conversation réussie.

---
## Les erreurs du premier essai sont utiles
- Au premier test, l'IA **se trompe**. C'est normal, et c'est ce qu'on cherche
- Chaque erreur montre **une chose qui n'est pas écrite**: une étape sautée, une valeur par défaut, un choix que vous faites sans y penser
- Quand l'IA se trompe, on **corrige le texte**. On n'accuse pas l'IA
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
