#!/bin/bash

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/projet/Backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "$(date) - Début du script analyse.sh [analyse.sh]"

# Fichier contenant le chemin du périphérique USB détecté
USB_DEVICE_PATH="/usr/share/projet/Backend/usb_device_path.txt"

# Liste des commandes requises
REQUIRED_CMDS=("usbguard" "evtest" "clamscan" "olevba")

# Vérification de la présence des outils nécessaires
for cmd in "${REQUIRED_CMDS[@]}"; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "$(date) - Erreur : La commande '$cmd' n'est pas installée. Veuillez l'installer avant d'exécuter ce script. [analyse.sh]"
        exit 1
    fi
done

echo "$(date) - Tous les outils requis sont installés. Début de l'analyse... [analyse.sh]"

# Vérification que le fichier contenant le chemin existe
if [ ! -f "$USB_DEVICE_PATH" ]; then
    echo "$(date) - Erreur : Le fichier $USB_DEVICE_PATH est introuvable. Veuillez exécuter detect.sh d'abord. [analyse.sh]"
    exit 1
fi

# Lecture du chemin du périphérique USB
USB_PATH=$(cat "$USB_DEVICE_PATH")

if [ -z "$USB_PATH" ]; then
    echo "$(date) - Erreur : Aucun périphérique USB détecté. [analyse.sh]"
    exit 1
fi

echo "$(date) - Analyse du périphérique USB : $USB_PATH [analyse.sh]"

# Étape 1 : Vérification des entrées HID avec SBGuard
echo "$(date) - Étape 1 : Vérification des entrées HID avec SBGuard... [analyse.sh]"
sbguard --check "$USB_PATH" >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "$(date) - SBGuard a détecté des entrées HID non autorisées. [analyse.sh]"
    exit 1
fi
echo "$(date) - SBGuard : Aucune entrée HID non autorisée détectée. [analyse.sh]"

# Étape 2 : Contrôle des périphériques HID avec evtest
echo "$(date) - Étape 2 : Contrôle des périphériques HID avec evtest... [analyse.sh]"
evtest "$USB_PATH" >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "$(date) - Erreur lors de l'utilisation de evtest. [analyse.sh]"
    exit 1
fi
echo "$(date) - evtest : Contrôle terminé. [analyse.sh]"

# Étape 3 : Analyse antivirus avec ClamAV
echo "$(date) - Étape 3 : Analyse antivirus avec ClamAV... [analyse.sh]"
clamscan -r "$USB_PATH" --remove >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "$(date) - ClamAV a détecté des fichiers infectés. Consultez $LOG_FILE pour plus de détails. [analyse.sh]"
    exit 1
fi
echo "$(date) - ClamAV : Aucun fichier infecté détecté. [analyse.sh]"

# Étape 4 : Analyse des fichiers Office avec oletools
echo "$(date) - Étape 4 : Analyse des fichiers Office avec oletools... [analyse.sh]"
find "$USB_PATH" -type f \( -iname "*.doc" -o -iname "*.docx" -o -iname "*.xls" -o -iname "*.xlsx" \) | while read -r file; do
    echo "$(date) - Analyse du fichier : $file [analyse.sh]"
    olevba "$file" --reveal >> "$LOG_FILE" 2>&1
    if [ $? -ne 0 ]; then
        echo "$(date) - oletools a détecté des macros malveillantes dans $file. Consultez $LOG_FILE pour plus de détails. [analyse.sh]"
        exit 1
    fi
done
echo "$(date) - oletools : Aucun fichier Office malveillant détecté. [analyse.sh]"

echo "$(date) - Analyse terminée avec succès. [analyse.sh]"