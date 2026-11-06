from models.chargement import charger_tout
from models.nettoyage import nettoyer_tout, ecrire_journal
from models.rapprochement import rapprocher, ecarter_aberrants
from models.comparaison import comparer, exporter_comparatif
from models.synthese import victoires, ecart_moyen, top3_gains
from views import menu_view, synthese_view
from views import menu_view, synthese_view, comparatif_view
from models.panier import prix_utilisables, panier_par_enseigne, panier_optimal
from views import menu_view, synthese_view, comparatif_view, panier_view
from models.historique import charger_historique, variation_black_friday, resume_par_enseigne, mesurer_recherches
from views import menu_view, synthese_view, comparatif_view, panier_view, historique_view

def preparer_donnees():
    df = charger_tout()
    df = nettoyer_tout(df)
    df = ecarter_aberrants(rapprocher(df))
    ecrire_journal()
    tableau = comparer(df)
    exporter_comparatif(tableau)
    return df, tableau

def lancer():
    df, tableau = preparer_donnees()
    while True:
        choix = menu_view.afficher_menu()
        if choix == "1":
            comparatif_view.afficher_comparatif(tableau)
        elif choix == "2":
            synthese_view.afficher_synthese(victoires(tableau), ecart_moyen(tableau), top3_gains(tableau))
        elif choix == "3":
            prix = prix_utilisables(df)
            total_optimal, choix_articles = panier_optimal(prix)
            panier_view.afficher_panier(panier_par_enseigne(prix), total_optimal, choix_articles)
        elif choix == "4":
            h = charger_historique()
            resume = resume_par_enseigne(variation_black_friday(h))
            historique_view.afficher_black_friday(resume)
        elif choix == "5":
            t_liste, t_construction, t_dico = mesurer_recherches()
            historique_view.afficher_complexite(t_liste, t_construction, t_dico)
        elif choix == "0":
            break
        else:
            print("Choix invalide")