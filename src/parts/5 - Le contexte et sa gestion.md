# 5 - Le contexte et sa gestion

---
## 5. Le contexte
Le contexte, c'est **tout ce que Claude voit** au moment de répondre.

- Vos instructions et votre prompt
- La conversation jusqu'ici
- Les documents joints
- Les résultats des outils (une page web, un fichier lu)
- Le reste, **il ne le connaît pas**

---
## La session
- Une session, c'est une conversation
- À chaque message, Claude **relit toute la conversation** depuis le début
- Entre deux conversations, **il ne se souvient de rien**
- Sauf ce qui est dans un projet Claude ou dans sa mémoire

---
## Plusieurs conversations en parallèle
- Vous pouvez donner **plusieurs tâches en même temps**: une conversation par tâche
- Par exemple: le tableau des sorties dans l'une, la circulaire dans une autre, un mail aux parents dans une troisième
- Chaque conversation **avance à son rythme**, et vous passez de l'une à l'autre
- Vous relisez et vous corrigez quand une tâche est prête

Note: Le montrer en direct: lancer une tâche longue (par exemple ranger le dossier), puis ouvrir une nouvelle conversation pour un mail court pendant que la première travaille. C'est aussi une bonne raison de faire des conversations courtes: une tâche, une conversation.

---
## La fenêtre de contexte
- C'est la quantité maximum de texte que Claude lit en une fois
- Elle est grande: environ un million de tokens, quelques gros livres
- Mais elle n'est **pas infinie**
- Et plus elle est pleine, **moins il fait attention** à chaque détail

---
## Le cache
- Claude garde le début de la conversation pendant quelques minutes
- Il ne relit donc pas tout à chaque message: c'est plus rapide et moins cher
- Après une longue pause, il doit tout relire
- Conséquence: une très longue conversation reprise le lendemain **coûte plus et répond moins bien**

*À lire seul*

---
## Le coût d'une demande
- L'IA se paie en **tokens**: tout ce que Claude lit, plus tout ce qu'il écrit
- À chaque message, il **relit toute la conversation**: plus elle est longue, plus chaque message coûte
- Les documents joints et les pages web lues comptent aussi
- Un gros modèle (Opus) et un effort haut coûtent plus qu'un modèle plus léger (Sonnet) et un effort bas

Note: Ordre de grandeur pour la salle, sans chiffres précis: une question courte coûte très peu; une circulaire de 20 pages lue en effort haut coûte bien plus. Le message: ce n'est pas cher pour une vraie tâche, mais les longues conversations qui traînent coûtent sans rien rapporter.

---
## Budget et limites
- Avec Claude Entreprise, le collège paie un abonnement, et aussi **selon les tokens utilisés**
- Il peut y avoir **une limite par personne** ou un budget pour le collège: c'est l'admin qui les règle
- Si une limite est atteinte, Claude le dit: attendre, ou demander à l'admin
- Les bons réflexes: **une conversation par sujet**, joindre seulement ce qui sert, Sonnet pour le simple, l'effort haut seulement quand il le faut

Note: À vérifier avec l'admin avant la séance: le contrat exact (abonnement seul, ou abonnement plus l'usage), les limites par personne, et où chacun voit sa consommation dans l'application. Si le contrat est un forfait sans usage, adapter la première ligne: "les tokens comptent dans votre quota".
---
## L'entonnoir du contexte
```mermaid
flowchart TD
  A[Pas de contexte] --> A2[Réponse générique]
  B[Trop peu] --> B2[Réponse vague]
  C[Le bon contexte] --> C2[Réponse précise et utile]
  D[Trop de contexte] --> D2[Confusion et erreurs]
```

---
## Les types de contexte
1. Les instructions: ce que vous voulez, comment
2. Les exemples: un mot aux parents réussi
3. Les connaissances: le règlement, le calendrier
4. La mémoire: ce que Claude retient de vous
5. Les outils: ce que Claude peut aller chercher

*À lire seul*

---
## Cinq niveaux
1. Rien: on pose une question
2. Du contexte dans la demande: mieux, mais on se répète
3. La mémoire de Claude: il retient quelques éléments, de façon peu fiable
4. Les projets Claude: des instructions et des documents permanents
5. Une base de connaissances **à vous**, que l'IA utilise

```mermaid
flowchart LR
  N1[1. Rien] --> N2[2. Dans la demande] --> N3[3. Mémoire] --> N4[4. Projets Claude] --> N5[5. Votre base]
```

---
## Les projets Claude
- Un projet Claude garde des instructions et des documents **pour toutes ses conversations**
- Exemple: un projet Claude "Direction primaire" avec le ton de l'école, le règlement, le calendrier
- Vous ne réexpliquez plus rien: chaque nouvelle conversation part de là
- Un projet Claude **par grand sujet**, pas un pour tout

---
## La limite des niveaux 3 et 4
- La mémoire et les projets Claude **vivent chez Anthropic**
- Ils ne passent pas dans un autre outil
- On voit mal ce qu'ils contiennent
- Chacun refait le sien, rien n'est partagé
- C'est un **contexte loué**

---
## Plus n'est pas toujours mieux
- **Le contexte est fini**
- Chaque document ajouté rapporte un peu moins que le précédent
- Un document inutile peut même faire baisser la qualité
- Donnez **ce qui sert à la tâche**, pas tout ce que vous avez

---
## Une longue conversation se dégrade
- Claude se perd et mélange les sujets
- Il oublie des consignes du début
- Il **invente davantage**: les hallucinations augmentent
- Chaque message coûte plus, parce qu'il relit tout
- Ce n'est pas vous: c'est **la limite du contexte**

---
## Des conversations courtes, sur un seul point
**Évitez à tout prix les conversations longues et "fourre-tout".**

- Une conversation = **un point précis**: un mail, un tableau, une circulaire
- Dévier un peu, c'est permis. Changer de sujet: **nouvelle conversation**
- Besoin de garder la suite? Demandez **un résumé**, et collez-le dans une nouvelle conversation
- Mieux vaut **dix conversations courtes** qu'une seule longue

Note: C'est la règle la plus importante de la partie: la dire avec force. Les longues conversations sont la cause la plus fréquente des mauvaises réponses et des inventions.

---
## La compaction
- Quand une conversation devient trop longue, Claude **résume le début**
- Il continue à partir de ce résumé
- Les détails du début **peuvent se perdre**
- Si une consigne compte, redites-la, ou mettez-la dans votre fiche de contexte

Note: La compaction existe aussi dans l'application Claude (Claude Desktop). Montrer une longue conversation déjà compactée, préparée avant la séance. Image utile: un PV de réunion garde les décisions et perd les détails.

---
## Quatre règles pratiques
1. **Une conversation = un sujet**, et une conversation courte
2. Nouvelle conversation quand vous changez de sujet, ou quand les réponses se dégradent
3. Ce qui doit durer va **dans un fichier à vous** (la fiche de contexte) et dans un projet Claude
4. Pour garder la suite d'un travail, **demandez un résumé**, et repartez de ce résumé dans une nouvelle conversation

---
## L'idée centrale
**Résultat = modèle × contexte**

- Le modèle est le même pour vous trois: Claude Entreprise
- Le contexte, c'est vous qui le donnez
- C'est **le seul facteur que vous contrôlez**

Pour un système qui vous connaît: il choisit le bon contexte pour chaque demande, au lieu de tout mettre. Et ce contexte est à vous.

---
## Pause
10 minutes

Note: Pendant la pause, ouvrir les fichiers des démos et le dossier "Plan B - résultats attendus", au cas où.
