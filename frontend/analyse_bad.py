import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

def formater_peripherique():
    root.destroy()
    subprocess.run(["python", "format_interface.py"])

def nettoyer_peripherique():
    label.config(text="Nettoyage en cours...")
    root.update()
    try:
        subprocess.run(["bash", "clean.sh"], capture_output=True, text=True)
    finally:
        root.update()
        root.destroy()
        subprocess.run(["python", "end_clean_interface.py"])

def quitter():
    root.destroy()
    subprocess.run(["python", "main_interface.py"])

# Création de la fenêtre principale
root = Tk()
root.title("Alerte Sécurité USB")
root.attributes('-fullscreen', True)

# Style ttk
style = ttk.Style()
style.configure('TLabel', font=("Arial", 40), padding=20)
style.configure('Red.TButton', font=("calibri", 30, "bold"), borderwidth=4, relief="raised", width=20, height=20, padding=(30, 20), foreground='black', background='#F5B7B1')   # Rouge
style.configure('Green.TButton', font=("calibri", 30, "bold"), borderwidth=4, relief="raised", width=20, height=20, padding=(30, 20), foreground='black', background='#ABEBC6')  # Vert
style.configure('Quitter.TButton', font=("calibri", 30, "bold"), borderwidth=4, relief="raised", width=20, height=20, padding=(30, 20), foreground='black', background='lightgrey')  # Gris

# Appliquer la couleur au survol
style.map('Red.TButton', background=[('active', '#EC7063')])
style.map('Green.TButton', background=[('active', '#58D68D')])
style.map('Quitter.TButton', background=[('active', 'grey')])

# Conteneur principal
frame = ttk.Frame(root, padding=50)
frame.pack(expand=True)

# Label d'alerte
label = ttk.Label(frame, text="⚠ Attention ! Un élément suspect a été détecté. ⚠", font=("Arial", 40), foreground="red", anchor="center", justify="center")
label.pack(pady=20)

# Boutons d'action
btn_format = ttk.Button(frame, text="Formater", command=formater_peripherique, style="Red.TButton")
btn_format.pack(pady=10, fill='x')

btn_clean = ttk.Button(frame, text="Nettoyer", command=nettoyer_peripherique, style="Green.TButton")
btn_clean.pack(pady=10, fill='x')

btn_quit = ttk.Button(frame, text="Quitter", command=quitter, style="Quitter.TButton")
btn_quit.pack(pady=10, fill='x')

# Lancer la boucle principale
root.mainloop()