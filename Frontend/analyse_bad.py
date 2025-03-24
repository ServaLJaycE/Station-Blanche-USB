import tkinter as tk

def formater_peripherique():
    label.config(text="Formatage en cours...")
    # Ajoutez ici le code pour formater le périphérique

def nettoyer_peripherique():
    label.config(text="Nettoyage en cours...")
    # Ajoutez ici le code pour nettoyer les fichiers infectés

# Création de la fenêtre principale
root = tk.Tk()
root.title("Alerte Sécurité USB")
root.geometry("400x250")

label = tk.Label(root, text="Attention ! Un élément suspect a été détecté.", font=("Arial", 12), fg="red")
label.pack(pady=20)

btn_format = tk.Button(root, text="Formater", command=formater_peripherique, font=("Arial", 12), fg="white", bg="red")
btn_format.pack(pady=5)

btn_clean = tk.Button(root, text="Nettoyer", command=nettoyer_peripherique, font=("Arial", 12), fg="white", bg="green")
btn_clean.pack(pady=5)

root.mainloop()