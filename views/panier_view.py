from models.panier import PANIER
from views.comparatif_view import formater_prix

def afficher_panier(par_enseigne, total_optimal, choix_articles):
    print("\n--- Panier de rentrée ---")
    print("Contenu : " + ", ".join(f"{q} x {p}" for p, q in PANIER.items()))

    print("\nPrix du panier dans chaque enseigne :")
    for enseigne, resultat in par_enseigne.items():
        if resultat["manquants"]:
            manquants = ", ".join(resultat["manquants"])
            print(f"   {enseigne} : panier incomplet, il manque {manquants} "
                  f"(total partiel : {formater_prix(resultat['total'])})")
        else:
            print(f"   {enseigne} : {formater_prix(resultat['total'])}")

    print("\nEn achetant chaque article là où il est le moins cher :")
    for produit, enseigne in choix_articles.items():
        print(f"   {produit} (x{PANIER[produit]}) : {enseigne}")
    print(f"   Total : {formater_prix(total_optimal)}")