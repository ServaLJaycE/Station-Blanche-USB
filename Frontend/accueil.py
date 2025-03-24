import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

# Création de la fenêtre principale
accueil = Tk()
accueil.title("Station de Décontamination USB")
accueil.attributes('-fullscreen', True)

# Style ttk
style = ttk.Style()
style.configure('TLabel', font=("Arial", 30), padding=20)

# Ajouter un bouton pour quitter le mode plein écran
def exit_fullscreen(event=None):
    accueil.attributes('-fullscreen', False)

accueil.bind('<Escape>', exit_fullscreen)

# Conteneur principal
frame = ttk.Frame(accueil, padding=50)
frame.pack(expand=True)

# Label d'accueil
label = ttk.Label(frame, text="Bonjour, je suis une station de décontamination USB.\nInsérez un périphérique.", wraplength=800, font=("Arial", 40))
label.pack(pady=20)

# Lancer la boucle principale
accueil.mainloop()