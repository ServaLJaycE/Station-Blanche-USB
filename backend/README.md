# Backend

Ce dossier contient les scripts responsables des fonctionnalités principales de la station blanche USB. Ces scripts permettent de détecter, analyser, nettoyer et formater les périphériques USB connectés.

## Scripts

### `detect.sh`
Ce script détecte les périphériques USB insérés. Il :
- Effectue un scan toutes les 2 secondes pour détecter un nouveau périphérique.
- Enregistre le chemin du périphérique détecté (par exemple, `/dev/sdb`) dans le fichier `usb_device_path.txt`.
- Exécute des vérifications de sécurité avec **SBGuard** et **evtest** pour détecter des périphériques HID malveillants.
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
- Utilise la commande `udisksctl` pour démonter et éteindre le périphérique en toute sécurité.
- Enregistre les événements et erreurs dans `logs.txt`.

### `usb_device_path.txt`
Ce fichier temporaire contient le chemin du périphérique USB détecté par `detect.sh` (par exemple, `/dev/sdb`). Il est utilisé par les scripts de formatage (`fat32.sh`, `ext4.sh`, `ntfs.sh`) et d'éjection (`ejectUSB.sh`) pour identifier le périphérique à traiter.

### `usb_mount_path.txt`
Ce fichier temporaire contient le chemin de montage du périphérique USB détecté par `detect_mount.sh` (par exemple, `/media/usb`). Il est utilisé par `analyse.sh` pour analyser les fichiers du périphérique.

### `logs.txt`
Ce fichier contient les journaux générés par les scripts du dossier Backend. Il enregistre :
- Les événements importants, comme la détection, l'analyse et le formatage des périphériques.
- Les erreurs éventuelles ou les messages d'information.
- Les horodatages pour chaque action.

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

4. **Formatage d'un périphérique USB :**
   - Exécutez l'un des scripts de formatage (`fat32.sh`, `ext4.sh`, `ntfs.sh`) pour formater le périphérique détecté.
   - Les événements et erreurs seront enregistrés dans `logs.txt`.

5. **Éjection d'un périphérique USB :**
   - Exécutez `ejectUSB.sh` pour éjecter en toute sécurité le périphérique USB détecté.

6. **Vérification des logs :**
   - Consultez le fichier `logs.txt` pour suivre les actions effectuées par les scripts.

## Notes
- Assurez-vous que les scripts sont exécutés avec des privilèges root pour permettre le démontage, le formatage et l'éjection des périphériques.
- Les scripts de formatage ne demandent pas de confirmation avant de procéder. Assurez-vous que le périphérique détecté est celui que vous souhaitez formater.
- Les fichiers `usb_device_path.txt` et `usb_mount_path.txt` sont temporaires et sont recréés à chaque nouvelle détection de périphérique.