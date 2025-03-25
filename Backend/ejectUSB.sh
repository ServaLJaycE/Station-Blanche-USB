#!/bin/bash

# Vérifie si le fichier contenant le chemin du périphérique existe
DEVICE_PATH_FILE="/usr/share/projet/Backend/usb_device_path.txt"
if [ ! -f "$DEVICE_PATH_FILE" ]; then
    echo "Le fichier contenant le chemin du périphérique n'existe pas."
    exit 1
fi

# Lit le chemin du périphérique depuis le fichier
DEVICE_PATH=$(cat "$DEVICE_PATH_FILE")

# Éjecte le périphérique USB
udisksctl unmount -b "$DEVICE_PATH"
udisksctl power-off -b "$DEVICE_PATH"

if [ $? -eq 0 ]; then
    echo "Clé USB éjectée avec succès."
else
    echo "Échec de l'éjection de la clé USB."
    exit 1
fi