#!/bin/bash

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/Backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "Détection de la clé USB..."


DEVICES_BEFORE=$(lsblk -dn -o NAME)
# Boucle pour détecter un nouveau périphérique
while true; do
    DEVICES_AFTER=$(lsblk -dn -o NAME)
    NEW_DEVICE=$(comm -13 <(echo "$DEVICES_BEFORE" | sort) <(echo "$DEVICES_AFTER" | sort))

    if [ ! -z "$NEW_DEVICE" ]; then
        DEVICE_PATH="/dev/$NEW_DEVICE"
        echo "Clé USB détectée : $DEVICE_PATH"

        # Enregistre le chemin du périphérique dans un fichier temporaire
        echo "$DEVICE_PATH" > /usr/share/projet/Backend/usb_device_path.txt
        echo "Le chemin du périphérique a été enregistré dans usb_device_path.txt."
        break
    fi

    # Attendre 2 secondes avant de refaire un scan
    sleep 2
done