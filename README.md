# Subject template

Ce dépôt est le point de départ d'un sujet Manta Academy. L'étudiant n'a pas
besoin de connaître Nuxt ni de gérer un second dépôt : chaque push sur `main`
reconstruit le site et remplace la branche `gh-pages` de ce même dépôt.

## Créer un sujet

1. Créez un dépôt depuis ce template.
2. Ajoutez les sujets français dans `subjects/fr` et anglais dans
   `subjects/en`.
3. Placez les images et autres fichiers dans `assets`.
4. Copiez `metadata.example.yml` vers `metadata.yml` et configurez les outils.
5. Poussez sur `main`.

La première fois, configurez GitHub Pages sur **Deploy from a branch**, branche
`gh-pages`, dossier `/`. Dans les paramètres Actions du dépôt, les workflows
doivent disposer des permissions de lecture et d'écriture.

## Outils

Un outil distant est récupéré depuis un dépôt GitHub public :

```yaml
tools:
  - id: match
    repository: MEA-RUN/match
    ref: main
```

Un outil propre au sujet peut être placé directement dans le dépôt :

```text
tools/
  mon-outil/
    index.html
    style.css
    script.js
```

```yaml
tools:
  - id: mon-outil
    path: tools/mon-outil
    name: Mon outil
```

Les assets référencés par `index.html` doivent utiliser des chemins relatifs.
Les champs facultatifs `entrypoint`, `icon`, `description`, `version` et
`category` peuvent être déclarés dans `metadata.yml`.

## Sécurité des dépôts d'organisation

Le déploiement vérifie explicitement que l'auteur du push possède au minimum le
droit d'écriture sur le dépôt. Une pull request provenant d'un fork ne publie
rien avant sa validation et son merge sur `main`. Protégez également `main`
avec les règles de revue adaptées à votre organisation.

## Structure

```text
assets/
metadata.yml
subjects/
  en/
  fr/
tools/
```
