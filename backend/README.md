# Backend

Ce dossier contient les scripts responsables des fonctionnalités principales de la station blanche USB. Ces scripts permettent de détecter, analyser, nettoyer, formater et éjecter les périphériques USB connectés.

## Scripts

### `detect.sh`
Ce script détecte les périphériques USB insérés. Il :
- Effectue un scan toutes les 2 secondes pour détecter un nouveau périphérique.
- Enregistre le chemin du périphérique détecté (par exemple, `/dev/sdb`) dans le fichier `usb_device_path.txt`.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt` pour un suivi des événements.

### `detect_mount.sh`
Ce script détecte le chemin de montage du périphérique USB. Il :
- Effectue un scan toutes les 2 secondes pour détecter un nouveau point de montage.
- Enregistre le chemin de montage (par exemple, `/media/usb`) dans le fichier `usb_mount_path.txt`.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt`.

### `analyse.sh`
Ce script analyse les fichiers du périphérique USB monté. Il :
- Lit le chemin de montage depuis `usb_mount_path.txt`.
- Effectue une analyse antivirus avec **ClamAV** pour détecter et supprimer les fichiers infectés.
- Analyse les fichiers Office (comme `.docx` ou `.xls`) avec **oletools** pour détecter des macros malveillantes.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt`.

### `clean.sh`
Ce script nettoie les fichiers du périphérique USB monté. Il :
- Désinfecte les fichiers infectés avec **ClamAV**.
- Supprime les macros malveillantes des fichiers Office avec **oletools**.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs_clean.txt`.

### `hash.sh`
Ce script calcule un hash global SHA-1 pour tous les fichiers présents sur le périphérique USB monté. Il :
- Concatène le contenu de tous les fichiers dans un fichier temporaire.
- Calcule le hash SHA-1 global et l'ajoute au fichier `hash.txt`.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt`.

### `fat32.sh`
Ce script formate automatiquement le périphérique USB détecté en **FAT32**. Il :
- Lit le chemin du périphérique depuis `usb_device_path.txt`.
- Démonte toutes les partitions existantes sur le périphérique.
- Formate le périphérique en FAT32 sans demander de confirmation.
- Enregistre les événements et erreurs dans `logs.txt`.

### `ext4.sh`
Ce script formate automatiquement le périphérique USB détecté en **EXT4**. Il :
- Lit le chemin du périphérique depuis `usb_device_path.txt`.
- Démonte toutes les partitions existantes sur le périphérique.
- Formate le périphérique en EXT4 sans demander de confirmation.
- Enregistre les événements et erreurs dans `logs.txt`.

### `ntfs.sh`
Ce script formate automatiquement le périphérique USB détecté en **NTFS**. Il :
- Lit le chemin du périphérique depuis `usb_device_path.txt`.
- Démonte toutes les partitions existantes sur le périphérique.
- Formate le périphérique en NTFS sans demander de confirmation.
- Enregistre les événements et erreurs dans `logs.txt`.

### `ejectUSB.sh`
Ce script éjecte en toute sécurité le périphérique USB détecté. Il :
- Lit le chemin du périphérique depuis `usb_device_path.txt`.
- Copie les logs sur la clé USB avant l'éjection.
- Utilise la commande `udisksctl` pour démonter et éteindre le périphérique en toute sécurité.
- Supprime les fichiers temporaires `usb_device_path.txt` et `usb_mount_path.txt`.
- Enregistre les événements et erreurs dans `logs.txt`.

### Fichiers temporaires
- **`usb_device_path.txt`** : Contient le chemin du périphérique USB détecté (par exemple, `/dev/sdb`).
- **`usb_mount_path.txt`** : Contient le chemin de montage du périphérique USB (par exemple, `/media/usb`).
- **`logs.txt`** : Contient les journaux générés par les scripts du backend.
- **`hash.txt`** : Contient les hashes SHA-1 calculés pour les fichiers du périphérique USB.

## Utilisation
1. **Détection d'un périphérique USB :**
   - Exécutez `detect.sh` pour détecter un périphérique USB inséré.
   - Le chemin du périphérique sera enregistré dans `usb_device_path.txt`.

2. **Détection du chemin de montage :**
   - Exécutez `detect_mount.sh` pour détecter le chemin de montage du périphérique USB.
   - Le chemin de montage sera enregistré dans `usb_mount_path.txt`.

3. **Analyse des fichiers :**
   - Exécutez `analyse.sh` pour analyser les fichiers du périphérique USB monté.
   - Les résultats de l'analyse seront enregistrés dans `logs.txt`.

4. **Nettoyage des fichiers :**
   - Exécutez `clean.sh` pour désinfecter et nettoyer les fichiers du périphérique USB.

5. **Calcul du hash global :**
   - Exécutez `hash.sh` pour calculer un hash global SHA-1 des fichiers du périphérique USB.

6. **Formatage d'un périphérique USB :**
   - Exécutez l'un des scripts de formatage (`fat32.sh`, `ext4.sh`, `ntfs.sh`) pour formater le périphérique détecté.

7. **Éjection d'un périphérique USB :**
   - Exécutez `ejectUSB.sh` pour éjecter en toute sécurité le périphérique USB détecté.

8. **Vérification des logs :**
   - Consultez le fichier `logs.txt` pour suivre les actions effectuées par les scripts.

## Notes
- Assurez-vous que les scripts sont exécutés avec des privilèges root.
- Les scripts de formatage ne demandent pas de confirmation avant de procéder.
- Les fichiers temporaires sont recréés à chaque nouvelle détection de périphérique.