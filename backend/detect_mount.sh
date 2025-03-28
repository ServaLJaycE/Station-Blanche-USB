#!/bin/bash

# Redirige toutes les sorties (stdout et stderr) vers logs.txt
LOG_FILE="/usr/share/projet/Backend/logs.txt"
exec >> "$LOG_FILE" 2>&1

echo "$(date) - Début du script detect_mount.sh [detect_mount.sh]"

# Fichier temporaire pour enregistrer le chemin de montage
MOUNT_PATH_FILE="/usr/share/projet/Backend/usb_mount_path.txt"

# Liste les périphériques montés avant l'insertion
MOUNTS_BEFORE=$(lsblk -o MOUNTPOINT -nr | grep -v '^$')

echo "$(date) - Veuillez insérer un périphérique USB... [detect_mount.sh]"

# Boucle pour détecter un nouveau point de montage
while true; do
    # Liste les périphériques montés après l'insertion
    MOUNTS_AFTER=$(lsblk -o MOUNTPOINT -nr | grep -v '^$')

    # Identifie le nouveau point de montage
    NEW_MOUNT=$(comm -13 <(echo "$MOUNTS_BEFORE" | sort) <(echo "$MOUNTS_AFTER" | sort))

    if [ ! -z "$NEW_MOUNT" ]; then
        echo "$(date) - Périphérique USB monté sur : $NEW_MOUNT [detect_mount.sh]"

        # Enregistre le chemin de montage dans un fichier temporaire
        echo "$NEW_MOUNT" > "$MOUNT_PATH_FILE"
        echo "$(date) - Le chemin de montage a été enregistré dans $MOUNT_PATH_FILE [detect_mount.sh]"
        break
    fi

    # Attendre 2 secondes avant de refaire un scan
    sleep 2
done

echo "$(date) - Fin du script detect_mount.sh [detect_mount.sh]"