import tkinter as tk

# Création de la fenêtre principale
accueil = tk.Tk()
accueil.title("Station de Décontamination USB")
accueil.attributes('-fullscreen', True)

label = tk.Label(accueil, text="Bonjour, je suis une station de décontamination USB Insérez un périphérique", wraplength=400, font=("Arial", 12))
label.pack(pady=20)

accueil.mainloop()
