#!/bin/bash

# Chemin de destination
DEST_DIR="/usr/share/projet"
mkdir -p "$DEST_DIR"

# Fonction pour installer les dépendances supplémentaires
install_dependencies() {
    echo "Installation des dépendances supplémentaires..."
    sudo apt update
    sudo apt install -y clamav python3-pip
    pip3 install -r requirements.txt
    echo "Dépendances supplémentaires installées avec succès."
}

# Vérifie si l'option --complete est passée
if [[ "$1" == "--complete" ]]; then
    install_dependencies
fi

# Création des répertoires nécessaires
echo "Création des répertoires dans $DEST_DIR..."
mkdir -p "$DEST_DIR/backend"
mkdir -p "$DEST_DIR/frontend/images"
mkdir -p "$DEST_DIR/tasks"

# Copie des fichiers
echo "Copie des fichiers dans $DEST_DIR..."
cp -r backend/* "$DEST_DIR/backend/"
cp -r frontend/* "$DEST_DIR/frontend/"
cp -r tasks/* "$DEST_DIR/tasks/"

# Attribution des permissions pour le backend
echo "Attribution des permissions pour le backend..."
chmod 755 "$DEST_DIR/backend/"*.sh
chmod 644 "$DEST_DIR/backend/logs.txt"
chmod 644 "$DEST_DIR/backend/README.md"

# Attribution des permissions pour le frontend
echo "Attribution des permissions pour le frontend..."
chmod 755 "$DEST_DIR/frontend/"*.py
chmod 644 "$DEST_DIR/frontend/README.md"
chmod 755 "$DEST_DIR/frontend/images/"*.png
chmod 644 "$DEST_DIR/frontend/refus_acces.py"

# Attribution des permissions pour les tasks
echo "Attribution des permissions pour les tasks..."
chmod 700 "$DEST_DIR/tasks/"*.sh
chmod 644 "$DEST_DIR/tasks/logs.txt"
chmod 600 "$DEST_DIR/tasks/start_reference.sh"
chmod 700 "$DEST_DIR/tasks/start.sh"

echo "Installation terminée avec succès."