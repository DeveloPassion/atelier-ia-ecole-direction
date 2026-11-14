# 11 - Bonus, les techniques de prompting

---
## 11. Bonus: les techniques de prompting
Demander mieux, pour obtenir mieux.

---
## La recette d'une bonne demande, en détail
La même recette que dans la partie 4, en six points:

1. **Qui vous êtes**: votre rôle, l'école, la classe, la situation
2. **Ce que vous voulez**: un verbe clair (résume, compare, rédige, classe), et le document à traiter
3. **Pour qui**: des parents, l'équipe, le pouvoir organisateur
4. **Sous quelle forme**: longueur, ton, structure
5. **Un exemple**, si la forme compte
6. **Les règles et les critères**: ce qu'il ne doit pas faire, et comment vous allez juger la réponse

Mettez **les règles importantes à la fin**: la fin d'un long texte est mieux lue que le milieu.

---
## Sans exemple, ou avec quelques exemples
- **Sans exemple**: pour les tâches simples. "Résume ce mail en trois points"{copy}
- **Avec deux ou trois exemples**: quand la forme compte. "Voici deux mots aux parents de l'an passé. Écris celui de la sortie P4 dans le même style"{copy}
- Les exemples valent souvent mieux qu'une longue explication
- Attention: il copie **trop** les exemples. Variez-les, et dites ce qui doit changer

---
## Donner un rôle
- Un rôle **ne rend pas l'IA meilleure**: "Tu es un juriste" ne lui donne pas de compétences en droit
- D'après mon expérience avec les modèles récents: sans rôle, le résultat est **aussi bon**, parfois meilleur
- Un rôle oriente surtout **le vocabulaire, les outils, le niveau et le point de vue**
- Utile pour **une manière de travailler**: "Aborde ce dossier comme un conseiller pédagogique le ferait"{copy}
- Utile aussi **pour relire**: "Lis ce mot comme un parent pressé, sur son téléphone. Qu'est-ce qui n'est pas clair?"{copy}
- Le contexte compte bien plus que le rôle. Et les faits se vérifient toujours

Note: C'est mon expérience, pas une règle. La documentation d'Anthropic conseille encore de donner un rôle dans les instructions: le mieux est de tester avec et sans.

---
## Les modèles ont besoin de moins en moins d'aide
- Chaque nouvelle version **comprend mieux** une demande simple et claire
- Beaucoup d'astuces d'hier (rôles, formules magiques) servent **de moins en moins**, et peuvent même **gêner**: testez avec et sans
- Exemple: "réfléchis étape par étape". Les modèles récents raisonnent déjà seuls: c'est **l'effort**
- Ce qui reste utile: **donner vous-même les étapes**, pour imposer votre méthode. "1. Trouve les dates. 2. Garde celles du primaire. 3. Vérifie chaque date dans le texte. 4. Fais le tableau"{copy}
- Et toujours: **le contexte**, un objectif clair, vos critères, vos exemples si la forme compte
- Commencez **simple**. Ajoutez des consignes seulement quand le résultat ne convient pas

---
## Enchaîner les demandes
<div class="chart strip"><svg viewBox="0 0 960 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma: une grosse tâche en trois petites demandes, avec une vérification entre deux">
<rect x="20" y="30" width="240" height="80" rx="14" fill="#475363"/>
<text x="140" y="64" font-size="18" fill="#fff" font-weight="700" text-anchor="middle">1. Chercher</text>
<text x="140" y="90" font-size="14.5" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">les informations</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(284,54) scale(1.0)" fill="#e5007d"/>
<text x="297" y="134" font-size="13.5" fill="#4ade80" font-weight="700" text-anchor="middle">vous vérifiez</text>
<rect x="360" y="30" width="240" height="80" rx="14" fill="#475363"/>
<text x="480" y="64" font-size="18" fill="#fff" font-weight="700" text-anchor="middle">2. Résumer</text>
<text x="480" y="90" font-size="14.5" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">l'essentiel</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(624,54) scale(1.0)" fill="#e5007d"/>
<text x="637" y="134" font-size="13.5" fill="#4ade80" font-weight="700" text-anchor="middle">vous vérifiez</text>
<rect x="700" y="30" width="240" height="80" rx="14" fill="#e5007d"/>
<text x="820" y="64" font-size="18" fill="#fff" font-weight="700" text-anchor="middle">3. Écrire</text>
<text x="820" y="90" font-size="14.5" fill="#fff" font-weight="400" text-anchor="middle">le texte final</text>
</svg></div>

Une grosse tâche = **plusieurs petites demandes**, chacune avec son résultat.

1. **Chercher, résumer, écrire**: les informations, puis l'essentiel, puis le texte
2. **Produire, critiquer, améliorer**: un brouillon, une critique selon vos critères, une meilleure version
3. **Planifier, faire, vérifier**: un plan validé, le travail, une relecture

Vous **vérifiez entre deux étapes**: une erreur ne passe pas à la suite.

---
## Régler la longueur et le ton
- Longueur: "en un mot"{copy}, "en une phrase"{copy}, "en trois points"{copy}, "en 120 mots maximum"{copy}, "une analyse détaillée"{copy}
- Ton: formel, chaleureux, ferme mais bienveillant, simple
- Niveau: "explique comme à un élève de 10 ans"{copy}, "pour un parent qui lit mal le français"{copy}
- Structure: un tableau, une liste numérotée, un mail prêt à copier

---
## Faire travailler l'IA sur la demande elle-même
- "**Pose-moi des questions** si besoin"{copy}
- "**Améliore ma demande** avant de la faire: qu'est-ce qui manque?"{copy}
- Après un bon résultat: "**Quelle demande** t'aurait permis de faire ça du premier coup?"{copy} Gardez-la
- Pour continuer ailleurs: "Donne-moi **un prompt que je peux passer à un autre agent** pour continuer"{copy}

---
## Juger le résultat avec des critères
- Donnez **vos critères** avant: "Un bon mot aux parents: moins de 120 mots, la date, le prix, l'échéance, un talon-réponse"{copy}
- Puis: "**Évalue ta réponse** selon ces critères. Pour chaque critère: oui ou non, et pourquoi"{copy}
- Pour les faits: "Pour chaque information, cite la phrase exacte et la page"{copy}. Son **niveau de confiance** est un indice, **pas une preuve**
- Un critère écrit une fois sert à chaque demande: il va **dans une skill** (bonus 14)

---
## Ce qui a une vraie valeur: vos processus écrits
- Les techniques de prompting aident. Ce qui fait **la vraie différence**, c'est **décrire vos processus**
- Écrivez **les étapes**, **les critères** d'un bon résultat, **vos préférences** (ton, longueur, forme), **les règles** et **un exemple** réussi
- À chaque utilisation, l'IA suit **votre** façon de faire, sans tout réexpliquer
- Après chaque utilisation: "**Qu'est-ce qu'on améliore dans ce processus?** Mets-le à jour"{copy}. Vous relisez, vous validez
- Le processus **s'améliore à chaque usage**. Il reste utile quand le modèle change: il vous appartient
- **Une skill** dit à l'IA comment suivre ce processus: elle le contient, ou elle le lit (bonus 14)
