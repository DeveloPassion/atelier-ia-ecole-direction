# 18 - Bonus, gérer les coûts

---
## 18. Bonus: gérer les coûts
Suivre les dépenses, mettre des limites, éviter les mauvaises surprises.

Note: Tout ce bonus vient du centre d'aide d'Anthropic, lu le 12/11/2026 (articles "Claude Enterprise plan overview", "Usage-based Enterprise plans", "Claude Enterprise consumption guide", "Usage analytics for Enterprise plans", "Manage model access for your organization"). La documentation est en anglais: les noms des menus peuvent être différents dans l'application en français. À revérifier dans la console avec l'admin du collège avant d'en parler: le contrat du collège peut être différent.

---
## Comment Claude Entreprise se paie
- **Un siège par personne**: il donne l'accès. Il n'inclut pas d'usage
- **L'usage en plus**, au volume: chaque token lu ou écrit, dans le chat, dans Cowork, dans Claude in Chrome
- Le prix dépend **du modèle et de la tâche**
- Les anciens contrats sont différents: un forfait par siège, avec un quota d'usage inclus
- Donc la première question à l'admin: **quel est notre contrat?**

Note: Source: "the seat fee covers access only, and all usage is billed separately at API rates" (article "Claude Enterprise plan overview"). La page des prix d'Anthropic annonce 20 dollars par siège et par mois, avec un minimum de 20 sièges, plus l'usage: à confirmer, le collège a peut-être d'autres conditions. Les sièges "Standard" et "Premium" sont les anciens types de sièges: ils ne sont plus vendus pour les nouveaux contrats.

---
## Le coût d'une demande
- L'IA se paie en **tokens**: tout ce que Claude lit, plus tout ce qu'il écrit
- À chaque message, il **relit toute la conversation**: plus elle est longue, plus chaque message coûte
- Les documents joints et les pages web lues comptent aussi
- Un gros modèle (Opus) et un effort haut coûtent plus qu'un modèle plus léger (Sonnet) et un effort bas

Note: Ordre de grandeur pour la salle, sans chiffres précis: une question courte coûte très peu; une circulaire de 20 pages lue en effort haut coûte bien plus. Le message: ce n'est pas cher pour une vraie tâche, mais les longues conversations qui traînent coûtent sans rien rapporter.

---
## Le modèle change tout
<div class="chart"><svg viewBox="0 0 960 232" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graphique: le prix d'un token par modèle, comparé à Sonnet 5.5">
<text x="20" y="26" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">LE PRIX D'UN TOKEN, COMPARÉ À SONNET 5.5</text>
<text x="140" y="64" font-size="16" fill="#fff" font-weight="700" text-anchor="end">Haiku 5.5</text>
<rect x="155" y="44" width="8" height="28" rx="5" fill="#475363"/>
<text x="175" y="58" font-size="15" fill="#fff" font-weight="700" text-anchor="start">jusqu'à 20 fois moins</text>
<text x="175" y="75" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">le très simple, très vite</text>
<text x="140" y="110" font-size="16" fill="#fff" font-weight="700" text-anchor="end">Sonnet 5.5</text>
<rect x="155" y="90" width="120" height="28" rx="5" fill="#4ade80"/>
<text x="287" y="104" font-size="15" fill="#fff" font-weight="700" text-anchor="start">la référence</text>
<text x="287" y="121" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">le simple: un mail, un résumé court</text>
<text x="140" y="156" font-size="16" fill="#fff" font-weight="700" text-anchor="end">Opus 5.5</text>
<rect x="155" y="136" width="240" height="28" rx="5" fill="#ff4fa8"/>
<text x="407" y="150" font-size="15" fill="#fff" font-weight="700" text-anchor="start">2 fois plus</text>
<text x="407" y="167" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">le gros du travail: une circulaire, un dossier</text>
<text x="140" y="202" font-size="16" fill="#fff" font-weight="700" text-anchor="end">Fable 5.2</text>
<rect x="155" y="182" width="480" height="28" rx="5" fill="#e5007d"/>
<text x="647" y="196" font-size="15" fill="#fff" font-weight="700" text-anchor="start">4 fois plus</text>
<text x="647" y="213" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">seulement une tâche qui le justifie</text>
</svg></div>

- En pratique, l'écart est **plus grand**: un gros modèle réfléchit et écrit davantage
- Le bon modèle pour la tâche est **le premier levier**. Il se choisit **à chaque conversation**

Note: Les prix publics d'Anthropic, par million de tokens lus et par million de tokens écrits (page "Pricing" de la documentation, lue le 12/11/2026): Haiku 5.5: 0,10 et 0,50 dollar (pour les demandes de moins de 100 000 tokens). Sonnet 5.5: 2 et 10 dollars. Opus 5.5: 4 et 20 dollars. Fable 5.2: 8 et 40 dollars. Selon la documentation, un contrat Entreprise à l'usage paie ces tarifs: à confirmer pour le collège. Le message: un mauvais choix se paie à chaque message. Tout faire avec Fable coûte au moins quatre fois plus que tout faire avec Sonnet, pour un résultat souvent identique sur une tâche simple. Mais l'inverse coûte aussi: un modèle trop léger sur une tâche difficile, et on recommence. L'effort haut et le mode rapide augmentent encore la facture. Deux précisions: "20 fois moins" pour Haiku vaut pour les demandes de moins de 100 000 tokens (au-delà, 4 fois moins que Sonnet), et "4 fois plus" vaut pour Fable 5.2 (les versions 5 et 5.1 coûtent 5 fois plus).

---
## Une longue conversation coûte de plus en plus
<div class="chart"><svg viewBox="0 0 960 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graphique: à chaque message, Claude relit plus de texte">
<text x="20" y="24" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">CE QUE CLAUDE RELIT, MESSAGE APRÈS MESSAGE</text>
<rect x="60" y="138" width="44" height="12" rx="4" fill="#475363"/>
<text x="82" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">1</text>
<rect x="122" y="126" width="44" height="24" rx="4" fill="#475363"/>
<text x="144" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">2</text>
<rect x="184" y="114" width="44" height="36" rx="4" fill="#475363"/>
<text x="206" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">3</text>
<rect x="246" y="102" width="44" height="48" rx="4" fill="#475363"/>
<text x="268" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">4</text>
<rect x="308" y="90" width="44" height="60" rx="4" fill="#475363"/>
<text x="330" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">5</text>
<rect x="370" y="78" width="44" height="72" rx="4" fill="#475363"/>
<text x="392" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">6</text>
<rect x="432" y="66" width="44" height="84" rx="4" fill="#475363"/>
<text x="454" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">7</text>
<rect x="494" y="54" width="44" height="96" rx="4" fill="#475363"/>
<text x="516" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">8</text>
<rect x="556" y="42" width="44" height="108" rx="4" fill="#475363"/>
<text x="578" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">9</text>
<rect x="618" y="30" width="44" height="120" rx="4" fill="#ff4fa8"/>
<text x="640" y="170" font-size="13" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="middle">10</text>
<text x="690" y="70" font-size="15" fill="#fff" font-weight="700" text-anchor="start">1 conversation de 100 messages</text>
<text x="690" y="92" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">relit environ 9 fois plus de texte</text>
<text x="690" y="112" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">que 10 conversations de 10 messages</text>
</svg></div>

- À chaque message, Claude **relit tout** ce qui précède: vos messages, ses réponses, les documents, les pages lues
- Avec un agent, c'est plus fort encore: chaque étape **s'ajoute au contexte**, et tout est relu à l'étape suivante
- La parade: **une conversation par sujet**. La fiabilité baisse aussi avec la longueur (partie 5): on paie plus, pour moins bien

Note: Un calcul simple pour la salle: dix conversations de 10 messages font relire environ neuf fois moins de texte qu'une seule conversation de 100 messages. Le cache réduit le prix de ce qui est relu, mais il expire après quelques minutes, et il ne change pas la logique: plus c'est long, plus chaque message coûte.

---
## Ce qui coûte le plus
- **Le modèle**: Fable consomme énormément, Opus beaucoup, Sonnet moins, Haiku peu. Et l'effort haut consomme plus
- **Les longues conversations**: chaque message relit tout l'historique
- **Les tâches d'agent** (Cowork, Claude in Chrome): beaucoup d'étapes, donc beaucoup de tokens que vous ne voyez pas
- **Plusieurs agents** en même temps: chacun fait ses propres demandes
- **Une tâche planifiée oubliée**: elle tourne même quand personne ne regarde

Note: Les trois premières lignes viennent du guide de consommation d'Anthropic pour Claude Entreprise (Fable "Very High", Opus "High", Sonnet "Moderate", Haiku "Low"). Les deux dernières viennent de la documentation de Claude Code, l'outil des développeurs: la logique est la même, mais ce n'est pas écrit pour l'application de bureau.

---
## Sous le capot: le cache et la compaction
- **Le cache**: Claude garde le début de la conversation pendant quelques minutes. Il ne retraite pas tout à chaque message: c'est plus rapide et moins cher
- Après une longue pause, il doit tout relire: une longue conversation reprise le lendemain **coûte plus**. La qualité, elle, ne change pas
- **La compaction**: quand une conversation devient trop longue, Claude **résume le début**, et il continue à partir de ce résumé
- C'est **peu fiable**: beaucoup d'informations se perdent. N'attendez pas la compaction: repartez avant, avec un prompt de passage
- Si une consigne compte, mettez-la **dans votre base de connaissances**

Note: Le cache est documenté pour Claude Code. Je n'ai rien trouvé d'officiel pour l'application de bureau: le principe est le même, les détails peuvent être différents. La compaction existe aussi dans l'application Claude (Claude Desktop). Montrer une longue conversation déjà compactée, préparée avant la séance. Image utile: un PV de réunion garde les décisions et perd les détails.

---
## Ce que chacun fait
1. **Le bon modèle pour la tâche**, choisi à chaque conversation: Sonnet pour le simple, Opus pour le gros travail. Fable seulement pour une tâche qui le justifie
2. **Une conversation par sujet**, et courte: une longue conversation coûte de plus en plus à chaque message
3. **Le bon effort**: bas ou moyen pour le travail courant, haut pour ce qui doit être juste
4. Joindre **seulement ce qui sert** à la tâche
5. **Arrêter** un agent qui tourne en rond, au lieu de le laisser continuer
6. Regarder **sa consommation** de temps en temps: **Paramètres > Utilisation**

Documentation: [Bonnes pratiques pour les limites d'utilisation](https://support.claude.com/fr/articles/9797557)

Note: Chaque membre voit sa propre consommation si les propriétaires de l'organisation ont activé le réglage "Member analytics" (activé par défaut depuis juillet 2026 sur les contrats à l'usage, selon la documentation). Chemin dans la documentation en anglais: "Settings > Usage".

---
## Ce que l'admin règle
- **Une limite pour le collège**: la dépense maximum pour toute l'organisation
- **Une limite par personne**, ou par groupe. La plus basse des deux s'applique
- Ce sont des limites **dures**: quand elle est atteinte, l'usage s'arrête
- **Des alertes** préviennent l'admin à 75% et à 90% de la limite du collège
- **Les modèles autorisés** et le modèle par défaut: on peut retirer Fable, et plafonner l'effort
- **Les fonctions**: Cowork, Claude in Chrome et la recherche web peuvent être coupés

Note: Dans la documentation en anglais: les limites sont dans "Organization settings > Usage", les modèles dans "Organization settings > Models", et les rôles dans "Organization settings > Roles". Attention: selon la documentation, la restriction des modèles n'est pas encore appliquée dans Claude in Chrome. Une personne peut dépasser un peu sa limite: l'usage est compté après chaque demande.

---
## Pour l'admin: suivre les dépenses
- L'admin voit la dépense **par personne, par modèle et par produit**, avec un export en tableau (CSV)
- Il voit aussi qui est **bloqué** et qui est **proche de sa limite**
- Chaque personne voit **sa propre consommation**, si l'admin l'a permis
- Les chiffres ont **un jour de retard**: on ne voit pas la dépense de la dernière heure

Note: Dans la documentation en anglais: "Analytics" (initiales en bas à gauche), et "Settings > Analytics > Export spend report" pour le fichier CSV (une ligne par personne et par modèle). La page "Usage" de l'organisation montre "Blocked right now" et "Near their limit". Tous les admins ne voient pas la dépense: certains rôles voient les statistiques, pas les montants.

---
## Quand une limite est atteinte
- Claude **s'arrête**, et il le dit
- Vous pouvez **demander plus d'usage**: l'admin accepte ou refuse
- Sinon, les limites repartent à zéro **le 1er du mois**
- Ensuite, cherchez la cause: une conversation interminable? Fable? Un agent laissé seul?

Note: Le bouton s'appelle "Request more usage" dans la documentation en anglais. Remise à zéro: le 1er du mois à minuit, heure UTC. Sur un ancien contrat avec quota, c'est différent: des limites par session de quelques heures et par semaine.

---
## Pour l'admin: les réglages du premier jour
Pour la direction et l'admin:

1. **Une limite pour le collège**, et **une limite par personne**
2. Savoir **qui reçoit les alertes** à 75% et à 90%
3. **Le modèle par défaut**: Sonnet ou Opus. Fable retiré, ou réservé à quelques personnes
4. **La consommation visible** pour chacun
5. Une personne qui regarde la dépense **une fois par mois**: par personne, par modèle, et ce qui a changé
6. **Couper ce qui ne sert pas**: la mémoire pour tout le collège, et le réglage "Auto" tant que personne n'en a besoin

Une limite n'est pas une punition: c'est **une ceinture de sécurité**. Elle arrête un agent qui tourne seul, ou une tâche oubliée, avant la facture.

---
## À demander à l'admin du collège
- Quel est notre contrat: **l'usage au volume**, ou un ancien contrat avec un quota?
- Quel est **le budget**, et quelles limites sont déjà en place?
- Qui est l'admin, et **qui reçoit les alertes**?
- Quels **modèles** sont autorisés? Fable l'est-il?
- Où chacun voit-il **sa consommation**?

Note: Tant que ces réponses manquent, rester prudent dans la séance: dire "le collège paie selon l'usage, l'admin peut mettre des limites, regardez votre consommation", sans chiffres.
