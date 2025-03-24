import tkinter as tk
import subprocess
#from format_interface import ouvrir_format_page


# Fonctions associées aux boutons
def analyser_usb():
    label.config(text="Analyse de la clé USB en cours...")

def formater_usb():
    #format_interface.ouvrir_format_page()
    subprocess.run(["python", "format_interface.py"])
    menu.destroy()


def ejecter_usb():
    label.config(text="Clé USB éjectée en toute sécurité.")

# bouton pour quitter
def quitter() :
    menu.quit()

# Créer la fenêtre principale
menu = tk.Tk()
menu.title("Station de décontamination USB")

# Configurer le plein écran
menu.attributes('-fullscreen', True)

# Ajouter un bouton pour quitter le mode plein écran
def exit_fullscreen(event=None):
    menu.attributes('-fullscreen', False)

menu.bind('<Escape>', exit_fullscreen)


# Ajouter un label pour le titre
label = tk.Label(menu, text="Bienvenue sur la station de décontamination USB !", font=("Arial", 20))
label.pack(pady=20)

# Créer un conteneur pour les boutons côte à côte
button_frame = tk.Frame(menu)
button_frame.pack(pady=20)

# Ajouter les boutons avec leurs commandes dans le conteneur
button_analyser = tk.Button(button_frame, text="Analyser", command=analyser_usb, font=("Arial", 16), bg="lightblue", width=15, height=3)
button_analyser.pack(side=tk.LEFT, padx=15)

button_formater = tk.Button(button_frame, text="Formater", command=formater_usb, font=("Arial", 16), bg="lightgreen", width=15, height=3)
button_formater.pack(side=tk.LEFT, padx=15)

button_ejecter = tk.Button(button_frame, text="Éjecter", command=ejecter_usb, font=("Arial", 16), bg="lightcoral", width=15, height=3)
button_ejecter.pack(side=tk.LEFT, padx=15)

# Ajouter un bouton pour quitter l'application
button_quitter = tk.Button(menu, text="Quitter", command=quitter, font=("Arial", 16), bg="lightgrey", width=15, height=3)
button_quitter.pack(pady=20)

# Lancer la boucle principale
menu.mainloop()
