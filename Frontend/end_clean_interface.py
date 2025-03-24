import tkinter as tk

def retour_accueil():
    root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Nettoyage Terminé")
root.geometry("400x200")

label = tk.Label(root, text="Nettoyage terminé. Les logs ont été écrits sur le périphérique USB.", font=("Arial", 12), wraplength=350)
label.pack(pady=20)

btn_ok = tk.Button(root, text="OK", command=retour_accueil, font=("Arial", 12))
btn_ok.pack(pady=10)

root.mainloop()
