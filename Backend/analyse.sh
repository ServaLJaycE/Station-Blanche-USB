#!/bin/bash

# Fichier contenant le chemin du périphérique USB détecté
USB_DEVICE_PATH="usb_device_path.txt"
LOG_FILE="logs.txt"

# Liste des commandes requises
REQUIRED_CMDS=("usbguard" "evtest" "clamscan" "olevba")

# Vérification de la présence des outils nécessaires
for cmd in "${REQUIRED_CMDS[@]}"; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "Erreur : La commande '$cmd' n'est pas installée. Veuillez l'installer avant d'exécuter ce script."
        exit 1
    fi
done

echo "Tous les outils requis sont installés. Début du script..."

# Initialisation des logs
echo "=== Début de l'analyse : $(date) ===" > "$LOG_FILE"

# Vérification que le fichier contenant le chemin existe
if [ ! -f "$USB_DEVICE_PATH" ]; then
    echo "Erreur : Le fichier $USB_DEVICE_PATH est introuvable. Veuillez exécuter detect.sh d'abord." | tee -a "$LOG_FILE"
    exit 1
fi

# Lecture du chemin du périphérique USB
USB_PATH=$(cat "$USB_DEVICE_PATH")

if [ -z "$USB_PATH" ]; then
    echo "Erreur : Aucun périphérique USB détecté." | tee -a "$LOG_FILE"
    exit 1
fi

echo "Analyse du périphérique USB : $USB_PATH" | tee -a "$LOG_FILE"

# Étape 1 : Vérification des entrées HID avec SBGuard
echo "Étape 1 : Vérification des entrées HID avec SBGuard..." | tee -a "$LOG_FILE"
sbguard --check "$USB_PATH" >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "SBGuard a détecté des entrées HID non autorisées." | tee -a "$LOG_FILE"
    exit 1
fi
echo "SBGuard : Aucune entrée HID non autorisée détectée." | tee -a "$LOG_FILE"

# Étape 2 : Contrôle des périphériques HID avec evtest
echo "Étape 2 : Contrôle des périphériques HID avec evtest..." | tee -a "$LOG_FILE"
evtest "$USB_PATH" >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'utilisation de evtest." | tee -a "$LOG_FILE"
    exit 1
fi
echo "evtest : Contrôle terminé." | tee -a "$LOG_FILE"

# Étape 3 : Analyse antivirus avec ClamAV
echo "Étape 3 : Analyse antivirus avec ClamAV..." | tee -a "$LOG_FILE"
clamscan -r "$USB_PATH" --remove >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "ClamAV a détecté des fichiers infectés. Consultez $LOG_FILE pour plus de détails." | tee -a "$LOG_FILE"
    exit 1
fi
echo "ClamAV : Aucun fichier infecté détecté." | tee -a "$LOG_FILE"

# Étape 4 : Analyse des fichiers Office avec oletools
echo "Étape 4 : Analyse des fichiers Office avec oletools..." | tee -a "$LOG_FILE"
find "$USB_PATH" -type f \( -iname "*.doc" -o -iname "*.docx" -o -iname "*.xls" -o -iname "*.xlsx" \) | while read -r file; do
    echo "Analyse du fichier : $file" | tee -a "$LOG_FILE"
    olevba "$file" --reveal >> "$LOG_FILE" 2>&1
    if [ $? -ne 0 ]; then
        echo "oletools a détecté des macros malveillantes dans $file. Consultez $LOG_FILE pour plus de détails." | tee -a "$LOG_FILE"
        exit 1
    fi
done
echo "oletools : Aucun fichier Office malveillant détecté." | tee -a "$LOG_FILE"

echo "Analyse terminée avec succès." | tee -a "$LOG_FILE"
echo "=== Fin de l'analyse : $(date) ===" >> "$LOG_FILE"