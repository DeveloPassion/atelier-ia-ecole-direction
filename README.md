# L'IA au service de l'école

Atelier d'environ 2 heures pour une direction d'école: comprendre l'IA générative et l'IA agentique, démarrer avec Claude, rester prudent, et voir l'intérêt d'un système qui vous connaît et qui vous appartient. Préparé pour le Collège de Bonne-Espérance.

Les personnes et les documents de démo sont fictifs: ce support sert à apprendre.

- Le cours en ligne: https://developassion.github.io/atelier-ia-ecole-direction/
- 17 parties: 9 pour l'atelier, une par bloc, et 8 bonus (trucs et astuces, techniques de prompting, plusieurs agents, connecteurs et MCP, skills, l'IA et les élèves, pour aller plus loin, questions fréquentes). Chaque partie s'ouvre dans son onglet. Dans une partie: `S` pour les notes de l'orateur (les étapes des démos), `F` pour le plein écran, `Échap` pour la vue d'ensemble

## Contenu

- `index.html` et `01-...html` à `17-...html`: les slides (reveal.js), qui marchent aussi hors ligne
- `documents/`: l'aide-mémoire à imprimer, les prérequis, la fiche de contexte (PDF à remplir) et un projet de règles d'usage de l'IA
- `fichiers-de-demo.zip`: les mêmes fichiers de démo, en un seul zip à télécharger (https://developassion.github.io/atelier-ia-ecole-direction/fichiers-de-demo.zip)
- `fichiers-de-demo/`: les fichiers des démos, tous fictifs (voir `LISEZ-MOI.txt`), les résultats attendus (plan B) et deux dossiers de démo: "en vrac" et "notes seules"

## Les sources

- `src/parts/`: les textes des slides, un fichier Markdown par partie (`---` sépare les slides, `Note:` commence les notes de l'orateur). L'ordre, les durées et les noms des fichiers HTML sont dans `src/parts.json`
- `src/demo/`: les deux systèmes de démo, "notes seules" et "en vrac", en clair. Les dossiers vides gardent un fichier `.gitkeep`
- `tools/build.py`: les slides et `index.html`. `lib/` et `theme.css` ne changent pas
- `tools/handouts.py`: les PDF de `documents/` (prérequis, fiche de contexte, règles d'usage)
- `tools/aide_memoire.py`: l'aide-mémoire (deux pages, à garder en phase avec les slides)
- `tools/feuille_de_route.py`: la feuille de route de l'animateur (quelle démo, quand, avec quels fichiers). Elle lit les slides; on l'écrit hors du dépôt, elle n'est pas publiée
- `tools/build_demo.py`: les zips des systèmes de démo et `fichiers-de-demo.zip`. Le système complet (avec AI Kit for Obsidian, un produit payant) n'est pas dans ce dépôt: `--private-dir` met à jour sa copie privée

## Reconstruire

Depuis la racine du dépôt:

```
python3 tools/build.py
uv run --with reportlab python tools/handouts.py
uv run --with reportlab python tools/aide_memoire.py
python3 tools/build_demo.py
```

Publier: commit, puis push sur `main`. GitHub Pages met le site à jour en une minute environ.

## Licence

© 2026 Sébastien Dubois / DeveloPassion. Tous droits réservés. Voir [LICENSE](LICENSE).

Les bibliothèques et la police incluses dans `lib/` gardent leur propre licence: reveal.js (MIT), Pele (MIT), Noto Sans (SIL Open Font License 1.1).
