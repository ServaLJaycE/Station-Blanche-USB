import tkinter as tk
import subprocess
from tkinter import ttk
import os

# Créer la fenêtre principale
format_interface = tk.Tk()
format_interface.title("Choisir le format de la clé USB")
format_interface.attributes('-fullscreen', True)  # Mode plein écran

# Désactiver la touche "Échap" pour éviter de quitter accidentellement
def disable_escape(event):
    pass  # Ignore l'événement

format_interface.bind("<Escape>", disable_escape)

# Définition du dossier backend
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend"))

# Fonctions pour formater
def fat32():
    subprocess.run(["bash", os.path.join(backend_dir, "fat32.sh")])
    format_interface.destroy()
    subprocess.run(["python", "endFormat_interface.py"])

def ntfs():
    subprocess.run(["bash", os.path.join(backend_dir, "ntfs.sh")])
    format_interface.destroy()
    subprocess.run(["python", "endFormat_interface.py"])

def ext4():
    subprocess.run(["bash", os.path.join(backend_dir, "ext4.sh")])
    format_interface.destroy()
    subprocess.run(["python", "endFormat_interface.py"])

def quitter():
    format_interface.destroy()
    subprocess.run(["python", "main_interface.py"])

# Chargement des images avec gestion d'erreurs si elles sont manquantes
def charger_image(chemin, facteur_x=1, facteur_y=1):
    try:
        return tk.PhotoImage(file=chemin).subsample(facteur_x, facteur_y)
    except Exception:
        return None  # Retourne None si l'image est introuvable

image_windows = charger_image("images/windows.png", 12, 12)  # NTFS (Windows)
image_linux = charger_image("images/linux.png", 10, 10)  # EXT4 (Linux)
image_winlin = charger_image("images/winlin.png", 6, 6)  # FAT32 (Windows et Linux)

# Style des boutons
style = ttk.Style()
style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth=4, relief='raised', padding=(0,10))  # Ajout de padding
style.configure('Fat32.TButton', foreground='black', background='#AED6F1', padding=(0, 20))  # Bleu
style.configure('Ntfs.TButton', foreground='black', background='#ABEBC6')  # Vert
style.configure('Ext4.TButton', foreground='black', background='#F5B7B1')  # Rouge
style.configure('Quitter.TButton', foreground='black', background='lightgrey')  # Gris

# Couleur des boutons au survol
style.map('Fat32.TButton', background=[('active', '#5DADE2')])
style.map('Ntfs.TButton', background=[('active', '#58D68D')])
style.map('Ext4.TButton', background=[('active', '#EC7063')])
style.map('Quitter.TButton', background=[('active', 'grey')])

# Titre
label_format = tk.Label(
    format_interface,
    text="Choisissez le format de la clé USB :",
    font=("Arial", 30),
    anchor="center"
)
label_format.place(relx=0.5, rely=0.2, anchor="center")

# Conteneur des boutons avec espacements
button_frame = ttk.Frame(format_interface)
button_frame.place(relx=0.5, rely=0.5, anchor="center")

# Boutons de formatage avec un espacement plus marqué
button_fat32 = ttk.Button(button_frame, text="FAT32", image=image_winlin, compound="right", command=fat32, style="Fat32.TButton")
button_fat32.pack(side=tk.LEFT, padx=6, pady=5)

button_ntfs = ttk.Button(button_frame, text="NTFS", image=image_windows, compound="right", command=ntfs, style="Ntfs.TButton")
button_ntfs.pack(side=tk.LEFT, padx=6, pady=5)

button_ext4 = ttk.Button(button_frame, text="EXT4", image=image_linux, compound="right", command=ext4, style="Ext4.TButton")
button_ext4.pack(side=tk.LEFT, padx=6, pady=5)

# Bouton Quitter avec un meilleur espacement
button_quitter = ttk.Button(format_interface, text="Quitter", command=quitter, style="Quitter.TButton")
button_quitter.place(relx=0.5, rely=0.75, anchor="center")

# Lancer l'interface
format_interface.mainloop()
