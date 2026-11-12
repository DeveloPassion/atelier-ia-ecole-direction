# 5 - Le contexte et sa gestion

---
## 5. Le contexte
Le contexte, c'est **tout ce que Claude voit** au moment de répondre.

---
## Ce que Claude voit
- Vos instructions et votre prompt
- La conversation jusqu'ici
- Les documents joints
- Les résultats des outils (une page web, un fichier lu)
- Le reste, **il ne le connaît pas**

Note: ESSENTIEL.

---
## La session
- Une session, c'est une conversation
- À chaque message, Claude **relit toute la conversation** depuis le début
- Entre deux conversations, **il ne se souvient de rien**
- Sauf ce qui est **écrit quelque part**: les fichiers de votre base de connaissances (ou un projet Claude, ou sa mémoire)
- Dans votre base, il ne relit pas tout: il lit **les fichiers qu'il va chercher** pour la tâche

Note: ESSENTIEL. Précision utile si la question vient: Claude ne charge pas toute la base à chaque conversation. Il cherche et il ouvre les fichiers dont il a besoin. D'où l'intérêt d'une base bien rangée, avec des noms clairs.

---
## La conversation grandit à chaque tour
<div class="chart tall"><svg viewBox="0 0 960 346" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma: à chaque tour, Claude relit tous les messages et toutes les réponses d'avant, et la conversation remplit la fenêtre">
<line x1="150" y1="40" x2="940" y2="40" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-dasharray="6 6"/>
<text x="20" y="45" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">0 token</text>
<line x1="150" y1="328" x2="940" y2="328" stroke="#fbbf24" stroke-width="2" stroke-dasharray="6 6"/>
<text x="20" y="322" font-size="14" fill="#fbbf24" font-weight="700" text-anchor="start">La limite de</text>
<text x="20" y="341" font-size="14" fill="#fbbf24" font-weight="700" text-anchor="start">la fenêtre</text>
<text x="295" y="26" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">Tour 1</text>
<rect x="208" y="50" width="174" height="42" rx="10" fill="rgba(255,255,255,0.07)"/>
<text x="196" y="71.0" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="700" text-anchor="middle" transform="rotate(-90 196 71.0)">lu</text>
<rect x="220" y="57" width="150" height="28" rx="7" fill="rgba(229,0,125,0.78)" stroke="#fff" stroke-width="2"/>
<text x="295" y="76.0" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Votre message</text>
<rect x="208" y="100" width="174" height="50" rx="10" fill="rgba(74,222,128,0.10)" stroke="rgba(74,222,128,0.6)" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="196" y="125.0" font-size="14" fill="#4ade80" font-weight="700" text-anchor="middle" transform="rotate(-90 196 125.0)">écrit</text>
<rect x="220" y="107" width="150" height="36" rx="7" fill="#5a6678"/>
<text x="295" y="130.0" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Sa réponse</text>
<text x="555" y="26" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">Tour 2</text>
<rect x="468" y="50" width="174" height="116" rx="10" fill="rgba(255,255,255,0.07)"/>
<text x="456" y="108.0" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="700" text-anchor="middle" transform="rotate(-90 456 108.0)">relu</text>
<rect x="480" y="57" width="150" height="28" rx="7" fill="rgba(229,0,125,0.78)"/>
<text x="555" y="76.0" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Votre message</text>
<rect x="480" y="90" width="150" height="36" rx="7" fill="#5a6678"/>
<text x="555" y="113.0" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Sa réponse</text>
<rect x="480" y="131" width="150" height="28" rx="7" fill="rgba(229,0,125,0.78)" stroke="#fff" stroke-width="2"/>
<text x="555" y="150.0" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Votre message</text>
<rect x="468" y="174" width="174" height="50" rx="10" fill="rgba(74,222,128,0.10)" stroke="rgba(74,222,128,0.6)" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="456" y="199.0" font-size="14" fill="#4ade80" font-weight="700" text-anchor="middle" transform="rotate(-90 456 199.0)">écrit</text>
<rect x="480" y="181" width="150" height="36" rx="7" fill="#5a6678"/>
<text x="555" y="204.0" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Sa réponse</text>
<text x="815" y="26" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">Tour 3</text>
<rect x="728" y="50" width="174" height="190" rx="10" fill="rgba(255,255,255,0.07)"/>
<text x="716" y="145.0" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="700" text-anchor="middle" transform="rotate(-90 716 145.0)">relu</text>
<rect x="740" y="57" width="150" height="28" rx="7" fill="rgba(229,0,125,0.78)"/>
<text x="815" y="76.0" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Votre message</text>
<rect x="740" y="90" width="150" height="36" rx="7" fill="#5a6678"/>
<text x="815" y="113.0" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Sa réponse</text>
<rect x="740" y="131" width="150" height="28" rx="7" fill="rgba(229,0,125,0.78)"/>
<text x="815" y="150.0" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Votre message</text>
<rect x="740" y="164" width="150" height="36" rx="7" fill="#5a6678"/>
<text x="815" y="187.0" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Sa réponse</text>
<rect x="740" y="205" width="150" height="28" rx="7" fill="rgba(229,0,125,0.78)" stroke="#fff" stroke-width="2"/>
<text x="815" y="224.0" font-size="14" fill="#fff" font-weight="700" text-anchor="middle">Votre message</text>
<rect x="728" y="248" width="174" height="50" rx="10" fill="rgba(74,222,128,0.10)" stroke="rgba(74,222,128,0.6)" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="716" y="273.0" font-size="14" fill="#4ade80" font-weight="700" text-anchor="middle" transform="rotate(-90 716 273.0)">écrit</text>
<rect x="740" y="255" width="150" height="36" rx="7" fill="#5a6678"/>
<text x="815" y="278.0" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Sa réponse</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(398,76)" fill="rgba(255,255,255,0.5)"/>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(658,110)" fill="rgba(255,255,255,0.5)"/>
</svg></div>

À chaque tour, Claude **relit tout**, puis il écrit. La fenêtre se remplit, et chaque message **coûte plus** que le précédent.

Note: ESSENTIEL. Montrer les trois colonnes de gauche à droite. Tour 1: il lit votre message, il écrit sa réponse. Tour 2: il relit le premier message et sa première réponse, plus le nouveau message. Tour 3: il relit tout, encore. Deux conséquences, qui reviennent dans toute la partie: la conversation finit par remplir la fenêtre (la ligne du bas), et chaque message coûte plus cher que le précédent.

---
## Plusieurs conversations en parallèle
- Vous pouvez donner **plusieurs tâches en même temps**: une conversation par tâche
- Par exemple: le tableau des sorties dans l'une, la circulaire dans une autre, un mail aux parents dans une troisième
- Chaque conversation **avance à son rythme**, et vous passez de l'une à l'autre
- Vous relisez et vous corrigez quand une tâche est prête

Note: À PASSER si le temps manque. Le montrer en direct: lancer une tâche longue (par exemple ranger le dossier), puis ouvrir une nouvelle conversation pour un mail court pendant que la première travaille. C'est aussi une bonne raison de faire des conversations courtes: une tâche, une conversation.

---
## La fenêtre de contexte
- C'est la quantité maximum de texte que Claude **lit en une fois**: tout ce qu'il a sous les yeux pendant la conversation
- Elle est grande: environ **un million de tokens**, soit plusieurs centaines de milliers de mots
- Mais elle n'est **pas infinie**, et tout y compte: vos messages, ses réponses, les documents, les pages lues
- Ce qui tient dans la fenêtre **n'est pas forcément bien lu**

Note: ESSENTIEL.

---
## Des mots aux tokens, des tokens au coût
<div class="chart tall"><svg viewBox="0 0 960 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma: ce qui entre devient des tokens, remplit la fenêtre de contexte, et le coût dépend des tokens lus et écrits">
<text x="20" y="24" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">CE QUI ENTRE</text>
<text x="245" y="24" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">EN TOKENS</text>
<text x="486" y="24" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">LA FENÊTRE DE CONTEXTE</text>
<text x="780" y="24" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">CE QUI SORT</text>
<text x="20" y="60" font-size="16" fill="#fff" font-weight="700" text-anchor="start">La demande</text>
<text x="20" y="85" font-size="16" fill="#fff" font-weight="700" text-anchor="start">La conversation</text>
<text x="20" y="110" font-size="16" fill="#fff" font-weight="700" text-anchor="start">Les fichiers</text>
<text x="20" y="135" font-size="16" fill="#fff" font-weight="700" text-anchor="start">Les résultats d'outils</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(208,78) scale(1.0)" fill="#e5007d"/>
<rect x="245" y="50" width="36" height="34" rx="6" fill="#475363" stroke="rgba(255,255,255,0.3)"/>
<text x="263.0" y="73" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">Un</text>
<rect x="285" y="50" width="52" height="34" rx="6" fill="#475363" stroke="rgba(255,255,255,0.3)"/>
<text x="311.0" y="73" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">petit</text>
<rect x="341" y="50" width="44" height="34" rx="6" fill="#475363" stroke="rgba(255,255,255,0.3)"/>
<text x="363.0" y="73" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">mor</text>
<rect x="389" y="50" width="50" height="34" rx="6" fill="#475363" stroke="rgba(255,255,255,0.3)"/>
<text x="414.0" y="73" font-size="16" fill="#fff" font-weight="700" text-anchor="middle">ceau</text>
<text x="245" y="112" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">Un mot peut faire</text>
<text x="245" y="131" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="start">plusieurs tokens</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(448,78) scale(1.0)" fill="#e5007d"/>
<path d="M494,34 h-8 v160 h8" fill="none" stroke="#fff" stroke-width="3"/>
<path d="M720,34 h8 v160 h-8" fill="none" stroke="#fff" stroke-width="3"/>
<rect x="498" y="40" width="218" height="25" rx="4" fill="rgba(96,165,250,0.38)"/>
<text x="607" y="58" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Les instructions</text>
<rect x="498" y="70" width="218" height="25" rx="4" fill="rgba(74,222,128,0.30)"/>
<text x="607" y="88" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">L'historique utile</text>
<rect x="498" y="100" width="218" height="25" rx="4" fill="rgba(251,191,36,0.30)"/>
<text x="607" y="118" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Les fichiers</text>
<rect x="498" y="130" width="218" height="25" rx="4" fill="rgba(168,85,247,0.40)"/>
<text x="607" y="148" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Les résultats d'outils</text>
<rect x="498" y="160" width="218" height="25" rx="4" fill="rgba(255,255,255,0.15)"/>
<text x="607" y="178" font-size="14" fill="#fff" font-weight="400" text-anchor="middle">Le bruit, le contexte périmé</text>
<text x="607" y="216" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="middle">200 000 → 1 million de tokens</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(738,78) scale(1.0)" fill="#e5007d"/>
<text x="780" y="62" font-size="17" fill="#fff" font-weight="700" text-anchor="start">Les tokens</text>
<text x="780" y="85" font-size="17" fill="#fff" font-weight="700" text-anchor="start">de la réponse</text>
<text x="780" y="124" font-size="14" fill="#fbbf24" font-weight="700" text-anchor="start">Session longue:</text>
<text x="780" y="143" font-size="14" fill="#fbbf24" font-weight="400" text-anchor="start">moins fiable</text>
<text x="780" y="172" font-size="14" fill="#fbbf24" font-weight="700" text-anchor="start">Fenêtre pleine:</text>
<text x="780" y="191" font-size="14" fill="#fbbf24" font-weight="400" text-anchor="start">la compaction</text>
<line x1="20" y1="240" x2="940" y2="240" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
<text x="20" y="277" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">LE COÛT</text>
<text x="140" y="278" font-size="19" fill="#fff" font-weight="700" text-anchor="start">tokens lus × prix d'entrée  +  tokens écrits × prix de sortie</text>
<text x="940" y="277" font-size="14" fill="rgba(255,255,255,0.74)" font-weight="400" text-anchor="end">selon le modèle</text>
<line x1="20" y1="302" x2="940" y2="302" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
<text x="20" y="342" font-size="14" fill="#ff4fa8" font-weight="700" text-anchor="start">GÉRER LE CONTEXTE</text>
<text x="250" y="343" font-size="18" fill="#fff" font-weight="700" text-anchor="start">Choisir</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(334,322) scale(0.85)" fill="#e5007d"/>
<text x="380" y="343" font-size="18" fill="#fff" font-weight="700" text-anchor="start">Structurer</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(494,322) scale(0.85)" fill="#e5007d"/>
<text x="540" y="343" font-size="18" fill="#fff" font-weight="700" text-anchor="start">Résumer</text>
<polygon points="0,0 12,0 26,16 12,32 0,32 14,16" transform="translate(630,322) scale(0.85)" fill="#e5007d"/>
<text x="680" y="343" font-size="18" fill="#fff" font-weight="700" text-anchor="start">Rafraîchir</text>
<text x="480" y="386" font-size="17" fill="#fff" font-weight="700" text-anchor="middle">La bonne information, au bon moment.</text>
</svg></div>

Note: À PASSER si le temps manque. Lire l'image de gauche à droite. Tout ce qui entre (la demande, la conversation, les fichiers, les résultats des outils) est coupé en tokens. Ces tokens remplissent la fenêtre de contexte: on y trouve l'utile, et aussi du bruit et du contexte périmé. Le modèle écrit ensuite sa réponse, en tokens aussi. Le coût: les tokens lus et les tokens écrits, chacun à son prix, et ce prix dépend du modèle (bonus 18). Gérer le contexte, c'est choisir ce qui entre, le structurer, le résumer, et le rafraîchir: donner au modèle la bonne information, au bon moment. C'est ce que fait une base de connaissances bien rangée.

---
## Plus c'est long, moins c'est fiable
- La fiabilité **baisse peu à peu** quand la conversation s'allonge, bien avant que la fenêtre soit pleine
- Ce qui est **au milieu** d'un long contexte est moins bien utilisé que le début et la fin
- **Plus n'est pas mieux**: chaque document ajouté rapporte un peu moins, et un document inutile peut faire baisser la qualité. Donnez **ce qui sert à la tâche**
- Les signes: il **oublie une consigne**, il **se répète**, il **mélange les sujets**, il **invente davantage**. Alors: nouvelle conversation
- Ce n'est pas vous: c'est **la limite du contexte**

Note: ESSENTIEL. Il n'y a pas de seuil précis: cela dépend de la tâche et du modèle. Repère pratique avec Opus 5.5 (fenêtre d'un million de tokens): très fiable jusqu'à environ 500 000 à 600 000 tokens. Ce repère vient de l'expérience de Sébastien, pas d'une mesure. On n'approche presque jamais cette taille dans une conversation normale, mais une très longue conversation avec beaucoup de documents peut y arriver. Sources: l'étude "Context Rot" de Chroma (2025, https://www.trychroma.com/research/context-rot): pour la même question, la qualité baisse quand le texte autour s'allonge; et "Lost in the Middle" (2023): le début et la fin d'un long texte sont mieux utilisés que le milieu. La phrase à retenir: la taille de la fenêtre dit combien de texte tient, pas comment il est lu.

---
## La fiabilité selon la longueur
<div class="chart"><svg viewBox="0 0 960 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma: la fiabilité baisse quand la conversation s'allonge">
<rect x="80" y="20" width="480" height="240" fill="rgba(74,222,128,0.13)"/><rect x="560" y="20" width="160" height="240" fill="rgba(251,191,36,0.15)"/><rect x="720" y="20" width="160" height="240" fill="rgba(255,20,147,0.15)"/>
<line x1="80" y1="260" x2="880" y2="260" stroke="rgba(255,255,255,0.55)" stroke-width="2"/><line x1="80" y1="20" x2="80" y2="260" stroke="rgba(255,255,255,0.55)" stroke-width="2"/>
<path d="M80,45 C300,47 460,52 560,64 C640,82 700,122 760,168 C810,205 850,226 880,236" fill="none" stroke="#ff1493" stroke-width="5" stroke-linecap="round"/>
<text x="320" y="200" fill="#4ade80" font-size="22" font-weight="700" text-anchor="middle">Zone confortable</text><text x="640" y="200" fill="#fbbf24" font-size="20" font-weight="700" text-anchor="middle">Prudence</text><text x="800" y="120" fill="#ff4fa8" font-size="20" font-weight="700" text-anchor="middle">Moins fiable</text>
<text x="80" y="288" fill="rgba(255,255,255,0.75)" font-size="17" text-anchor="middle">0</text><text x="280" y="288" fill="rgba(255,255,255,0.75)" font-size="17" text-anchor="middle">250 000</text><text x="480" y="288" fill="rgba(255,255,255,0.75)" font-size="17" text-anchor="middle">500 000</text><text x="680" y="288" fill="rgba(255,255,255,0.75)" font-size="17" text-anchor="middle">750 000</text><text x="880" y="288" fill="rgba(255,255,255,0.75)" font-size="17" text-anchor="middle">1 million</text>
<text x="480" y="318" fill="rgba(255,255,255,0.75)" font-size="17" text-anchor="middle">Taille du contexte (tokens)</text><text x="40" y="140" fill="rgba(255,255,255,0.75)" font-size="17" text-anchor="middle" transform="rotate(-90 40 140)">Fiabilité</text>
</svg></div>

<p class="caption"><span class="tag">Schéma indicatif, pas une mesure</span> Stable longtemps, puis une baisse. Le seuil dépend de la tâche et du modèle.</p>

Note: À PASSER si le temps manque. Ce schéma n'est pas un résultat de benchmark: Anthropic n'a pas publié de courbe de contexte long pour Opus 5.5. La forme (stable, puis une baisse) suit les études "Context Rot" de Chroma (2025) et "Lost in the Middle" (2023). Le repère de 500 000 à 600 000 tokens est dans les notes de la slide précédente.

---
## Le coût, en bref
- L'IA se paie en **tokens**: tout ce que Claude lit, plus tout ce qu'il écrit
- Avec Claude Entreprise, le collège paie **un siège par personne, plus l'usage**
- **Voir sa consommation**: dans les paramètres de l'application, la page de l'utilisation. Regardez-la de temps en temps
- Si une limite est atteinte, Claude s'arrête et le dit: **demander plus à l'admin**, ou attendre
- Premier levier: **le bon modèle pour la tâche**. Opus coûte 2 fois plus que Sonnet, et Fable 4 fois plus
- Deuxième levier: **des conversations courtes**. Claude relit tout à chaque message: une longue conversation coûte de plus en plus
- Le détail (les prix, les limites, le suivi): **bonus 18**

Note: À PASSER si le temps manque, sauf l'écran de l'utilisation: le montrer en direct (dans les paramètres; la documentation en anglais dit "Settings > Usage", le nom exact dépend de la version et de la langue). À vérifier avec l'admin avant la séance: le contrat exact (usage au volume, ou ancien contrat avec un quota inclus), les limites par personne, et si chacun voit bien sa consommation. Si le contrat est un ancien contrat avec quota, adapter la deuxième ligne: "les tokens comptent dans votre quota". Ordre de grandeur pour la salle, sans chiffres précis: une question courte coûte très peu; une circulaire de 20 pages lue en effort haut coûte bien plus.

---
## L'entonnoir du contexte
```mermaid
flowchart TD
  A[Pas de contexte] --> A2[Réponse générique]
  B[Trop peu] --> B2[Réponse vague]
  C[Le bon contexte] --> C2[Réponse précise et utile]
  D[Trop de contexte] --> D2[Confusion et erreurs]
```

Note: À PASSER si le temps manque.

---
## Les types de contexte
1. Les instructions: ce que vous voulez, comment
2. Les exemples: un mot aux parents réussi
3. Les connaissances: le règlement, le calendrier
4. La mémoire: ce que Claude retient de vous
5. Les outils: ce que Claude peut aller chercher

Note: À PASSER si le temps manque.

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

Note: ESSENTIEL.

---
## Les projets Claude
- Un projet Claude garde des instructions et des documents **pour toutes ses conversations**
- Exemple: un projet Claude "Direction primaire" avec le ton de l'école, le règlement, le calendrier
- Pratique, mais tout reste **chez Anthropic**, et chaque projet est une île
- Mon conseil: **pas de projet Claude**, mais **un seul dossier de travail** pour l'IA: votre base de connaissances

Note: À PASSER si le temps manque: la slide suivante dit l'essentiel.

---
## La limite des niveaux 3 et 4
- La mémoire et les projets Claude **vivent chez Anthropic**
- Ils ne passent pas dans un autre outil
- On voit mal ce qu'ils contiennent
- Chacun refait le sien, rien n'est partagé
- C'est un **contexte loué**

La mémoire de Claude est **à proscrire**: elle ne vous appartient pas vraiment, elle est peu fiable, elle retient des choses un peu au hasard, et elle s'en sert un peu au hasard aussi. **Désactivez-la.**

Note: ESSENTIEL. C'est ici qu'on le dit avec force, une seule fois: la mémoire de Claude est à proscrire. Les autres parties y renvoient.

---
## Le niveau 5: votre base de connaissances
- Une **source de contexte** facile d'accès, pour vous et pour l'IA
- L'idéal: des **fichiers texte** (Markdown: du texte simple, avec # pour les titres), dans un dossier à vous
- Elle contient le contexte de **vos rôles, vos projets, vos personnes, vos processus**
- L'idéal: **démarrer chaque conversation dans le dossier** de votre base de connaissances
- Tout ce qui doit durer y va. **Une seule source de vérité**

Note: ESSENTIEL. C'est le fil rouge de la suite: la partie 7 montre à quoi ressemble cette base. Dans l'application Claude, "démarrer dans le dossier" = choisir ce dossier comme dossier de travail.

---
## Des conversations courtes, sur un seul point
**Évitez à tout prix les conversations longues et "fourre-tout".**

1. **Une conversation = un sujet**: un mail, un tableau, une circulaire. Mieux vaut **dix conversations courtes** qu'une seule longue
2. Nouvelle conversation quand vous **changez de sujet**, ou quand les réponses se dégradent
3. Ce qui doit durer va **dans votre base de connaissances**
4. Pour garder la suite d'un travail: **"Donne-moi un prompt que je peux passer à un autre agent pour continuer."{copy}** Collez-le dans une nouvelle conversation
5. N'attendez pas que Claude **résume lui-même** le début d'une conversation trop longue (la compaction): il perd beaucoup d'informations (bonus 18)

Note: ESSENTIEL. C'est la règle la plus importante de la partie: la dire avec force. Les longues conversations sont la cause la plus fréquente des mauvaises réponses et des inventions. Dévier un peu, c'est permis. Si le temps le permet, montrer une longue conversation déjà compactée, préparée avant la séance. Image utile: un PV de réunion garde les décisions et perd les détails.

---
## L'idée centrale
**Résultat = modèle × contexte**

- Le modèle est le même pour vous trois: Claude Entreprise
- Le contexte, c'est vous qui le donnez
- C'est **le seul facteur que vous contrôlez**

Pour un système qui vous connaît: il choisit le bon contexte pour chaque demande, au lieu de tout mettre. Et ce contexte est à vous.

Note: ESSENTIEL.

---
## Pause
10 minutes

Note: Pendant la pause, ouvrir les fichiers des démos et le dossier "Plan B - résultats attendus", au cas où.
