import tkinter as tk

# Fonction qui ouvre la nouvelle fenêtre de formatage
def ouvrir_format_page(parent, label):
    # Créer une nouvelle fenêtre (Toplevel) pour le formatage
    format_window = tk.Toplevel(parent)
    format_window.title("Choisir le format de la clé USB")

    # Configurer le plein écran
    format_window.attributes('-fullscreen', True)

    # Ajouter un bouton pour quitter le mode plein écran
    def exit_fullscreen(event=None):
        format_window.attributes('-fullscreen', False)

    format_window.bind('<Escape>', exit_fullscreen)

    # Ajouter un titre à la nouvelle fenêtre
    label_format = tk.Label(format_window, text="Choisissez le format de la clé USB :", font=("Arial", 16))
    label_format.pack(pady=20)

    # Fonction pour afficher le format sélectionné dans le label principal
    def choisir_format(format_type):
        label.config(text=f"Format sélectionné : {format_type}")
        format_window.destroy()  # Fermer la fenêtre après la sélection du format

    # Ajouter les boutons pour choisir le format
    button_fat32 = tk.Button(format_window, text="FAT32", command=lambda: choisir_format("FAT32"), font=("Arial", 14), bg="lightblue", width=15, height=2)
    button_fat32.pack(pady=10)

    button_windows = tk.Button(format_window, text="Windows", command=lambda: choisir_format("Windows"), font=("Arial", 14), bg="lightgreen", width=15, height=2)
    button_windows.pack(pady=10)

    button_linux = tk.Button(format_window, text="Linux", command=lambda: choisir_format("Linux"), font=("Arial", 14), bg="lightcoral", width=15, height=2)
    button_linux.pack(pady=10)
