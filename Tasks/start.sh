#!/bin/bash


# Redirige toute la sortie (stdout et stderr) vers le fichier de log
LOG_FILE="/usr/share/projet/Tasks/logs.txt"
exec >> "$LOG_FILE" 2>&1


# Vérifie si le script est exécuté en tant que root
if [ "$EUID" -ne 0 ]; then
    echo "$(date) - Veuillez exécuter ce script start.sh en tant que root."
    exit 1
fi

# Chemin vers le fichier Python Tkinter
PYTHON_FILE="/usr/share/projet/le_fichier.py"




# Exécute le fichier Python en tant que root
echo "$(date) - Exécution du fichier Python $PYTHON_FILE..."
sudo python3 "$PYTHON_FILE"