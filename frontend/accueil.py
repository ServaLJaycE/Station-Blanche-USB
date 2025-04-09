import tkinter as tk
import subprocess
import os
import time


def verifier_detection():
    # Chemins vers les fichiers générés par detect.sh et detect_mount.sh
    usb_device_path = "/usr/share/projet/backend/usb_device_path.txt"
    #usb_mount_path = "/usr/share/projet/Backend/usb_mount_path.txt"

    # Vérifie si le fichier existe
    if os.path.exists(usb_device_path) :#and os.path.exists(usb_mount_path):
        root.destroy()
        subprocess.run(["python3", "main_interface.py"])
    else:
        root.after(2000, verifier_detection)


# Crée la fenêtre principale
root = tk.Tk()
root.title("Station de Décontamination USB")
root.attributes('-fullscreen', True)

# Message d'accueil
label = tk.Label(
    root,
    text="Bonjour, je suis une station de décontamination USB.\nInsérez un périphérique.",
    font=("Arial", 30),
    wraplength=700,
    justify="center"
)
label.pack(pady=20)
label.place(relx=0.5, rely=0.5, anchor="center")  # Centre le conteneur

# Lancer detect.sh et detect_mount.sh en parallèle
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend"))
subprocess.Popen(["bash", os.path.join(backend_dir, "detect.sh")])
subprocess.Popen(["bash", os.path.join(backend_dir, "detect_mount.sh")])

# Vérifie périodiquement si les fichiers nécessaires ont été générés
root.after(2000, verifier_detection)

# Lancer la boucle principale
root.mainloop()