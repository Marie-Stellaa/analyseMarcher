from pathlib import Path
import pandas as pd
from models.nettoyage import journal
from models.comparaison import exporter_comparatif

DOSSIER = Path("exports")

def preparer_dossier():
    DOSSIER.mkdir(exist_ok=True)

def exporter_historique(variation):
    table = variation.round(1).reset_index()
    table.columns = ["enseigne", "produit_id", "variation_pct"]
    table.to_csv(DOSSIER / "historique_black_friday.csv", index=False, encoding="utf-8-sig")

def exporter_journal():
    pd.DataFrame({"message": journal}).to_csv(
        DOSSIER / "journal_nettoyage.csv", index=False, encoding="utf-8-sig")

def exporter_comparatif_csv(tableau):
    exporter_comparatif(tableau, DOSSIER / "comparatif_prix.csv")

def exporter_panier(par_enseigne, total_optimal, choix_articles):
    lignes = []
    for enseigne, r in par_enseigne.items():
        if r["manquants"]:
            statut = "incomplet"
            detail = "manque " + ", ".join(r["manquants"]) + " (total partiel)"
        else:
            statut = "complet"
            detail = ""
        lignes.append({"enseigne": enseigne, "total_fcfa": r["total"],
                       "statut": statut, "detail": detail})
    detail = ", ".join(f"{p}: {e}" for p, e in choix_articles.items())
    lignes.append({"enseigne": "Chaque article au moins cher", "total_fcfa": total_optimal,
                   "statut": "complet", "detail": detail})
    pd.DataFrame(lignes).to_csv(DOSSIER / "panier.csv", index=False, encoding="utf-8-sig")

def exporter_synthese(victoires, ecarts, top3):
    with open(DOSSIER / "synthese.txt", "w", encoding="utf-8") as f:
        f.write("Nombre de fois où chaque enseigne est la moins chère\n")
        for e, nb in victoires.items():
            f.write(f"  {e} : {nb}\n")
        f.write("\nÉcart moyen par rapport au prix le plus bas\n")
        for e, v in ecarts.items():
            f.write(f"  {e} : {v['fcfa']} FCFA ({v['pct']} %)\n")
        f.write("\nLes 3 produits où il y a le plus à gagner\n")
        for _, l in top3.iterrows():
            f.write(f"  {l['nom']} : {l['ecart_FCFA']:.0f} FCFA ({l['ecart_pct']} %), "
                    f"le moins cher : {l['moins_chere']}\n")

def exporter_complexite(t_liste, t_construction, t_dico):
    with open(DOSSIER / "complexite.txt", "w", encoding="utf-8") as f:
        f.write("Retrouver un prix dans 20 876 lignes\n")
        f.write(f"  Liste : {t_liste * 1000:.3f} ms par recherche (O(n))\n")
        f.write(f"  Dictionnaire : {t_construction * 1000:.1f} ms de construction, "
                f"puis {t_dico * 1_000_000:.2f} microsecondes par recherche (O(1) en moyenne)\n")