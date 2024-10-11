import tkinter as tk


#  Voici un exemple simple pour créer une fenêtre avec un bouton :
def bouton_click():
    print("Le bouton a été cliqué !")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon Application Tkinter")

# Créer un bouton
bouton = tk.Button(fenetre, text="Clique moi", command=bouton_click)
bouton.pack()




#  Tu peux aussi ajouter des étiquettes :
# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon Application Tkinter")

# Créer une étiquette
etiquette = tk.Label(fenetre, text="Bonjour, Tkinter!")
etiquette.pack()




#  Pour ajouter une entrée de texte :
def afficher_texte():
    texte = entree.get()
    print("Texte entré :", texte)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon Application Tkinter")

# Créer une entrée de texte
entree = tk.Entry(fenetre)
entree.pack()

# Créer un bouton pour soumettre le texte
bouton = tk.Button(fenetre, text="Soumettre", command=afficher_texte)
bouton.pack()

# Lancer la boucle principale
fenetre.mainloop()
