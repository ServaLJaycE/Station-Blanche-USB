import tkinter as tk
import subprocess
from tkinter import ttk
import os

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend"))

def retour_accueil():
    process = subprocess.Popen(["bash", os.path.join(backend_dir, "hash.sh")])
    process.wait()
    root.destroy()
    subprocess.run(["python3", "main_interface.py"])  # Utilisation de python3

# Création de la fenêtre principale
root = tk.Tk()
root.title("Analyse USB")
root.attributes('-fullscreen', True)  # Mode plein écran

# Désactiver la touche "Échap" pour éviter de quitter accidentellement
def disable_escape(event):
    pass  # Ignore l'événement

root.bind("<Escape>", disable_escape)

# Style ttk
style = ttk.Style()
style.configure('TLabel', font=("Arial", 30), padding=15)
style.configure('OK.TButton', font=("calibri", 24, "bold"), borderwidth=4, relief="raised", padding=15, foreground='black', background='#ABEBC6')  # Vert
style.map('OK.TButton', background=[('active', '#58D68D')])

# Conteneur principal
frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

# Label d'information
label = ttk.Label(
    frame,
    text="Analyse terminée :\nAucun virus détecté !",
    font=("Arial", 30),
    anchor="center",
    justify="center",
    wraplength=700
)
label.pack(pady=20)

# Bouton OK
btn_ok = ttk.Button(frame, text="OK", command=retour_accueil, style="OK.TButton")
btn_ok.pack(pady=20, fill="x")

# Lancer la boucle principale
root.mainloop()
