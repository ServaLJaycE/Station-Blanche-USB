import tkinter as tk
from tkinter import ttk
import subprocess
import os

def ejecter_usb():
    backend_dir = "/usr/share/projet/backend"  # Ou adapte dynamiquement si besoin

    log_file = os.path.join(backend_dir, "logs.txt")
    usb_mount_path_file = os.path.join(backend_dir, "usb_mount_path.txt")

    usb_mount_path = None

    # Essaie de récupérer l'ancien chemin de montage
    if os.path.exists(usb_mount_path_file):
        with open(usb_mount_path_file, "r") as f:
            path = f.read().strip()
            if os.path.ismount(path):
                usb_mount_path = path

    # Si l'ancien chemin est invalide, tente de le redétecter dynamiquement
    if usb_mount_path is None:
        result = subprocess.run(["lsblk", "-o", "MOUNTPOINT", "-nr"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if line.startswith("/media") or line.startswith("/mnt"):
                usb_mount_path = line.strip()
                break

    # Copie logs.txt sur la clé si montée
    if usb_mount_path and os.path.exists(usb_mount_path):
        subprocess.run(["cp", log_file, os.path.join(usb_mount_path, "logs.txt")])

    # Éjection
    subprocess.run(["bash", os.path.join(backend_dir, "ejectUSB.sh")])

    # Retour accueil
    root.destroy()
    subprocess.run(["python3","accueil.py"])


# Création de la fenêtre principale
root = tk.Tk()
root.title("Formatage Terminé")
root.attributes('-fullscreen', True)

def disable_escape(event):
    pass

root.bind("<Escape>", disable_escape)

# Affichage du message
success = True
message = "✅ Formatage réussi !" if success else "❌ Échec du formatage.\nVeuillez réessayer."
message_color = "green" if success else "red"

style = ttk.Style()
style.configure('TLabel', font=("Arial", 30), padding=15)
style.configure('OK.TButton', font=("calibri", 24, "bold"), borderwidth=4, relief="raised", padding=15, foreground='black', background='#ABEBC6')
style.map('OK.TButton', background=[('active', '#58D68D')])

frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

label = ttk.Label(frame, text=message, font=("Arial", 30), foreground=message_color, anchor="center", justify="center", wraplength=700)
label.pack(pady=20)

btn_ok = ttk.Button(frame, text="OK", command=ejecter_usb, style="OK.TButton")
btn_ok.pack(pady=20, fill="x")

root.mainloop()
