import pandas as pd

journal = []

def noter(message):
    journal.append(message)

def texte_en_nombre(valeur):
    if isinstance(valeur, (int, float)):
        if valeur !=valeur: 
            return None
        return valeur 
    chiffres ="".join(c for c  in str(valeur) if c.isdigit())
    if chiffres == "":
        return None 
    return int(chiffres) 

def nettoyer_marche_lagune(df):
    avant = len(df)
    df =  df.drop_duplicates().copy()
    noter(f"Marché Lagune :{ avant - len(df)} doublon(s) supprimé(s)")

    df["nom"]= df["nom"].str.strip().str.lower()

    df["prix"]= df["prix"].apply( texte_en_nombre)
    for code in df [df["prix"].isna()]["code"]:
        noter(f"Marché Lagune: prix inutilisable pour {code}")

    df ["disponible"] = df["stock"] != "Rupture"
    df["prix_paye"] = df["prix"]
    return df  

def nettoyer_baobab_shop(df):
    avant = len(df)
    df =  df.drop_duplicates().copy()
    noter(f"Baobab Shop : {avant - len(df)} doublon(s) supprimé(s)")

    df["nom"]= df["nom"].str.strip().str.lower()

    df["prix"]= df["prix"].apply( texte_en_nombre)
    for code in df [df["prix"].isna()]["code"]:
        noter(f"Baobab Shop: prix inutilisable pour {code}")

    df ["disponible"] = df["stock"]  > 0
    df["prix_paye"] = df["prix"] + df["livraison"]
    return df  

def nettoyer_comptoir_ivoire(df):
    avant = len(df)
    df =  df.drop_duplicates().copy()
    noter(f"Comptoir ivoire : {avant - len(df)} doublon(s) supprimé(s)")

    df["nom"]= df["nom"].str.strip().str.lower()

    df["prix"]= df["prix"].apply( texte_en_nombre)
    for code in df [df["prix"].isna()]["code"]:
        noter(f"comptoir ivoire: prix inutilisable pour {code}")

    df ["disponible"] = df["stock"]  > 0
    df["prix_paye"] = df["prix"] * (1 - df["remise"] / 100)
    return df 

def nettoyer_tout(df):
    ml = nettoyer_marche_lagune(df[df["enseigne"] == "Marché Lagune"])
    bb = nettoyer_baobab_shop(df[df["enseigne"] == "Baobab Shop"])
    ci = nettoyer_comptoir_ivoire(df[df["enseigne"] == "Comptoir Ivoire"])
    return pd.concat([ml, bb, ci], ignore_index=True)

def ecrire_journal():
    with open("resultats/journal.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(journal))