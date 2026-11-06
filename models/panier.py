import pandas as pd
from models.comparaison import ENSEIGNES

PANIER = {"P04": 1, "P12": 1, "P14": 2, "P15": 1, "P28": 1}

def prix_utilisables(df):
    ok = df[df["disponible"] & df["prix_paye"].notna()]
    return ok.pivot(index="produit_id", columns="enseigne", values="prix_paye")

def panier_par_enseigne(prix):
    resultat = {}
    for e in ENSEIGNES:
        total = 0
        manquants = []
        for produit, quantite in PANIER.items():
            p = prix.loc[produit, e]
            if pd.isna(p):
                manquants.append(produit)
            else:
                total += p * quantite
        resultat[e] = {"total": total, "manquants": manquants}
    return resultat

def panier_optimal(prix):
    total = 0
    choix = {}
    for produit, quantite in PANIER.items():
        ligne = prix.loc[produit]
        choix[produit] = ligne.idxmin()
        total += ligne.min() * quantite
    return total, choix