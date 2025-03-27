#!/bin/bash

# Fichier contenant le chemin de montage du périphérique USB
USB_MOUNT_PATH_FILE="/usr/share/projet/Backend/usb_mount_path.txt"
LOG_FILE="/usr/share/projet/Backend/logs.txt"

# Initialisation des logs
echo "=== Début du calcul du hash global SHA-1 : $(date) ===" | tee -a "$LOG_FILE"

# Vérification que le fichier contenant le chemin existe
if [ ! -f "$USB_MOUNT_PATH_FILE" ]; then
    echo "Erreur : Le fichier $USB_MOUNT_PATH_FILE est introuvable. Veuillez exécuter detect_mount.sh d'abord." | tee -a "$LOG_FILE"
    exit 1
fi

# Lecture du chemin de montage
USB_MOUNT_PATH=$(cat "$USB_MOUNT_PATH_FILE")

if [ -z "$USB_MOUNT_PATH" ]; then
    echo "Erreur : Aucun périphérique USB monté détecté." | tee -a "$LOG_FILE"
    exit 1
fi

echo "Calcul du hash global SHA-1 pour les fichiers dans : $USB_MOUNT_PATH" | tee -a "$LOG_FILE"

# Création d'un fichier temporaire pour concaténer les contenus
TEMP_FILE=$(mktemp)

# Parcours des fichiers et concaténation de leurs contenus
find "$USB_MOUNT_PATH" -type f | while read -r file; do
    #echo "Ajout du contenu du fichier : $file" | tee -a "$LOG_FILE"
    cat "$file" >> "$TEMP_FILE"
done

# Calcul du hash global SHA-1
GLOBAL_HASH=$(sha1sum "$TEMP_FILE" | awk '{print $1}')
echo "Hash global SHA-1 de la clé USB : $GLOBAL_HASH" | tee -a "$LOG_FILE"

# Suppression du fichier temporaire
rm -f "$TEMP_FILE"

echo "=== Fin du calcul du hash global SHA-1 : $(date) ===" | tee -a "$LOG_FILE"

