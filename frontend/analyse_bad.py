import tkinter as tk
import subprocess
from tkinter import ttk
import os

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend"))

def formater_peripherique():
    root.destroy()
    subprocess.run(["python3", "format_interface.py"])

def nettoyer_peripherique():
    label.config(text="Nettoyage en cours...")
    root.update()
    try:
        subprocess.run(["bash", "clean.sh"], capture_output=True, text=True)
    finally:
        root.update()
        root.destroy()
        subprocess.run(["python3", "end_clean_interface.py"])

def ejecter():
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
    font=("Arial", 25),
    foreground="red",
    anchor="center",
    justify="center",
    wraplength=700
)
label.pack(pady=15)

# Boutons d'action
btn_format = ttk.Button(frame, text="Formater", command=formater_peripherique, style="Red.TButton")
btn_format.pack(pady=10, fill='x')

btn_clean = ttk.Button(frame, text="Nettoyer", command=nettoyer_peripherique, style="Green.TButton")
btn_clean.pack(pady=10, fill='x')

btn_eject = ttk.Button(frame, text="Ejecter", command=ejecter, style="Ejecter.TButton")
btn_eject.pack(pady=10, fill='x')

# Lancer la boucle principale
root.mainloop()
