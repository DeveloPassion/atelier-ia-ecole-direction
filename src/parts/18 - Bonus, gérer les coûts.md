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
## Ce qui coûte le plus
- **Les tâches d'agent** (Cowork, Claude in Chrome): beaucoup d'étapes, donc beaucoup de tokens que vous ne voyez pas
- **Le modèle**: Fable consomme énormément, Opus beaucoup, Sonnet moins, Haiku peu. Et l'effort haut consomme plus
- **Les longues conversations**: chaque message relit tout l'historique
- **Plusieurs agents** en même temps: chacun fait ses propres demandes
- **Une tâche planifiée oubliée**: elle tourne même quand personne ne regarde

Note: Les trois premières lignes viennent du guide de consommation d'Anthropic pour Claude Entreprise (Fable "Very High", Opus "High", Sonnet "Moderate", Haiku "Low"). Les deux dernières viennent de la documentation de Claude Code, l'outil des développeurs: la logique est la même, mais ce n'est pas écrit pour l'application de bureau.

---
## Sous le capot: le cache
- Claude garde le début de la conversation pendant quelques minutes
- Il ne retraite donc pas tout à chaque message: c'est plus rapide et moins cher
- Après une longue pause, il doit tout relire
- Conséquence: une très longue conversation reprise le lendemain **coûte plus**
- Le cache change **le coût et la vitesse**, pas la qualité des réponses

Note: Le cache est documenté pour Claude Code. Je n'ai rien trouvé d'officiel pour l'application de bureau: le principe est le même, les détails peuvent être différents.

---
## Sous le capot: la compaction
- Quand une conversation devient trop longue, Claude **résume le début**
- Il continue à partir de ce résumé
- C'est **peu fiable**: énormément d'informations se perdent, et le risque d'erreurs augmente
- N'attendez pas la compaction: repartez avant, avec un prompt de passage
- Si une consigne compte, mettez-la **dans votre base de connaissances**

Note: La compaction existe aussi dans l'application Claude (Claude Desktop). Montrer une longue conversation déjà compactée, préparée avant la séance. Image utile: un PV de réunion garde les décisions et perd les détails.

---
## Ce que chacun fait
1. **Une conversation par sujet**, et courte
2. **Le bon modèle**: Sonnet pour le simple, Opus pour le gros travail. Fable seulement pour une tâche qui le justifie
3. **Le bon effort**: bas ou moyen pour le travail courant, haut pour ce qui doit être juste
4. Joindre **seulement ce qui sert** à la tâche
5. **Arrêter** un agent qui tourne en rond, au lieu de le laisser continuer
6. Regarder **sa consommation** de temps en temps: dans les paramètres, la page de l'utilisation

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
## Suivre les dépenses
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
## Les réglages du premier jour
Pour la direction et l'admin:

1. **Une limite pour le collège**, et **une limite par personne**
2. Savoir **qui reçoit les alertes** à 75% et à 90%
3. **Le modèle par défaut**: Sonnet ou Opus. Fable retiré, ou réservé à quelques personnes
4. **La consommation visible** pour chacun
5. Une personne qui regarde la dépense **une fois par mois**: par personne, par modèle, et ce qui a changé

---
## À demander à l'admin du collège
- Quel est notre contrat: **l'usage au volume**, ou un ancien contrat avec un quota?
- Quel est **le budget**, et quelles limites sont déjà en place?
- Qui est l'admin, et **qui reçoit les alertes**?
- Quels **modèles** sont autorisés? Fable l'est-il?
- Où chacun voit-il **sa consommation**?

Note: Tant que ces réponses manquent, rester prudent dans la séance: dire "le collège paie selon l'usage, l'admin peut mettre des limites, regardez votre consommation", sans chiffres.
