import tkinter as tk
import subprocess
from tkinter import ttk
import os

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend"))

def ejecter_usb():
    #! A RAJOUTER POUR CHAQUE EJECTER
    # Chemin du fichier de logs
    log_file = "/usr/share/projet/backend/logs.txt"
    # Chemin de montage de la clé USB
    usb_mount_path_file = "/usr/share/projet/backend/usb_mount_path.txt"

    # Vérifie si le fichier contenant le chemin de montage existe
    if os.path.exists(usb_mount_path_file):
        with open(usb_mount_path_file, "r") as f:
            usb_mount_path = f.read().strip()

        # Copie le fichier de logs sur la clé USB
        if os.path.exists(usb_mount_path):
            subprocess.run(["cp", log_file, os.path.join(usb_mount_path, "logs.txt")])
        #! A RAJOUTER POUR CHAQUE EJECTER

    process = subprocess.Popen(["bash", os.path.join(backend_dir, "ejectUSB.sh")])
    process.wait()
    root.destroy()
    subprocess.run(["python3", "accueil.py"])  # Utilisation de python3

# Création de la fenêtre principale
root = tk.Tk()
root.title("Alerte Sécurité USB")
root.attributes('-fullscreen', True)  # Mode plein écran

# Désactiver la touche "Échap" pour éviter de quitter accidentellement
def disable_escape(event):
    pass  # Ignore l'événement

root.bind("<Escape>", disable_escape)

# Style ttk
style = ttk.Style()
style.configure('TLabel', font=("Arial", 30), padding=15)
style.configure('Red.TButton', font=("calibri", 24, "bold"), borderwidth=4, relief="raised", padding=15, foreground='black', background='#F5B7B1')  # Rouge
style.configure('Ejecter.TButton', font=("calibri", 24, "bold"), borderwidth=4, relief="raised", padding=15, foreground='black', background='lightgrey')  # Gris

# Appliquer la couleur au survol
style.map('Red.TButton', background=[('active', '#EC7063')])
style.map('Ejecter.TButton', background=[('active', 'grey')])

# Conteneur principal
frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

# Label d'alerte
label = ttk.Label(
    frame,
    text="⚠ La clé est corrompue !\nAccès interdit à la station de décontamination. ⚠",
    font=("Arial", 30),
    foreground="red",
    anchor="center",
    justify="center",
    wraplength=700
)
label.pack(pady=20)

# Boutons d'action

button_ejecter = ttk.Button(frame, text="Éjecter", command=ejecter_usb, style="Ejecter.TButton")
button_ejecter.pack(pady=10, fill='x')

# Lancer la boucle principale
root.mainloop()
