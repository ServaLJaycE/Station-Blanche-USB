import tkinter as tk

def retour_accueil():
    root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Analyse USB")
root.geometry("400x200")

label = tk.Label(root, text="Analyse terminée : Aucun virus détecté !", font=("Arial", 12))
label.pack(pady=20)

btn_ok = tk.Button(root, text="OK", command=retour_accueil, font=("Arial", 12))
btn_ok.pack(pady=10)

root.mainloop()
