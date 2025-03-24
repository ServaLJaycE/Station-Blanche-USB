import tkinter as tk
import subprocess

# Créer une nouvelle fenêtre pour le formatage
format_interface = tk.Tk()
format_interface.title("Choisir le format de la clé USB")

# Configurer le plein écran
format_interface.attributes('-fullscreen', True)

# Ajouter un bouton pour quitter le mode plein écran
def exit_fullscreen(event=None):
    format_interface.attributes('-fullscreen', False)

format_interface.bind('<Escape>', exit_fullscreen)

def quitter() :
    format_interface.destroy()
    subprocess.run(["python", "main_interface.py"])
    



# Ajouter un titre à la nouvelle fenêtre
label_format = tk.Label(format_interface, text="Choisissez le format de la clé USB :", font=("Arial", 16))
label_format.pack(pady=20)

# Fonction pour afficher le format sélectionné dans le label principal
# def choisir_format(format_type):
#     label.config(text=f"Format sélectionné : {format_type}")
#     format_interface.destroy()  # Fermer la fenêtre après la sélection du format

# Ajouter les boutons pour choisir le format
button_fat32 = tk.Button(format_interface, text="FAT32", command= 0, font=("Arial", 14), bg="lightblue", width=15, height=2) #  choisir_format("FAT32")
button_fat32.pack(pady=10)

button_windows = tk.Button(format_interface, text="Windows", command=0 , font=("Arial", 14), bg="lightgreen", width=15, height=2) # choisir_format("Windows")
button_windows.pack(pady=10)

button_linux = tk.Button(format_interface, text="Linux", command=0 , font=("Arial", 14), bg="lightcoral", width=15, height=2) # choisir_format("Linux")
button_linux.pack(pady=10)

button_quitter = tk.Button(format_interface, text="Quitter", command=quitter, font=("Arial", 14), bg="lightgrey", width=15, height=2)
button_quitter.pack(pady=10)

# Lancer la boucle principale
format_interface.mainloop()