import tkinter as tk
import subprocess
import os
import time

from django.template.defaultfilters import center


def verifier_detection():
    # Chemin vers le fichier contenant le chemin du périphérique
    usb_device_path = "/usr/share/Backend/usb_device_path.txt"

    # Vérifie si le fichier existe
    if os.path.exists(usb_device_path):
        root.destroy()
        subprocess.run(["python3", "main_interface.py"])
    else:
        root.after(2000, verifier_detection)

# Crée la fenêtre principale
root = tk.Tk()
root.title("Station de Décontamination USB")
root.attributes('-fullscreen', True)

label = tk.Label(root, text="Bonjour, je suis une station de décontamination USB.\nInsérez un périphérique.", font=("Arial", 30))
label.pack(pady=20)
label.place(relx=0.5, rely=0.5, anchor="center")  # Centre le conteneur


subprocess.Popen(["bash", "/usr/share/Backend/detect.sh"])

root.after(2000, verifier_detection)

root.mainloop()