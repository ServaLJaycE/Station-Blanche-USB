#!/bin/bash

virus=false

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/projet/backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "$(date) - Début du script analyse.sh [analyse.sh]"

# Fichier contenant le chemin de montage du périphérique USB
USB_MOUNT_PATH_FILE="/usr/share/projet/backend/usb_mount_path.txt"

# Liste des commandes requises
REQUIRED_CMDS=("clamscan" "olevba")

# Vérification de la présence des outils nécessaires
for cmd in "${REQUIRED_CMDS[@]}"; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "$(date) - Erreur : La commande '$cmd' n'est pas installée. Veuillez l'installer avant d'exécuter ce script. [analyse.sh]"
        exit 1
    fi
done

echo "$(date) - Tous les outils requis sont installés. Début de l'analyse... [analyse.sh]"

# Vérification que le fichier contenant le chemin existe
if [ ! -f "$USB_MOUNT_PATH_FILE" ]; then
    echo "$(date) - Erreur : Le fichier $USB_MOUNT_PATH_FILE est introuvable. Veuillez exécuter detect_mount.sh d'abord. [analyse.sh]"
    exit 1
fi

# Lecture du chemin de montage
USB_MOUNT_PATH=$(cat "$USB_MOUNT_PATH_FILE")

if [ -z "$USB_MOUNT_PATH" ]; then
    echo "$(date) - Erreur : Aucun périphérique USB monté détecté. [analyse.sh]"
    exit 1
fi

echo "$(date) - Analyse du périphérique USB monté sur : $USB_MOUNT_PATH [analyse.sh]"

# Étape 1 : Analyse antivirus avec ClamAV
echo "$(date) - Étape 1 : Analyse antivirus avec ClamAV... [analyse.sh]"
clamscan -r "$USB_MOUNT_PATH" --remove >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "$(date) - ClamAV a détecté des fichiers infectés. Consultez $LOG_FILE pour plus de détails. [analyse.sh]"
    virus=true
    exit 1
fi
echo "$(date) - ClamAV : Aucun fichier infecté détecté. [analyse.sh]"

# Étape 2 : Analyse des fichiers Office avec oletools
echo "$(date) - Étape 2 : Analyse des fichiers Office avec oletools... [analyse.sh]"
find "$USB_MOUNT_PATH" -type f \( -iname "*.doc" -o -iname "*.docx" -o -iname "*.xls" -o -iname "*.xlsx" \) | while read -r file; do
    echo "$(date) - Analyse du fichier : $file [analyse.sh]"
    olevba "$file" --reveal >> "$LOG_FILE" 2>&1
    if [ $? -ne 0 ]; then
        virus=true
        echo "$(date) - oletools a détecté des macros malveillantes dans $file. Consultez $LOG_FILE pour plus de détails. [analyse.sh]"
        exit 1
    fi
done
echo "$(date) - oletools : Aucun fichier Office malveillant détecté. [analyse.sh]"

echo "$(date) - Analyse terminée avec succès. [analyse.sh]"

if [ "$virus" = true ]; then
    exit 1
else
    exit 0
fi