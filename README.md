# Analyse comparative de prix

Comparateur de prix entre trois enseignes (Marché Lagune, Baobab Shop, Comptoir Ivoire). Le programme lit les fichiers de chaque enseigne (CSV, JSON, Excel), les nettoie, les associe à un catalogue de 30 produits, puis compare les prix. Il calcule aussi un panier de rentrée et l'effet du Black Friday.



## Installation

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
pip install pandas openpyxl
```

## Utilisation

À la racine du projet :

```bash
python main.py
```

Le programme écrit `resultats/comparatif_prix.csv` et `resultats/journal.txt`, puis affiche un menu : comparatif, synthèse, panier, historique (Black Friday) et complexité.

## Structure du projet

```
main.py
controllers/    main_controller.py
models/         chargement, nettoyage, rapprochement, comparaison,
                synthese, panier, historique
views/          menu, comparatif, synthese, panier, historique
data/           fichiers fournis
resultats/      comparatif_prix.csv, journal.txt
```

Le projet suit l'architecture MVC.

## Avertissement

Ce projet est un simple projet d'école, sans aucune valeur commerciale. Les enseignes Marché Lagune, Baobab Shop et Comptoir Ivoire n'existent pas, et les prix ne correspondent à aucun magasin réel. Les résultats ne doivent pas être utilisés pour de vraies décisions d'achat.

## Auteure

Godé Ayekpa Epiphanie Marie-Stella Rachel
