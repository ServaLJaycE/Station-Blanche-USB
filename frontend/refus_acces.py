import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

def formater_peripherique():
    root.destroy()
    subprocess.run(["python", "format_interface.py"])

def ejecter_usb():
    root.destroy()
    subprocess.run(["python", "accueil.py"])



# Création de la fenêtre principale
root = Tk()
root.title("Alerte Sécurité USB")
root.attributes('-fullscreen', True)

# Style ttk
style = ttk.Style()
style.configure('TLabel', font=("Arial", 40), padding=20)
style.configure('Red.TButton', font=("calibri", 30, "bold"), borderwidth=4, relief="raised", width=20, height=20, padding=(30, 20), foreground='black', background='#F5B7B1')  # Rouge
style.configure('Ejecter.TButton', font=("calibri", 30, "bold"), borderwidth=4, relief="raised", width=20, height=20, padding=(30, 20), foreground='black', background='lightgrey')  # Gris

# Appliquer la couleur au survol
style.map('Red.TButton', background=[('active', '#EC7063')])
style.map('Ejecter.TButton', background=[('active', 'grey')])

# Conteneur principal
frame = ttk.Frame(root, padding=50)
frame.pack(expand=True)

# Label d'alerte
label = ttk.Label(frame, text="⚠ La clé est corrompue !\nAccès interdit à la station de décontamination.⚠", font=("Arial", 40), foreground="red", anchor="center", justify="center")
label.pack(pady=20)

# Boutons d'action
btn_format = ttk.Button(frame, text="Formater", command=formater_peripherique, style="Red.TButton")
btn_format.pack(pady=10, fill='x')

button_ejecter = ttk.Button(frame, text="Éjecter", command=ejecter_usb, style="Ejecter.TButton")
button_ejecter.pack(pady=10, fill='x')


# Lancer la boucle principale
root.mainloop()