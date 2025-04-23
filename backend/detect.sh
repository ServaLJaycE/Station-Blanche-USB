#!/bin/bash

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/projet/backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "Détection de la clé USB... [detection.sh]"

DEVICES_BEFORE_LSBLK=$(lsblk -dn -o NAME)
DEVICES_BEFORE_LSUSB=$(lsusb)

# Boucle pour détecter un nouveau périphérique
while true; do
    DEVICES_AFTER_LSBLK=$(lsblk -dn -o NAME)
    DEVICES_AFTER_LSUSB=$(lsusb)

    # Détection des nouveaux périphériques de stockage
    NEW_DEVICE_LSBLK=$(comm -13 <(echo "$DEVICES_BEFORE_LSBLK" | sort) <(echo "$DEVICES_AFTER_LSBLK" | sort))

    # Détection des nouveaux périphériques USB
    NEW_DEVICE_LSUSB=$(comm -13 <(echo "$DEVICES_BEFORE_LSUSB" | sort) <(echo "$DEVICES_AFTER_LSUSB" | sort))

    if [ ! -z "$NEW_DEVICE_LSBLK" ]; then
        # Si un périphérique de stockage est détecté
        DEVICE_PATH="/dev/$NEW_DEVICE_LSBLK"
        echo "Clé USB détectée : $DEVICE_PATH"

        # Enregistre le chemin du périphérique dans un fichier temporaire
        echo "$DEVICE_PATH" > /usr/share/projet/backend/usb_device_path.txt
        echo "Le chemin du périphérique a été enregistré dans usb_device_path.txt. [detection.sh]"
        break
    elif [ ! -z "$NEW_DEVICE_LSUSB" ]; then
        # Si un périphérique USB est détecté, vérifie s'il est suspect
        echo "Périphérique détecté : $NEW_DEVICE_LSUSB [detection.sh]"

        # Vérifie si ce n'est pas une clé USB (par exemple, une souris ou autre)
        if ! echo "$NEW_DEVICE_LSUSB" | grep -iqE "UDisk|Mass Storage|Flash Drive|USB Storage|Logilink|Kingston"; then
            echo "Périphérique non autorisé détecté (non clé USB) : $NEW_DEVICE_LSUSB [detect.sh]"


            # Bloque le périphérique suspect
            # USB_ID=$(echo "$NEW_DEVICE_LSUSB" | awk '{print $6}') # Récupère l'ID USB (VendorID:ProductID)
            # echo "Blocage du périphérique suspect avec ID : $USB_ID"
            # for DEV_PATH in $(ls /sys/bus/usb/devices/ | grep ":"); do
            #     if grep -q "$USB_ID" "/sys/bus/usb/devices/$DEV_PATH/idVendor" 2>/dev/null; then
            #         echo "0" > "/sys/bus/usb/devices/$DEV_PATH/authorized"
            #         echo "Périphérique $USB_ID bloqué."
            #     fi
            # done


            # Redirige vers le script refus_acces.py
            python3 /usr/share/projet/frontend/refus_acces.py
            exit 1
        fi
    fi

    # Attendre 2 secondes avant de refaire un scan
    sleep 2
done
