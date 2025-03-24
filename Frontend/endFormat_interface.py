import tkinter as tk

def retour_accueil():
    root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Formatage Terminé")
root.geometry("400x200")

# Message de réussite ou d'échec du formatage (modifiable selon le résultat réel)
success = True  # Remplacez par une variable déterminant le succès ou l'échec
message = "Formatage réussi !" if success else "Échec du formatage. Veuillez réessayer."

label = tk.Label(root, text=message, font=("Arial", 12), wraplength=350, fg="green" if success else "red")
label.pack(pady=20)

btn_ok = tk.Button(root, text="OK", command=retour_accueil, font=("Arial", 12))
btn_ok.pack(pady=10)

root.mainloop()
