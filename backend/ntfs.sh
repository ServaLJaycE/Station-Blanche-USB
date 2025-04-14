#!/bin/bash

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/projet/backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "$(date) - Début du script ntfs.sh"

# Vérifie si le fichier contenant le chemin du périphérique existe
USB_DEVICE_PATH_FILE="/usr/share/backend/usb_device_path.txt"
if [ ! -f "$USB_DEVICE_PATH_FILE" ]; then
    echo "$(date) - Erreur : Aucun périphérique détecté. Veuillez exécuter detect.sh d'abord. [ntfs.sh]"
    exit 1
fi

# Lit le chemin du périphérique
DEVICE_PATH=$(cat "$USB_DEVICE_PATH_FILE")
echo "$(date) - Clé USB détectée : $DEVICE_PATH [ntfs.sh]"

# Démonte toutes les partitions du périphérique
echo "$(date) - Démontage des partitions existantes sur $DEVICE_PATH... [ntfs.sh]"
umount "${DEVICE_PATH}"* 2>/dev/null

# Formate le périphérique en NTFS
echo "$(date) - Formatage de $DEVICE_PATH en NTFS... [ntfs.sh]"
mkfs.ntfs -f "$DEVICE_PATH"

if [ $? -eq 0 ]; then
    echo "$(date) - Formatage terminé avec succès. [ntfs.sh]"
else
    echo "$(date) - Erreur lors du formatage de $DEVICE_PATH. [ntfs.sh]"
    exit 1
fi

echo "$(date) - Fin du script ntfs.sh [ntfs.sh]"