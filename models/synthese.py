import pandas as pd 
from models.comparaison import ENSEIGNES

def victoires (tableau):
    resultat = {}
    for e in ENSEIGNES:
        resultat[e] = int((tableau[e] == tableau["prix_min"]).sum())
    return resultat

def ecart_moyen(tableau):
    resultat = {}
    for e in ENSEIGNES:
        ecart = tableau[e] - tableau["prix_min"]
        resultat[e] = {
            "fcfa": round(ecart.mean()),
            "pct": round((ecart / tableau["prix_min"] * 100).mean(), 1),
        }
    return resultat 

def top3_gains(tableau):
    colonnes = ["produit_id", "nom", "moins_chere", "ecart_FCFA", "ecart_pct"]
    return tableau.sort_values("ecart_FCFA", ascending=False).head(3)[colonnes]