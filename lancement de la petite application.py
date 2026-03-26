import tkinter as tk

#Création de la fenêtre
fenetre = tk.Tk()                                                       #Créer la fenêtre
fenetre.title("___ Suivi de santé quotidien ___")
fenetre.geometry("1280x1024")

#Label pour l'eau
label_eau = tk.Label(fenetre,text=" Verre d'eau bus ?")
label_eau.pack()
champ_eau= tk.Entry(fenetre)
champ_eau.pack()

#Label pour le sommeil
label_sommeil = tk.Label(fenetre,text=" Combien d'heure avez vous ?")
label_sommeil.pack()
champ_sommeil= tk.Entry(fenetre)
champ_sommeil.pack()

#Label pour l'humeur
label_humeur = tk.Label(fenetre,text="Nombre d'heures dormi ?")
label_humeur.pack()
champ_humeur= tk.Entry(fenetre)
champ_humeur.pack()

#Label pour les pas 
label_pas = tk.Label(fenetre,text="Nombre de pas effectué ?")
label_pas.pack()
champ_pas= tk.Entry(fenetre)
champ_pas.pack()

#Label pour l'activité
label_activite = tk.Label(fenetre,text=" Quel est l'activité effectué?")
label_activite.pack()
champ_activite= tk.Entry(fenetre)
champ_activite.pack()

#Label pour la durée
label_duree = tk.Label(fenetre, text= "Quel est la durée de l'activité ?")
label_duree.pack()
champ_duree = tk.Entry(fenetre)
champ_duree.pack()

bouton = tk.Button(fenetre, text="Sauvegarder")
bouton.pack()

#Ouverture de la fenêtre
fenetre.mainloop()