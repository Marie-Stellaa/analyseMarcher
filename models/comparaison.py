import pandas as pd 
ENSEIGNES = ["Marché Lagune", "Baobab Shop", "Comptoir Ivoire"]

def comparer(df): 
    ok = df[df["disponible"] & df["prix_paye"].notna()]
    tableau = ok.pivot(index="produit_id", columns="enseigne", values= "prix_paye")
    tableau = tableau[tableau.notna().sum(axis=1)>= 2].copy()

    tableau["prix_min"] = tableau[ENSEIGNES].min(axis=1)
    tableau["moins_chere"] = tableau[ENSEIGNES].idxmin(axis=1)
    tableau["ecart_FCFA"] = tableau[ENSEIGNES].max(axis=1) - tableau["prix_min"]
    tableau["ecart_pct"] = (tableau["ecart_FCFA"] / tableau["prix_min"] * 100).round(1)

    catalogue = pd.read_csv("data/catalogue_reference.csv").set_index("produit_id")
    tableau["nom"] = catalogue["nom"]

    return tableau.reset_index()

def exporter_comparatif(tableau):
    tableau.to_csv("resultats/comparatif_prix.csv", index= False, encoding= "utf-8-sig")