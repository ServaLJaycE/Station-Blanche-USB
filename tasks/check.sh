#!/bin/bash

# Chemin vers le fichier start.sh actuel
CURRENT_FILE="/usr/share/projet/Tasks/start.sh"
# Chemin vers le fichier de référence
REFERENCE_FILE="/usr/share/projet/Tasks/start_reference.sh"


# Redirige toute la sortie (stdout et stderr) vers le fichier de log
LOG_FILE="/usr/share/projet/Tasks/logs.txt"
exec > "$LOG_FILE" 2>&1


# Vérifie si le fichier de référence existe
if [ ! -f "$REFERENCE_FILE" ]; then
    echo "$(date) - Le fichier de référence $REFERENCE_FILE est introuvable [check.sh]."
    exit 1
fi

# Calcule les empreintes de hachage des deux fichiers
CURRENT_HASH=$(sha256sum "$CURRENT_FILE" | awk '{print $1}')
REFERENCE_HASH=$(sha256sum "$REFERENCE_FILE" | awk '{print $1}')

# Compare les empreintes de hachage
if [ "$CURRENT_HASH" != "$REFERENCE_HASH" ]; then
    echo "$(date) - Le fichier start.sh a été modifié. Remplacement par la version de référence... [check.sh]."
    cp "$REFERENCE_FILE" "$CURRENT_FILE"
    chmod +x "$CURRENT_FILE"
else
    echo "$(date) - Le fichier start.sh est identique à la version actuelle [check.sh]."
fi


# Exécute le fichier start.sh en tant que root
echo "$(date) - Exécution de start.sh en tant que root... [check.sh]."
sudo bash "$CURRENT_FILE"