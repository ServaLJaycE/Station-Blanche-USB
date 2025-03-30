#!/bin/bash

LOG_FILE="/usr/share/projet/backend/logs_clean.txt"
USB_MOUNT_PATH_FILE="/usr/share/projet/backend/usb_mount_path.txt"

echo "$(date) - Début du script clean.sh [clean.sh]" >> "$LOG_FILE"

# Vérification que le fichier contenant le chemin existe
if [ ! -f "$USB_MOUNT_PATH_FILE" ]; then
    echo "$(date) - Erreur : Le fichier $USB_MOUNT_PATH_FILE est introuvable. Veuillez exécuter detect_mount.sh d'abord. [clean.sh]" >> "$LOG_FILE"
    exit 1
fi

# Lecture du chemin de montage
USB_MOUNT_PATH=$(cat "$USB_MOUNT_PATH_FILE")

if [ -z "$USB_MOUNT_PATH" ]; then
    echo "$(date) - Erreur : Aucun périphérique USB monté détecté. [clean.sh]" >> "$LOG_FILE"
    exit 1
fi

echo "$(date) - Nettoyage du périphérique USB monté sur : $USB_MOUNT_PATH [clean.sh]" >> "$LOG_FILE"

# Étape 1 : Désinfection avec ClamAV
echo "$(date) - Étape 1 : Désinfection avec ClamAV... [clean.sh]" >> "$LOG_FILE"
clamscan -r "$USB_MOUNT_PATH" --move="$USB_MOUNT_PATH/quarantine" --log="$LOG_FILE" --infected
if [ $? -ne 0 ]; then
    echo "$(date) - ClamAV a détecté et déplacé des fichiers infectés. Consultez $LOG_FILE pour plus de détails. [clean.sh]" >> "$LOG_FILE"
else
    echo "$(date) - ClamAV : Aucun fichier infecté détecté. [clean.sh]" >> "$LOG_FILE"
fi

# Étape 2 : Suppression des macros malveillantes avec oletools
echo "$(date) - Étape 2 : Suppression des macros malveillantes avec oletools... [clean.sh]" >> "$LOG_FILE"
find "$USB_MOUNT_PATH" -type f \( -iname "*.doc" -o -iname "*.docx" -o -iname "*.xls" -o -iname "*.xlsx" \) | while read -r file; do
    echo "$(date) - Analyse et nettoyage du fichier : $file [clean.sh]" >> "$LOG_FILE"
    olevba --reveal "$file" | grep -q "VBA Macros found"
    if [ $? -eq 0 ]; then
        echo "$(date) - Macros détectées dans $file. Suppression... [clean.sh]" >> "$LOG_FILE"
        # Suppression des macros avec un outil ??
        python3 -c "
import sys
from oletools.olevba import VBA_Parser
file = '$file'
vba_parser = VBA_Parser(file)
vba_parser.remove_macros()
" >> "$LOG_FILE" 2>&1
        echo "$(date) - Macros supprimées de $file. [clean.sh]" >> "$LOG_FILE"
    else
        echo "$(date) - Aucun macro malveillant détecté dans $file. [clean.sh]" >> "$LOG_FILE"
    fi
done

echo "$(date) - Nettoyage terminé. [clean.sh]" >> "$LOG_FILE"
exit 0