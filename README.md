[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)

# P4_oliva_maximilien

Application de gestion hors-ligne de tournoi d'échec avec un système de ronde suisse.

## PEP-8

Depuis l'emplacement du script, dans un terminal de commande:

`flake8 --max-line-length 119 --exclude=venv/ --format=html --htmldir=flake8-html`

Un nouveau rapport flake8-html sera généré dans un répertoire 'flake8-html'


### Informations complémentaires

Utiliser le fichier 'requirements.txt' lors de l'initialisation de l'environement virtuel\
(cf. Lancements du script) pour l'installation des librairies nécéssaires.

### Création de l'environnement virtuel

Dans un terminal de commande, depuis l'emplacement du programme, :\
\
`python3 -m venv venv`\
\
`cd /venv/Scripts/`\
\
`activate`

### Lancement du script
\
`cd ../..`\
\
`pip install -r requirements.txt`\
\
`python3 main.py`

## Utilisation

 + **"1. Créer Joueur"** : *Ajout d'un joueur dans la base de donnée locale*
 + **"2. Créer tournoi"** : *Ajout d'un tournoi à partir d'une liste de 8 joueurs, 4 tours par défaut, au format ronde 
   suisse.*
 + **"3. Entrée les résultats d'un match"** : *Renseigner les résultats d'un match, génére le tour suivant lorsque 
   les résultats du tour sont renseignés*
 + **"4. Rapports"** : Permet d'accéder à :
   + *La liste de tous les joueurs*,
   + *La liste de tous les tournois*:
     + *la liste de tous les joueurs d'un tournoi*,
     + *le détail de chaque tour d'un tournoi*,
     + *le détail de chaque match pour chaque tour d'un tournoi*
   + *Modifier le rang d'un joueur*
 + **"0. Quitter programme"**