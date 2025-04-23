import tkinter as tk
import subprocess
from tkinter import ttk
import os

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend"))

def formater_peripherique():
    root.destroy()
    subprocess.run(["python3", "format_interface.py"])

def nettoyer_peripherique():
    label.config(text="Nettoyage en cours...")
    root.update()
    try:
        subprocess.run(["bash", os.path.join(backend_dir, "clean.sh")], capture_output=True, text=True)
    finally:
        root.update()
        root.destroy()
        subprocess.run(["python3", "end_clean_interface.py"])

def ejecter():
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
    subprocess.run(["python", "accueil.py"])

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
style.configure('Red.TButton', font=("calibri", 24, "bold"), borderwidth=4, relief="raised", padding=15, foreground='black', background='#F5B7B1')   # Rouge
style.configure('Green.TButton', font=("calibri", 24, "bold"), borderwidth=4, relief="raised", padding=15, foreground='black', background='#ABEBC6')  # Vert
style.configure('Ejecter.TButton', font=("calibri", 24, "bold"), borderwidth=4, relief="raised", padding=15, foreground='black', background='lightgrey')  # Gris

# Appliquer la couleur au survol
style.map('Red.TButton', background=[('active', '#EC7063')])
style.map('Green.TButton', background=[('active', '#58D68D')])
style.map('Quitter.TButton', background=[('active', 'grey')])

# Conteneur principal
frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

# Label d'alerte
label = ttk.Label(
    frame,
    text="⚠ Attention ! Un élément suspect a été détecté. ⚠",
    font=("Arial", 30),
    foreground="red",
    anchor="center",
    justify="center",
    wraplength=700
)
label.pack(pady=5)

# Boutons d'action
btn_format = ttk.Button(frame, text="Formater", command=formater_peripherique, style="Red.TButton")
btn_format.pack(pady=10, fill='x')

btn_clean = ttk.Button(frame, text="Nettoyer", command=nettoyer_peripherique, style="Green.TButton")
btn_clean.pack(pady=10, fill='x')

btn_eject = ttk.Button(frame, text="Ejecter", command=ejecter, style="Ejecter.TButton")
btn_eject.pack(pady=10, fill='x')

# Lancer la boucle principale
root.mainloop()
