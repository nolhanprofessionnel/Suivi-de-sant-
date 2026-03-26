import json                                     #Bibliothèque json permet de stocker des données de façon organisé
import os                                       #Bibliothèque os permet de vérifier si un fichier existe déjà
from datetime import date                       #Bibliothèque datetime permet de savoir automatiquement la date qu'on est 

def sauvegarder_jour(eau,sommeil,humeur,pas,activite, duree):
    #Fonction utiliser dans le programme
    def moyenne(L,cle):
        m=0
        for e in L:
            m=m+e[cle]
        return m/len(L)






    if os.path.exists("semaine_actuelle.json"):                #Vérification si le fichier demandé existe 
        with open("semaine_actuelle.json","r") as fichier:
            historique = json.load(fichier)
    else:
        historique = []

    #Demande d'information pour le suivi de santé
    print("\n === Suivi de santé du jour ===")
    sante_du_jour = {
        "date": str(date.today()),
        "eau": eau,
        "sommeil": sommeil,
        "humeur": humeur,
        "pas":pas,
        "activite": activite,
        "duree": duree,
    }
    historique.append(sante_du_jour)

    #Vérification des objectifs et affichage
    print(f"\n Vous avez bus {eau} verre d'eau aujourd'hui.")
    if eau<6:
        print("___ Alerte d'hydratation ___")

    print(f"\n Vous avez dormi {sommeil} heures.")
    if sommeil<7:
        print("___ Alerte de sommeil ___")

    print(f"\n Votre humeur est de {humeur} sur 10")
    if humeur <4:
        print("___ Alerte sur votre humeur ___")
    elif humeur>=4 and humeur<=7:
        print("___ Votre humeur est encourageante ___")
    else:
        print("___ Votre humeur est incroyable ___")

    print("\n === Fin du suivi de santé ===")

    #Création d'un fichier de sauvegarder
    with open("semaine_actuelle.json","w") as fichier:
        json.dump(historique, fichier)
    print("Données sauvegardées !")

    print("\n === Bilan de la semaine ===")
    for i in range (0,len(historique)):
        print(f"Jour {i+1} - Eau         : {'█' * historique[i]['eau']}")               #'█' caractère particulier
        print(f"Jour {i+1} - Sommeil     : {'█' * int(historique[i]['sommeil'])}")
        print(f"Jour {i+1} - Humeur      : {'█' * historique[i]['humeur']}")


    if len(historique) == 7:
        #Création de la moyenne d'eau
        moy_eau=moyenne(historique,'eau')

        #Création moyenne sommeil
        moy_sommeil=moyenne(historique,'sommeil')

        #Création moyenne humeur
        moy_humeur=moyenne(historique,'humeur')

        #Création du dictionnaire pour le bilan de la semaine
        bilan_semaine={
            "date": str(date.today()),
            "moyenne_eau": moy_eau,
            "moyenne_sommeil": moy_sommeil,
            "moyenne_humeur": moy_humeur,
        }

        if os.path.exists("suivi_mois.json"):                #Vérification si le fichier demandé existe 
            with open("suivi_mois.json","r") as fichier:
                precedent=json.load(fichier)
        else:
            precedent = []

        precedent.append(bilan_semaine)                                 #Ecrire le bilan de la semaine dans la liste precedent

        with open("suivi_mois.json","w") as fichier:
            json.dump(precedent, fichier)
        print("Données sauvegardées !")

        print("Semaine complète !")

        with open("semaine_actuelle.json","w") as fichier:                  #Réinitialiser la semaine qu'on vient de complété
            json.dump([], fichier)