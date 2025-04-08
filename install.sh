#!/bin/bash

# Chemin de destination
DEST_DIR="/usr/share/projet"
mkdir -p "$DEST_DIR"
# Création des répertoires nécessaires
echo "Création des répertoires dans $DEST_DIR..."
mkdir -p "$DEST_DIR/backend"
mkdir -p "$DEST_DIR/frontend/images"


# Copie des fichiers
echo "Copie des fichiers dans $DEST_DIR..."
cp -r backend/* "$DEST_DIR/backend/"
cp -r frontend/* "$DEST_DIR/frontend/"
cp -r tasks/* "$DEST_DIR/task/"

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
chmod 700 "$DEST_DIR/task/"*.sh
chmod 644 "$DEST_DIR/task/logs.txt"
chmod 600 "$DEST_DIR/task/start_reference.sh"
chmod 700 "$DEST_DIR/task/start.sh"

echo "Installation terminée avec succès."