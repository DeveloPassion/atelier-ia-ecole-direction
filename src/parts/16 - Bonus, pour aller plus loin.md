# 16 - Bonus, pour aller plus loin

---
## 16. Bonus: pour aller plus loin
Des fonctions avancées, à découvrir après l'atelier.

---
## Les tâches planifiées
- Claude peut faire une tâche **à une heure fixe**, tous les jours ou toutes les semaines, sans que vous le demandiez
- Exemples: chaque lundi à 7h, **la revue de la semaine**; chaque vendredi, la liste des sorties qui ne sont pas encore payées
- Une tâche qui lit **vos fichiers** (votre base de connaissances) tourne **sur votre PC**: il doit être allumé, avec l'application ouverte
- Les autres tâches tournent chez Anthropic, même si votre PC est éteint
- Commencez par **une seule** tâche planifiée, et relisez ses résultats pendant quelques semaines

Note: Disponible sur tous les abonnements payants, Entreprise compris, si l'admin n'a pas coupé Cowork (centre d'aide d'Anthropic, lu le 13/11/2026). C'est le premier pas vers une IA qui prend l'initiative (partie 7). La slide suivante montre comment en créer une.

---
## Créer une tâche planifiée
1. Dans la barre de gauche de l'application, ouvrez **"Planifiées"**, puis cliquez sur **"Nouvelle tâche"**
2. Choisissez **"Créer avec Claude"**: il vous pose ses questions (quoi, quel jour, à quelle heure)
3. Relisez le nom, l'horaire et les instructions qu'il propose, puis cliquez sur **"Planifier"**
4. Encore plus simple: décrivez la tâche dans une conversation. "Chaque lundi à 7h, fais ma revue de la semaine à partir de mon journal et de mes projets."{copy}

Pour voir une tâche, la modifier, la mettre en pause, la lancer tout de suite ou la supprimer: la page **"Planifiées"**.

Documentation: [Planifier des tâches récurrentes dans Claude Cowork](https://support.claude.com/fr/articles/13854387)

Note: Les noms des boutons viennent de la page en français du centre d'aide, lue le 13/11/2026: à vérifier sur leur PC, l'application change souvent. L'autre choix du bouton "Nouvelle tâche" s'appelle "Configurer manuellement": un formulaire avec un nom, la demande, le mode d'approbation, la fréquence (toutes les heures, chaque jour, chaque semaine, les jours ouvrables, ou à la main), et en option un modèle et un dossier de travail. Pour une tâche qui lit la base de connaissances: choisir le dossier de la base comme dossier de travail. Conseil: le mode d'approbation le plus prudent pour commencer, parce que personne ne regarde quand la tâche tourne. La documentation ne dit pas ce qu'une tâche planifiée coûte: elle consomme comme une demande normale, à chaque passage.

---
## La mémoire de Claude
- Claude peut **retenir des informations** sur vous d'une conversation à l'autre
- Mais cette mémoire est **chez Anthropic**: on voit mal ce qu'elle contient, et elle ne passe pas dans un autre outil
- Elle peut aussi **mélanger les sujets**: une information d'une conversation revient là où elle n'a rien à faire
- Mon conseil, comme dans la partie 5: **désactivez-la**, et gardez votre contexte dans **votre base de connaissances**
- Comment: **Paramètres > Votre Claude** (ou Paramètres > Mémoire). Coupez la génération de la mémoire à partir des conversations, et aussi **"Rechercher et référencer les chats"**

Documentation: [La recherche de chat et la mémoire de Claude](https://support.claude.com/fr/articles/11817273)

Note: Chemin lu le 13/11/2026 dans le centre d'aide: "Settings > Your Claude", avec un interrupteur "Generate memory from chats", et les choix "Pause memory" (mettre en pause) et "Reset memory" (tout effacer). Le nom exact en français est à vérifier sur leur PC. Sur Entreprise, un propriétaire de l'organisation peut couper la mémoire pour tout le monde (paramètres de l'organisation, rubrique des capacités): à proposer à l'admin du collège. Pour les organisations créées depuis le 31/10/2026, la mémoire est activée au départ pour chaque membre. Lien avec la partie 7: la mémoire est un contexte loué; votre base de connaissances est un contexte à vous.

---
## Claude dans Word, Excel, PowerPoint et Outlook
Des compléments mettent Claude **dans vos applications Microsoft 365**. Vous lui parlez du fichier ou du mail qui est ouvert.

| L'application | Ce que Claude y fait |
|---|---|
| **Word** | Répondre à vos questions sur le document, réécrire un passage, travailler en **suivi des modifications**, traiter les commentaires |
| **Excel** | Lire et écrire des cellules, des formules, des tableaux croisés et des graphiques |
| **PowerPoint** | Lire, modifier et créer des slides, avec vos modèles |
| **Outlook** (en test) | Trier la boîte de réception, résumer un long échange, préparer une réponse. **Il n'envoie jamais**: le brouillon reste à relire |

Documentation: [Claude for M365 (en anglais)](https://claude.com/docs/office-agents/overview)

Note: Lu le 13/11/2026 dans la documentation de Claude. Le nom du produit: "Claude for Microsoft 365". À ne pas confondre avec le connecteur Microsoft 365 du bonus 13: le connecteur donne à l'application Claude un accès à vos fichiers et à vos mails; les compléments, eux, mettent Claude dans Word, Excel, PowerPoint et Outlook. Les quatre compléments partagent la conversation: on peut passer d'un mail à un document. La dictée existe aussi. Disponible sur les abonnements Pro, Max, Team et Entreprise; Outlook est en bêta.

---
## Claude dans Office: l'obtenir, et rester prudent
1. Pour vous: la page **"Claude for Microsoft 365"** de la boutique de Microsoft, bouton **"Get it now"**. Puis ouvrez Word, activez le complément (onglet Accueil, Compléments), et connectez-vous avec **le compte Claude du collège**
2. Pour tout le collège: l'administrateur Microsoft 365 le déploie, dans son centre d'administration
3. Pour Outlook: cet administrateur donne aussi **un accord, une seule fois**, pour la lecture des boîtes mail

- Claude lit **le document ou le mail ouvert**, et ce contenu part chez Anthropic: pas de données d'élèves sans l'accord du collège et du DPO (partie 8)
- Un document reçu de l'extérieur peut cacher **des instructions pour l'IA**: relisez chaque modification avant de l'accepter

Documentation: [Claude for Word (en anglais)](https://claude.com/docs/office-agents/word) · [Claude for Outlook (en anglais)](https://claude.com/docs/office-agents/outlook)

Note: Lu le 13/11/2026. Versions: Word sur le web, Word pour Windows avec un abonnement Microsoft 365 (version 2205 ou plus récente), Word pour Mac (16.61 ou plus récente). Pas Word 2016 ou 2019, ni iPad, ni Android. Outlook: seulement une boîte Exchange Online (Microsoft 365), et pas les boîtes partagées. Côté administrateur: centre d'administration Microsoft 365, "Settings", "Integrated apps", chercher "Claude for Microsoft 365". Pour Outlook, l'accord est un consentement Microsoft Graph, donné par un administrateur général. L'usage compte sur le même compte Claude, avec les mêmes limites. Les données: supprimées chez Anthropic dans les 30 jours; le complément ne reprend pas les réglages de conservation particuliers de l'organisation. Problème connu: après les mises à jour de Microsoft 365 de septembre et d'octobre 2026 sur Windows, certaines personnes ne voient plus leur historique dans le complément.

---
## Claude sur le téléphone
- L'application Claude existe sur iPhone et Android, avec **le même compte**: vos conversations suivent
- Idéal pour **capturer**: dicter une idée ou une décision en sortant d'une réunion
- Mais le téléphone **n'a pas accès à votre base de connaissances**, qui est sur le PC: Claude y repart presque de zéro
- Le plus simple: noter sur le téléphone, puis **ranger dans la base** au bureau
- Donner une tâche depuis le téléphone à Claude sur le PC existe (la fonction **Dispatch**), mais en test, sur des abonnements personnels: **pas sur Entreprise** pour l'instant

Documentation: [Attribuer des tâches depuis n'importe où dans Claude Cowork](https://support.claude.com/fr/articles/13947068)

Note: Question probable. Dispatch (dans Cowork, application de bureau): une conversation relie le téléphone et le PC; la tâche tourne sur le PC, avec ses fichiers et ses connecteurs. Le PC doit rester allumé, avec l'application ouverte. Selon le centre d'aide (lu le 13/11/2026), c'est une bêta limitée à certains abonnements Pro, Max et Ultra, fermée aux nouveaux utilisateurs; la page ne parle pas des abonnements Team et Entreprise. Sans Dispatch, le téléphone sert à capturer et à poser des questions générales, pas à travailler dans la base. La dictée sur le téléphone marche en français (en bêta, selon la documentation).

---
## Le téléphone et vos données
- **Le compte du collège**, pas un compte personnel, même sur le téléphone
- Un téléphone se perd: **code de verrouillage**, et pas de documents sensibles enregistrés dessus
- **Pas de photo** d'un document avec des données d'élèves
- Si le téléphone peut donner des ordres au PC, il peut aussi y **lire, déplacer ou supprimer** des fichiers: même prudence qu'au bureau
- Une copie de la base sur le téléphone, c'est pratique, mais c'est **une copie de plus à protéger**

---
## La documentation d'Anthropic, en français
| Pour | La page du centre d'aide |
|---|---|
| Cowork | [Commencer avec Claude Cowork](https://support.claude.com/fr/articles/13345190) |
| Planifier une tâche | [Planifier des tâches récurrentes dans Claude Cowork](https://support.claude.com/fr/articles/13854387) |
| Couper la mémoire | [La recherche de chat et la mémoire de Claude](https://support.claude.com/fr/articles/11817273) |
| Ajouter un connecteur | [Utiliser les connecteurs](https://support.claude.com/fr/articles/11176164), [Configurer le connecteur Microsoft 365](https://support.claude.com/fr/articles/12542951) |
| Les skills | [Utiliser les compétences dans Claude](https://support.claude.com/fr/articles/12512180), [Créer des compétences personnalisées](https://support.claude.com/fr/articles/12512198) |
| Le navigateur | [Commencer avec Claude dans Chrome](https://support.claude.com/fr/articles/12012173) |
| Voir sa consommation | [Bonnes pratiques pour les limites d'utilisation](https://support.claude.com/fr/articles/9797557) |
| Les artefacts | [Que sont les artefacts et comment les utiliser?](https://support.claude.com/fr/articles/17153992) |
| L'ordinateur | [Laisser Claude utiliser votre ordinateur dans Cowork](https://support.claude.com/fr/articles/14128542) |

Note: Liens vérifiés le 13/11/2026: toutes ces pages existent en français. Le centre d'aide est traduit, et les noms des menus y sont en français. Attention: dans l'application et dans la documentation en français, les skills s'appellent des "compétences". Ces pages changent souvent: les relire avant une séance.

---
## La documentation de Claude, en anglais
Plus détaillée que le centre d'aide, mais en anglais. Demandez à Claude de vous traduire une page.

| Pour | La page de la documentation |
|---|---|
| Cowork | [Cowork overview](https://claude.com/docs/cowork/overview) |
| Les connecteurs | [Get started with connectors](https://claude.com/docs/connectors/getting-started), [Google Drive](https://claude.com/docs/connectors/google/drive), [Microsoft 365](https://claude.com/docs/connectors/microsoft/365) |
| Les skills | [Skills overview](https://claude.com/docs/skills/overview), [Create custom skills](https://claude.com/docs/skills/how-to) |
| Claude dans Office | [Claude for M365 overview](https://claude.com/docs/office-agents/overview) |

Note: Pages lues le 13/11/2026. Je n'ai pas trouvé de version française de cette documentation.
