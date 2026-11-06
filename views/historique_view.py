def afficher_black_friday(resume):
    print("\n--- Black Friday (24 au 30 novembre 2025) comparé au prix moyen de l'année ---")
    for enseigne, variation in resume.items():
        if variation < 0:
            print(f"   {enseigne} : baisse de {abs(variation)} %")
        else:
            print(f"   {enseigne} : hausse de {variation} %")
    print("\nAttention : pour Comptoir Ivoire, l'historique donne le prix catalogue, sans la remise.")

def afficher_complexite(t_liste, t_construction, t_dico):
    print("\n--- Complexité : retrouver un prix dans 20 876 lignes ---")
    print(f"   Liste : {t_liste * 1000:.3f} ms par recherche")
    print(f"   Dictionnaire : {t_construction * 1000:.1f} ms de construction (une seule fois), "
          f"puis {t_dico * 1_000_000:.2f} microsecondes par recherche")
    print(f"   Le dictionnaire est environ {t_liste / t_dico:.0f} fois plus rapide pour chercher.")
    print(f"   Il devient rentable à partir d'environ {t_construction / t_liste:.0f} recherches.")
    print("\n   Liste : on parcourt les lignes une à une, donc le temps grandit avec la taille des données (O(n)).")
    print("   Dictionnaire : Python va directement à la bonne case, quelle que soit la taille (O(1) en moyenne).")