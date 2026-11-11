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
## Créer une skill avec Claude
1. Utilisez **la skill de création de skills** (skill-creator): "Aide-moi à créer une skill pour écrire aux parents, en respectant la spécification des skills IA: https://agentskills.io/specification.md. Pose-moi des questions sur ma façon de faire"
2. Donnez un ou deux **exemples réussis**
3. **Testez** la skill sur un vrai cas
4. **Corrigez la skill**, pas seulement la réponse
5. Gardez une copie du texte **dans votre base de connaissances**: elle vous appartient

Avec le système de la phase 2: "Crée-moi une skill pour...", ou "skillify" après une conversation réussie.

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
- Après une utilisation: "**Qu'est-ce qu'on améliore**, dans le processus ou dans la skill? Mets à jour". Vous relisez, vous validez
- Relisez vos skills **une fois par trimestre**
- Une bonne skill fait gagner du temps **à chaque fois**, et à toute l'équipe si vous la partagez
