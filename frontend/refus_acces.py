import tkinter as tk
import subprocess
from tkinter import ttk

def formater_peripherique():
    root.destroy()
    subprocess.run(["python3", "format_interface.py"])  # Utilisation de python3

def ejecter_usb():
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
btn_format = ttk.Button(frame, text="Formater", command=formater_peripherique, style="Red.TButton")
btn_format.pack(pady=10, fill='x')

button_ejecter = ttk.Button(frame, text="Éjecter", command=ejecter_usb, style="Ejecter.TButton")
button_ejecter.pack(pady=10, fill='x')

# Lancer la boucle principale
root.mainloop()
