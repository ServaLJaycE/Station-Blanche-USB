import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

def retour_accueil():
    root.destroy()

# Création de la fenêtre principale
root = Tk()
root.title("Formatage Terminé")
root.attributes('-fullscreen', True)

# Style ttk
style = ttk.Style()
style.configure('TLabel', font=("Arial", 40), padding=20)
style.configure('OK.TButton', font=("calibri", 30, "bold"), borderwidth=4, relief="raised", width=20, height=20, padding=(30, 20), foreground='black', background='#ABEBC6')  # Vert
style.map('OK.TButton', background=[('active', '#58D68D')])

# Ajouter un bouton pour quitter le mode plein écran
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

root.bind('<Escape>', exit_fullscreen)

# Détermination du message et de la couleur selon le succès du formatage
success = True  # À remplacer par la vraie variable du succès
message = "✅ Formatage réussi !" if success else "❌ Échec du formatage.\nVeuillez réessayer."
message_color = "green" if success else "red"

# Conteneur principal
frame = ttk.Frame(root, padding=50)
frame.pack(expand=True)

# Label d'information
label = ttk.Label(frame, text=message, font=("Arial", 40), foreground=message_color, anchor="center", justify="center")
label.pack(pady=20)

# Bouton OK
btn_ok = ttk.Button(frame, text="OK", command=retour_accueil, style="OK.TButton")
btn_ok.pack(pady=20, fill="x")

# Lancer la boucle principale
root.mainloop()
