#!/bin/bash

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/projet/backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "$(date) - Début du script ejectUSB.sh [ejectUSB.sh]"

# Vérifie si le fichier contenant le chemin du périphérique existe
DEVICE_PATH_FILE="/usr/share/projet/backend/usb_device_path.txt"
if [ ! -f "$DEVICE_PATH_FILE" ]; then
    echo "$(date) - Erreur : Le fichier contenant le chemin du périphérique n'existe pas. [ejectUSB.sh]"
    exit 1
fi

# Lit le chemin du périphérique depuis le fichier
DEVICE_PATH=$(cat "$DEVICE_PATH_FILE")
echo "$(date) - Clé USB détectée : $DEVICE_PATH [ejectUSB.sh]"

# Éjecte le périphérique USB
echo "$(date) - Éjection du périphérique USB... [ejectUSB.sh]"
udisksctl unmount -b "$DEVICE_PATH" >> "$LOG_FILE" 2>&1
udisksctl power-off -b "$DEVICE_PATH" >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    echo "$(date) - Clé USB éjectée avec succès. [ejectUSB.sh]"

    # Vide le fichier logs.txt
    echo "$(date) - Vidage du fichier logs.txt... [ejectUSB.sh]"
    > "$LOG_FILE"

    # Supprime les fichiers usb_mount_path.txt et usb_device_path.txt
    echo "$(date) - Suppression des fichiers temporaires... [ejectUSB.sh]"
    rm -f /usr/share/projet/backend/usb_mount_path.txt
    rm -f /usr/share/projet/backend/usb_device_path.txt
else
    echo "$(date) - Échec de l'éjection de la clé USB. [ejectUSB.sh]"
    exit 1
fi

echo "$(date) - Fin du script ejectUSB.sh [ejectUSB.sh]"