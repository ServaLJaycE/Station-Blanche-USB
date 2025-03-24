#!/bin/bash

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/projet/Backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "$(date) - Début du script fat32.sh"

# Test du chemin
USB_DEVICE_PATH_FILE="/usr/share/Backend/usb_device_path.txt"
if [ ! -f "$USB_DEVICE_PATH_FILE" ]; then
    echo "$(date) - Erreur : Aucun périphérique détecté. Veuillez exécuter detect.sh d'abord. [fat32.sh]"
    exit 1
fi


DEVICE_PATH=$(cat "$USB_DEVICE_PATH_FILE")
echo "$(date) - Clé USB détectée : $DEVICE_PATH [fat32.sh]"

# Démonte toutes les partitions du périphérique
echo "$(date) - Démontage des partitions existantes sur $DEVICE_PATH... [fat32.sh]"
umount "${DEVICE_PATH}"* 2>/dev/null

# Formate le périphérique en FAT32
echo "$(date) - Formatage de $DEVICE_PATH en FAT32... [fat32.sh]"
mkfs.fat -F 32 "$DEVICE_PATH"

if [ $? -eq 0 ]; then
    echo "$(date) - Formatage terminé avec succès.[fat32.sh]"
else
    echo "$(date) - Erreur lors du formatage de $DEVICE_PATH.[fat32.sh]"
    exit 1
fi

echo "$(date) - Fin du script fat32.sh [fat32.sh]"