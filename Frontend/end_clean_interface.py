import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

def retour_accueil():
    root.destroy()

# Création de la fenêtre principale
root = Tk()
root.title("Nettoyage Terminé")
root.attributes('-fullscreen', True)

# Style ttk
style = ttk.Style()
style.configure('TLabel', font=("Arial", 40), padding=20)
style.configure('OK.TButton', font=("calibri", 30, "bold"), borderwidth=4, relief="raised", width=20, height=20, padding=(30, 20), foreground='black', background='#ABEBC6')  # Vert
style.map('OK.TButton', background=[('active', '#58D68D')])

# Conteneur principal
frame = ttk.Frame(root, padding=50)
frame.pack(expand=True)

# Label d'information (centré)
label = ttk.Label(frame, text="Nettoyage terminé.\nLes logs ont été écrits sur le périphérique USB.",
                  font=("Arial", 40), anchor="center", justify="center")
label.pack(pady=20)

# Bouton OK
btn_ok = ttk.Button(frame, text="OK", command=retour_accueil, style="OK.TButton")
btn_ok.pack(pady=20, fill="x")

# Lancer la boucle principale
root.mainloop()
