import tkinter as tk
import subprocess

def formater_peripherique():
    root.destroy()
    subprocess.run(["python", "format_interface.py"])

def nettoyer_peripherique():
    #script pour nettoyer les fichiers infectés
    label.config(text="Nettoyage en cours...")
    root.destroy()
    subprocess.run(["python", "end_clean_interface.py"])
    


def quitter():
    root.destroy()
    subprocess.run(["python", "main_interface.py"])

# Création de la fenêtre principale
root = tk.Tk()
root.title("Alerte Sécurité USB")
root.attributes('-fullscreen', True)

label = tk.Label(root, text="Attention ! Un élément suspect a été détecté.", font=("Arial", 12), fg="red")
label.pack(pady=20)

btn_format = tk.Button(root, text="Formater", command=formater_peripherique, font=("Arial", 12), fg="white", bg="red")
btn_format.pack(pady=5)

btn_clean = tk.Button(root, text="Nettoyer", command=nettoyer_peripherique, font=("Arial", 12), fg="white", bg="green")
btn_clean.pack(pady=5)

root.mainloop()