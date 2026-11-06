import pandas as pd
from models.comparaison import ENSEIGNES

def formater_prix(prix):
    if pd.isna(prix):
        return "—"
    return f"{prix:,.0f}".replace(",", " ") + " FCFA"

def afficher_comparatif(tableau):
    print("\n--- Comparatif des prix (produits présents dans au moins 2 enseignes) ---")
    for _, ligne in tableau.iterrows():
        print(f"\n{ligne['produit_id']} - {ligne['nom']}")
        for e in ENSEIGNES:
            print(f"   {e} : {formater_prix(ligne[e])}")
        print(f"   Moins chère : {ligne['moins_chere']}")
        print(f"   Écart : {formater_prix(ligne['ecart_FCFA'])} ({ligne['ecart_pct']} %)")