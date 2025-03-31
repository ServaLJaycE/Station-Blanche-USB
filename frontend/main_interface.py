import tkinter as tk
import subprocess
from tkinter import ttk
import os

# Création de la fenêtre principale
menu = tk.Tk()
menu.title("Station de décontamination USB")
menu.attributes('-fullscreen', True)  # Mode plein écran forcé

# Désactivation de la touche "Échap" pour éviter de quitter accidentellement
def disable_escape(event):
    pass  # Ignore l'événement

menu.bind("<Escape>", disable_escape)

# Définition du dossier Backend
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend"))

# Fonctions associées aux boutons
def analyser_usb():
    label.config(text="Analyse de la clé USB en cours...", foreground="blue")
    menu.update_idletasks()  # Mise à jour de l'interface
    subprocess.Popen(["bash", os.path.join(backend_dir, "pre_analyse.sh")])

def formater_usb():
    menu.destroy()
    subprocess.run(["python", "format_interface.py"])

def ejecter_usb():
    process = subprocess.Popen(["bash", os.path.join(backend_dir, "ejectUSB.sh")])
    process.wait()
    menu.destroy()
    subprocess.run(["python", "accueil.py"])

def quitter():
    menu.quit()

# Style des boutons
style = ttk.Style()
style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth=4, relief='raised', padding=15)
style.configure('Analyser.TButton', foreground='black', background='#AED6F1')  # Bleu
style.configure('Formater.TButton', foreground='black', background='#ABEBC6')  # Vert
style.configure('Ejecter.TButton', foreground='black', background='#F5B7B1')  # Rouge
style.configure('Quitter.TButton', foreground='black', background='lightgrey')  # Gris

# Couleurs des boutons au survol
style.map('Analyser.TButton', background=[('active', '#5DADE2')])
style.map('Formater.TButton', background=[('active', '#58D68D')])
style.map('Ejecter.TButton', background=[('active', '#EC7063')])
style.map('Quitter.TButton', background=[('active', 'grey')])

# Label de titre
label = ttk.Label(
    menu,
    text="Bienvenue sur la station de décontamination USB !",
    font=("Arial", 30),
    anchor="center",
    wraplength = 700,
    justify = "center"
)
label.place(relx=0.5, rely=0.2, anchor="center")

# Conteneur des boutons
button_frame = ttk.Frame(menu)
button_frame.place(relx=0.5, rely=0.5, anchor="center")

# Boutons
button_analyser = ttk.Button(button_frame, text="Analyser", command=analyser_usb, style="Analyser.TButton")
button_analyser.pack(side=tk.LEFT, padx=10)

button_formater = ttk.Button(button_frame, text="Formater", command=formater_usb, style="Formater.TButton")
button_formater.pack(side=tk.LEFT, padx=10)

button_ejecter = ttk.Button(button_frame, text="Éjecter", command=ejecter_usb, style="Ejecter.TButton")
button_ejecter.pack(side=tk.LEFT, padx=10)

# Bouton Quitter
button_quitter = ttk.Button(menu, text="Quitter", command=quitter, style="Quitter.TButton")
button_quitter.place(relx=0.5, rely=0.75, anchor="center")

# Lancer la boucle principale
menu.mainloop()
