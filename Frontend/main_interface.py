import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *


# Fonctions associées aux boutons
def analyser_usb():
    label.config(text="Analyse de la clé USB en cours...")

def formater_usb():
    menu.destroy()
    subprocess.run(["python", "format_interface.py"])

def ejecter_usb():
    menu.destroy()
    subprocess.run(["python", "accueil.py"])

# bouton pour quitter
def quitter() :
    menu.quit()

# Créer la fenêtre principale
menu = Tk()
menu.title("Station de décontamination USB")

# style
style = ttk.Style() 
style.configure('TButton', font = ('calibri', 30, 'bold'), borderwidth = '4', relief = 'raised', width = 20, height = 20, padding=(30, 20))

style.configure('Analyser.TButton', foreground='black', background='#AED6F1')   # Bleu
style.configure('Formater.TButton', foreground='black', background='#ABEBC6')   # Vert
style.configure('Ejecter.TButton', foreground='black', background='#F5B7B1')    # Rouge
style.configure('Quitter.TButton', foreground='black', background='lightgrey')    # Gris

# 🔹 Appliquer la couleur au survol avec map()
style.map('Analyser.TButton', background=[('active', '#5DADE2')]) 
style.map('Formater.TButton', background=[('active', '#58D68D')])  
style.map('Ejecter.TButton', background=[('active', '#EC7063')])  
style.map('Quitter.TButton', background=[('active', 'grey')])  

# Configurer le plein écran
menu.attributes('-fullscreen', True)

# Ajouter un bouton pour quitter le mode plein écran
def exit_fullscreen(event=None):
    menu.attributes('-fullscreen', False)

menu.bind('<Escape>', exit_fullscreen)


# Ajouter un label pour le titre
label = ttk.Label(menu, text="Bienvenue sur la station de décontamination USB !", font=("Arial", 40))
label.pack(pady=20)
label.place(relx=0.5, rely=0.3, anchor="center")  


# Créer un conteneur pour les boutons côte à côte
button_frame = ttk.Frame(menu)
button_frame.pack(pady=20)

button_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centre le conteneur


# Ajouter les boutons avec leurs commandes dans le conteneur
button_analyser = ttk.Button(button_frame, text="Analyser", command=analyser_usb, style="Analyser.TButton")
button_analyser.pack(side=tk.LEFT, padx=15)

button_formater = ttk.Button(button_frame, text="Formater", command=formater_usb, style="Formater.TButton")
button_formater.pack(side=tk.LEFT, padx=15)

button_ejecter = ttk.Button(button_frame, text="Éjecter", command=ejecter_usb, style="Ejecter.TButton")
button_ejecter.pack(side=tk.LEFT, padx=15)

# Ajouter un bouton pour quitter l'application
button_quitter = ttk.Button(menu, text="Quitter", command=quitter, style="Quitter.TButton")
button_quitter.pack(pady=20)
button_quitter.place(relx=0.5, rely=0.65, anchor="center")  

# Lancer la boucle principale
menu.mainloop()
