def afficher_synthese(victoires, ecarts, top3):
    print("\n--- Combien de fois chaque enseigne est la moins chère ---")
    for enseigne, nb in victoires.items():
        print(f"{enseigne} : {nb}")

    print("\n--- Écart moyen par rapport au prix le plus bas ---")
    for enseigne, e in ecarts.items():
        print(f"{enseigne} : {e['fcfa']} FCFA ({e['pct']} %)")

    print("\n--- Les 3 produits où il y a le plus à gagner ---")
    for _, ligne in top3.iterrows():
        print(f"{ligne['nom']} : {ligne['ecart_FCFA']:.0f} FCFA ({ligne['ecart_pct']} %), le moins cher : {ligne['moins_chere']}")