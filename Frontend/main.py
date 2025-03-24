import tkinter as tk

def on_click():
    label.config(text="Bouton cliqué !")

# Créer l'application
app = tk.Tk()
app.title("Station de décontamination USB")

# Configurer le plein écran
app.attributes('-fullscreen', True)

# Ajouter un bouton pour quitter le mode plein écran
def exit_fullscreen(event=None):
    app.attributes('-fullscreen', False)

app.bind('<Escape>', exit_fullscreen)

# Ajouter des widgets

label = tk.Label(app, text="Bienvenue sur la station de décontamination USB !", font=("Arial", 20))
label.pack(pady=20)

button = tk.Button(app, text="Cliquez ici", command=on_click)
button.pack(pady=10)

# Lancer la boucle principale
app.mainloop()
