import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

# Créer une nouvelle fenêtre pour le formatage
format_interface = Tk()
format_interface.title("Choisir le format de la clé USB")

# Configurer le plein écran
format_interface.attributes('-fullscreen', True)

def fat32():
    # ajouter script pour formater en fat32
    pass

def windows():
    # ajouter script pour formater en ntfs
    pass

def linux():
    # ajouter script pour formater en ext4
    pass

def quitter() :
    format_interface.destroy()
    subprocess.run(["python", "main_interface.py"])
    
# style
style = ttk.Style() 
style.configure('TButton', font = ('calibri', 30, 'bold'), borderwidth = '4', relief = 'raised', width = 20, height = 20, padding=(30, 20))

style.configure('Fat32.TButton', foreground='black', background='#AED6F1')   # Bleu
style.configure('Windows.TButton', foreground='black', background='#ABEBC6')   # Vert
style.configure('Linux.TButton', foreground='black', background='#F5B7B1')    # Rouge
style.configure('Quitter.TButton', foreground='black', background='lightgrey')    # Gris

# Appliquer la couleur au survol avec map()
style.map('Fat32.TButton', background=[('active', '#5DADE2')]) 
style.map('Windows.TButton', background=[('active', '#58D68D')])  
style.map('Linux.TButton', background=[('active', '#EC7063')])  
style.map('Quitter.TButton', background=[('active', 'grey')])  

# Ajouter un titre à la nouvelle fenêtre
label_format = tk.Label(format_interface, text="Choisissez le format de la clé USB :", font=("Arial", 40))
label_format.pack(pady=20)
label_format.place(relx=0.5, rely=0.3, anchor="center") 

# Créer un conteneur pour les boutons côte à côte
button_frame = ttk.Frame(format_interface)
button_frame.pack(pady=20)
button_frame.place(relx=0.5, rely=0.5, anchor="center") 


# Ajouter les boutons pour choisir le format
button_fat32 = ttk.Button(button_frame, text="FAT32", command= fat32, style="Fat32.TButton") #  choisir_format("FAT32")
button_fat32.pack(side=tk.LEFT, padx=15)

button_windows = ttk.Button(button_frame, text="Windows", command= windows, style="Windows.TButton") # choisir_format("Windows")
button_windows.pack(side=tk.LEFT, padx=15)

button_linux = ttk.Button(button_frame, text="Linux", command= linux, style="Linux.TButton") # choisir_format("Linux")
button_linux.pack(side=tk.LEFT, padx=15)

button_quitter = ttk.Button(format_interface, text="Quitter", command=quitter, style="Quitter.TButton")
button_quitter.pack(pady=20)
button_quitter.place(relx=0.5, rely=0.65, anchor="center")  

# Lancer la boucle principale
format_interface.mainloop()