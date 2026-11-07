# 7 - Un système qui vous connaît

---
## 7. Un système qui vous connaît
Et qui vous appartient.

---
## Le constat
- La limite n'est plus l'IA
- La limite, c'est **ce qu'elle sait de vous**
- Chaque conversation **repart de zéro**, ou presque

---
## Décharger son cerveau
- Tout ce que vous gardez en tête **vous pèse**: le car à confirmer, le parent à rappeler, le dossier à corriger
- Écrit dans un endroit fiable, ça ne vous pèse plus: **votre tête se libère**
- C'est votre **second cerveau**, digital
- **Double gain**: vous vous déchargez aujourd'hui, et chaque note rend l'IA plus utile demain

- Attention au revers: l'IA produit vite, et on peut **vite en faire trop**. Vous faites travailler l'IA, ou est-ce l'IA qui vous fait travailler?

Note: Message clé: on ne note pas "pour l'IA". On note d'abord pour soi, pour se décharger. L'IA en profite en plus. Le plus simple pour commencer: tout noter dans le journal du jour, et ranger plus tard.

---
## L'habitude de noter
Les paroles s'envolent, les écrits restent.

- Noter **tout de suite**: une idée, une décision, un appel, une chose à faire
- Noter **ce qui compte**, pas tout
- Noter aussi **le contexte**: pourquoi, avec qui, et quelle est la suite
- Relire au moins **une fois par semaine**

Note: Exemple: un parent appelle pour la sortie P4. On note tout de suite ce qui est dit, ce qui est décidé et la suite. Les gens savent qu'on reviendra vers eux, parce que c'est écrit. Sans cette habitude, le reste ne marche pas: on ne peut ni ranger, ni relier, ni donner à l'IA ce qu'on n'a pas noté.

---
## Le journal du jour
Le plus simple pour commencer: **une seule note par jour**.

- Tout y va: les appels, les idées, les décisions, les choses à faire
- **Rien à décider** sur le moment: pas de titre, pas de dossier
- Une fois par semaine, **on range**: une tâche, un projet, une note sur une personne
- Pour l'IA, c'est **une mine**: "Qu'est-ce que j'ai promis cette semaine?", "Qu'est-ce qui est resté en suspens?"

Note: Dans la démo Saint-Exemple, montrer la note du jour du 09/11. Avant la phase 2, un seul document Word "Journal" dans le OneDrive suffit, avec une date en titre pour chaque jour.

---
## Deux couches
- En bas: un système qui marche pour vous, **même sans IA**. Une structure claire, des types de notes, un journal, des projets et des tâches
- Au-dessus: une IA qui **comprend tout ce système**, et qui travaille avec vous
- L'IA ne vaut que ce que vaut **la couche du dessous**
- Ce sont des fichiers texte, chez vous: ils marchent avec **n'importe quelle IA**. Obsidian sert à les lire et à les écrire

```mermaid
flowchart TB
  IA[L'IA: elle comprend le système et agit avec vous]
  S[Votre système: structure, types de notes, journal, projets, tâches]
  IA --> S
```

---
## Ce qu'un système sait de vous
1. Qui vous êtes: votre rôle, votre école, vos valeurs, votre ton
2. Vos objectifs et vos projets: les priorités de l'année, les projets en cours, ce que vous attendez des autres
3. Votre environnement: les personnes, les outils (mAGEordome, GEDI-PRO, RAVEL, OneDrive, IT School), le calendrier scolaire
4. Vos processus: comment vous organisez une sortie, une inscription, la revue du lundi

---
## Une note, un type, une place
- Chaque note a **un seul type**: une sortie, une réunion, une personne, un projet, une tâche
- Le type dit où la note est rangée: les sorties avec les sorties, les réunions avec les réunions
- Le type dit aussi ce qu'elle contient: une sortie a une date, une classe, un prix, "payé" oui ou non
- Une note peut être liée à beaucoup de choses (la classe, le budget, l'institutrice), mais elle n'a **qu'une place**
- La liste "toutes les sorties de P4" **se fait toute seule**: pas besoin d'un dossier par classe

Note: Lien avec la démo 3: on a rangé des fichiers existants par classe. Pour des documents, c'est très bien, et la plupart ne doivent plus bouger. Dans le système, chaque sortie est une note de type "sortie" avec "classe: P4". On n'a plus à choisir un dossier: la liste par classe, par mois ou "pas encore payé" se fait toute seule. Et l'IA sait où chercher et ce qu'elle va trouver.

---
## Ce que l'IA lit d'abord
**La note de projet**. En une page:

1. Ce que c'est, et pourquoi
2. Où on en est: un statut (actif, en pause, terminé)
3. La prochaine action: les tâches, avec leurs dates
4. Les décisions prises
5. Les personnes et les documents

Pour l'IA, ce sont des informations à lire, **pas un texte à deviner**.

---
## Démo: en vrac ou organisé
Les mêmes faits, dans deux dossiers:

- **En vrac**: des fichiers texte, comme on les note souvent
- **Organisé**: des notes de projet, avec un statut et des tâches datées
- La même question aux deux: "Liste mes projets en cours, avec leur statut et leur prochaine action. Lequel est bloqué?"

Note: DÉMO EN VRAC OU ORGANISÉ (5 min), à l'écran. Dézipper avant la séance "Système Direction Saint-Exemple en vrac (démo).zip" et "Système Direction Saint-Exemple - notes seules (démo).zip".
1. Ouvrir Claude sur le dossier en vrac. Poser la question.
2. Ouvrir Claude sur le dossier organisé. Poser la même question.
3. Montrer dans la réponse du vrac la phrase où Claude dit qu'il a déduit les statuts lui-même, et les tâches qu'il compte comme des projets (les bancs, la photocopieuse).
4. Poser la question une deuxième fois au vrac: la liste change (au test du 05/11: 5 "projets", puis 6). L'organisé donne trois projets en cours et un terminé, avec les statuts lus dans les notes.
Message: en vrac, l'IA devine bien, mais elle devine. Organisé, elle sait. Ne pas promettre qu'elle se trompe sur le vrac: avec un bon modèle, elle trouve souvent le bon projet bloqué.
Corrigé: Sortie P4 (actif; mot aux parents avant le 12/11, puis car avant le 13/11). Plan de pilotage (actif; formations avant le 15/12). Classes de neige P5 (en pause, donc bloqué: 690 euros dépassent le plafond de 485 euros pour les six années; on attend la décision du PO, relance le 16/11). Pas en cours: les photos de classe (terminé le 23/10).
Pièges du vrac: "c'est réglé" pour les photos caché dans le journal; "réserver le photographe" encore dans "à faire.txt"; quatre projets de l'an passé listés "en cours" dans "Projets 2025-2026.txt"; le mot aux parents en double; les bancs sont une relance, pas un projet.
Le corrigé complet est la question 6 de "DEMO - À demander.txt".

---
## Avant et après
La sortie de P4 au musée, le 26 novembre.

- Sans système: **dix lignes de contexte** à chaque demande, et des oublis
- Avec un système: "Prépare la sortie P4 du 26 novembre"
- Il connaît la classe, l'institutrice, le budget, le plafond des frais, le modèle de mot aux parents
- Il ajoute l'encodage sur IT School à vos tâches

---
## Quatre façons de travailler
| | Le chat seul | Un projet Claude | La mémoire de Claude | Votre base |
|---|---|---|---|---|
| Ce qu'il sait de vous | Rien | Ce que vous y avez mis | Quelques éléments, peu visibles | **Tout ce qui compte, rangé** |
| Où c'est gardé | Chez Anthropic | Chez Anthropic | Chez Anthropic | **Chez vous** |
| Si vous changez d'IA | Rien à perdre | Tout à refaire | Perdu | **Rien à refaire** |
| Partagé avec l'équipe | Non | Un peu | Non | **Oui, si vous voulez** |

---
## Souverain: ce que ça veut dire
1. **Ne pas dépendre** de Claude seul, ni de ses projets, ni de sa mémoire
2. Une base de connaissances **à vous**: des fichiers texte, sur votre PC ou votre OneDrive, lisibles sans aucun outil
3. **Personnelle et partagée**: chaque direction a la sienne, et une partie commune peut servir à toute l'école
4. **Libre de changer de fournisseur**: la même base sert avec Claude aujourd'hui, et avec un autre demain
5. **Vous décidez** ce que l'IA voit, dossier par dossier

---
## Ce qu'il faut savoir
- Le modèle reste un **service externe**
- Chaque demande passe chez le fournisseur choisi
- Ce qui ne dépend plus de lui: vos connaissances, votre organisation, vos processus
- Si demain un autre modèle est meilleur, ou européen, ou local, vous changez **sans rien perdre**

---
## Louer ou posséder
- Les projets Claude et la mémoire de Claude: **un meublé loué**. Pratique, mais rien n'est à vous
- Votre base de connaissances: **une maison à vous**. Vous la meublez une fois, et vous la gardez

---
## Démo: Direction Saint-Exemple
Un système construit sur AI Kit for Obsidian, avec une direction fictive.

- Les mêmes demandes que tout à l'heure, **en une ligne**
- Puis la même question dans un chat vide, pour comparer

Note: DÉMO SYSTÈME (5 min), à l'écran. Ouvrir le dossier "Système Direction Saint-Exemple - notes seules (démo)" (dézippé avant la séance) dans Obsidian, et Claude sur ce dossier. Les demandes et les réponses attendues sont dans "DEMO - À demander.txt", à la racine du système. Pour chaque demande, montrer la réponse, puis poser la même question dans un chat vide. Les cinq demandes: 1) "Prépare la sortie P4 du 26 novembre." 2) "Fais ma revue du lundi." 3) "Écris aux parents de P4 que le paiement est attendu avant le 19/11." 4) "Qu'est-ce que j'attends des autres, et qui dois-je relancer cette semaine?" 5) "Quelles actions de la circulaire 9847 touchent mes projets?" (joindre le PDF). En 5 minutes: faire 1 et 2. Les autres si le temps le permet. Le fichier finit par un tableau qui compare le chat, un projet Claude, la mémoire de Claude et ce système. Si le temps le permet, 2 minutes dans mon propre système: le genre de demandes que je lui fais chaque jour.

---
## L'IA qui prend l'initiative
- Aujourd'hui: vous allez vers l'IA, et vous lui réexpliquez tout
- Demain: l'IA connaît vos projets, vos tâches et vos priorités, et **elle propose**
- Exemple, la revue du lundi: "Deux dossiers GEDI-PRO à corriger, la déclaration des classes de neige avant le 23 janvier, la sortie P4 pas encore payée. Je prépare le rappel aux parents?"
- **Elle propose, vous décidez**

---
## Le cercle vertueux
```mermaid
flowchart LR
  K[Vos connaissances] --> C[Le contexte de l'IA]
  C --> R[De meilleures réponses]
  R --> K
```

Vos notes deviennent le contexte de l'IA. Ses réponses deviennent de nouvelles notes.

---
## Le chemin
1. **La clarté**: votre rôle, vos priorités, vos objectifs (la fiche de contexte)
2. **Le système**: un endroit fiable, à côté de votre OneDrive
3. **L'habitude de noter**: d'abord le journal du jour
4. **Les projets et les tâches**
5. Le reste, une étape à la fois

Les objectifs viennent d'en haut. Ce que vous notez chaque jour vient d'en bas. Les deux se rejoignent pendant les revues.

La phase 2: un système de base pour chacun, construit ensemble, à ce rythme.

Note: D'abord une carte du dossier OneDrive, sans rien déplacer. La nouvelle information entre dans le système, les anciens dossiers suivent quand on travaille dessus.
