# Station Blanche USB

Ce dépôt contient le code source pour une station blanche USB, développée sur un Raspberry Pi sous Raspberry Pi OS. Cette station permet de sécuriser et de gérer des périphériques USB grâce à diverses fonctionnalités.

---

## Structure du projet

### 1. Frontend
Le dossier `frontend` contient le code responsable de l'interface visuelle (GUI). Cette interface permet à l'utilisateur d'interagir avec les fonctionnalités proposées par le backend de manière intuitive. Elle inclut :
- Les interfaces pour l'analyse, le nettoyage, le formatage et l'éjection des périphériques USB.
- Les scripts Python utilisant Tkinter pour créer une interface utilisateur simple et efficace.

### 2. Backend
Le dossier `backend` contient les scripts responsables de l'exécution des différentes fonctions de la station blanche USB, telles que :
- La détection des périphériques USB.
- Le scan antivirus avec **ClamAV**.
- Le nettoyage des fichiers avec **oletools**.
- Le calcul de hash SHA-1 pour vérifier l'intégrité des fichiers.
- Le formatage des périphériques USB en FAT32, NTFS ou EXT4.
- L'éjection sécurisée des périphériques USB.

### 3. Tasks
Le dossier `tasks` contient des scripts qui sont configurés pour s'exécuter automatiquement via `cron`. Ces scripts permettent :
- De vérifier l'intégrité des fichiers critiques.
- De lancer automatiquement l'application principale au démarrage.
- De gérer les journaux et les tâches de maintenance.

### 4. 3DFile
Le dossier `3DFile` regroupe les fichiers nécessaires à l'impression 3D du boîtier pour le Raspberry Pi. Ce boîtier est conçu pour protéger et intégrer le matériel utilisé dans ce projet.

---

## Fonctionnalités principales

1. **Détection des périphériques USB** :
   - Détecte automatiquement les périphériques USB insérés.
   - Enregistre les chemins des périphériques et des points de montage.

2. **Analyse antivirus** :
   - Utilise **ClamAV** pour détecter et supprimer les fichiers infectés.
   - Analyse les fichiers Office pour détecter des macros malveillantes avec **oletools**.

3. **Nettoyage des fichiers** :
   - Désinfecte les fichiers infectés.
   - Supprime les macros malveillantes des fichiers Office.

4. **Calcul de hash SHA-1** :
   - Calcule un hash global pour vérifier l'intégrité des fichiers présents sur la clé USB.

5. **Formatage des périphériques USB** :
   - Formate les périphériques USB en FAT32, NTFS ou EXT4.

6. **Éjection sécurisée** :
   - Éjecte les périphériques USB en toute sécurité après avoir copié les journaux sur la clé USB.

7. **Automatisation avec `cron`** :
   - Configure des tâches automatiques pour vérifier l'intégrité des fichiers et lancer l'application au démarrage.

---

## Installation

Pour installer le projet, utilisez le script `install.sh`. Ce script :
- Copie les fichiers dans `/usr/share/projet`.
- Attribue les permissions nécessaires aux fichiers.
- Installe les dépendances supplémentaires si l'option `--complete` est utilisée.
- Configure automatiquement les tâches `cron` pour l'exécution des scripts si l'option `--complete` est utilisée.

### Commandes d'installation

- **Installation standard** (sans dépendances supplémentaires ni configuration de `cron`) :
  ```bash
  sudo ./install.sh
  ```

- **Installation complète** (avec dépendances et configuration de `cron`) :
  ```bash
  sudo ./install.sh --complete
  ```

---

## Utilisation

1. **Lancement de l'application principale** :
   - L'application principale démarre automatiquement au démarrage si `cron` est configuré.
   - Sinon, vous pouvez la lancer manuellement (faite le depuis le dossier /usr/share/frontend/):
     ```bash
     sudo python3 /usr/share/projet/frontend/accueil.py
     ```

2. **Navigation dans l'interface** :
   - Insérez un périphérique USB pour accéder au menu principal.
   - Utilisez les boutons pour analyser, nettoyer, formater ou éjecter le périphérique USB.

3. **Logs** :
   - Les journaux des actions sont enregistrés dans `/usr/share/projet/backend/logs.txt` puis sur la clé avant ejection.

---

## Configuration automatique avec `cron`

Si l'installation complète est utilisée, les tâches suivantes sont configurées automatiquement :
- **`check.sh`** : Exécuté toutes les minutes pour vérifier l'intégrité des fichiers critiques.
- **`start.sh`** : Exécuté au démarrage pour lancer l'application principale.

Pour vérifier les tâches `cron` configurées :
```bash
sudo crontab -l
```

---

## Notes importantes

- **Privilèges root** :
  - La plupart des scripts nécessitent des privilèges root pour fonctionner correctement.

- **Dépendances** :
  - Assurez-vous que les dépendances suivantes sont installées :
    - **ClamAV** : Pour l'analyse antivirus.
    - **oletools** : Pour l'analyse des fichiers Office.

- **Permissions des fichiers** :
  - Les permissions des fichiers sont configurées automatiquement par le script `install.sh`.

---
