import pandas as pd
import csv
import time

def charger_historique():
    h = pd.read_csv("data/historique_prix.csv")
    h["date"] = pd.to_datetime(h["date"])
    return h

def variation_black_friday(h):
    moyenne_annee = h.groupby(["source", "produit_id"])["prix_fcfa"].mean()

    semaine = h[(h["date"] >= "2025-11-24") & (h["date"] <= "2025-11-30")]
    moyenne_semaine = semaine.groupby(["source", "produit_id"])["prix_fcfa"].mean()

    return (moyenne_semaine / moyenne_annee - 1) * 100

def resume_par_enseigne(variation):
    return variation.groupby("source").mean().round(1)

def charger_lignes():
    with open("data/historique_prix.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def chercher_dans_liste(lignes, source, produit, date):
    for ligne in lignes:
        if ligne["source"] == source and ligne["produit_id"] == produit and ligne["date"] == date:
            return int(ligne["prix_fcfa"])
    return None

def construire_dictionnaire(lignes):
    return {(l["source"], l["produit_id"], l["date"]): int(l["prix_fcfa"]) for l in lignes}

def mesurer_recherches(repetitions=200):
    lignes = charger_lignes()
    source, produit, date = "Baobab Shop", "P11", "2025-11-26"

    debut = time.perf_counter()
    for _ in range(repetitions):
        chercher_dans_liste(lignes, source, produit, date)
    temps_liste = (time.perf_counter() - debut) / repetitions

    debut = time.perf_counter()
    dico = construire_dictionnaire(lignes)
    temps_construction = time.perf_counter() - debut

    debut = time.perf_counter()
    for _ in range(repetitions):
        dico[(source, produit, date)]
    temps_dico = (time.perf_counter() - debut) / repetitions

    return temps_liste, temps_construction, temps_dico