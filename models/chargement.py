import pandas as pd
from pathlib import Path
import json

dossier_data = Path("data")

def lire_marche_lagune():
    df = pd.read_csv(dossier_data / "marche_lagune.csv", sep=";", encoding="utf-8-sig")
    df = df.rename(columns={"reference": "code", "designation": "nom", "disponibilite": "stock"})
    df["enseigne"]= "Marché Lagune"
    df["livraison"]=0 
    df["remise"]=0
    return df[["enseigne", "code", "nom", "prix", "livraison", "remise", "stock"]]

def lire_baobab_shop():
    with open(dossier_data / "baobab_shop.json", encoding="utf-8") as f:
        donnees = json.load(f)

    lignes = []
    for article in donnees["items"]:
        lignes.append({
            "enseigne": "Baobab Shop",
            "code": article["sku"],
            "nom": article["title"],
            "prix": article["pricing"]["amount"],
            "livraison": article["pricing"]["delivery_fee"],
            "remise": 0,
            "stock": article["stock"],
        })

    return pd.DataFrame(lignes)

def lire_comptoir_ivoire():
    df = pd.read_excel(dossier_data / "comptoir_ivoire.xlsx", header=2)
    df = df.rename(columns={
        "Code": "code",
        "Article": "nom",
        "Prix catalogue (FCFA)": "prix",
        "Remise (%)": "remise",
        "Quantité en rayon": "stock",
    })
    df["enseigne"] = "Comptoir Ivoire"
    df["livraison"] = 0
    return df[["enseigne", "code", "nom", "prix", "livraison", "remise", "stock"]]

def charger_tout():
    return pd.concat(
        [lire_marche_lagune(), lire_baobab_shop(), lire_comptoir_ivoire()],
        ignore_index=True
    )