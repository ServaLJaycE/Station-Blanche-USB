# Backend

Ce dossier contient les scripts responsables des fonctionnalités principales de la station blanche USB. Ces scripts permettent de détecter, analyser, nettoyer et formater les périphériques USB connectés.

## Scripts

### `detect.sh`
Ce script détecte les périphériques USB insérés. Il :
- Effectue un scan toutes les 2 secondes pour détecter un nouveau périphérique.
- Enregistre le chemin du périphérique détecté dans le fichier `usb_device_path.txt`.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt` pour un suivi des événements.

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
- Utilise la commande `udisksctl` pour éjecter le périphérique en toute sécurité.

### `usb_device_path.txt`
Ce fichier temporaire contient le chemin du périphérique USB détecté par `detect.sh`. Il est utilisé par les scripts de formatage (`fat32.sh`, `ext4.sh`, `ntfs.sh`) pour identifier le périphérique à formater.
Ce fichier etant temporaire il n'existe qu'entre le moment d'injection de la clé, et l'éjection de celle-ci.

### `logs.txt`
Ce fichier contient les journaux générés par les scripts du dossier Backend. Il enregistre :
- Les événements importants, comme la détection et le formatage des périphériques.
- Les erreurs éventuelles ou les messages d'information.
- Les horodatages pour chaque action.

## Utilisation
1. **Détection d'un périphérique USB :**
   - Exécutez `detect.sh` pour détecter un périphérique USB inséré.
   - Le chemin du périphérique sera enregistré dans `usb_device_path.txt`.

2. **Formatage d'un périphérique USB :**
   - Exécutez l'un des scripts de formatage (`fat32.sh`, `ext4.sh`, `ntfs.sh`) pour formater le périphérique détecté.
   - Les événements et erreurs seront enregistrés dans `logs.txt`.

3. **Éjection d'un périphérique USB :**
   - Exécutez `ejectUSB.sh` pour éjecter en toute sécurité le périphérique USB détecté.

4. **Vérification des logs :**
   - Consultez le fichier `logs.txt` pour suivre les actions effectuées par les scripts.

## Notes
- Assurez-vous que les scripts sont exécutés avec des privilèges root pour permettre le démontage et le formatage des périphériques.
- Les scripts de formatage ne demandent pas de confirmation avant de procéder. Assurez-vous que le périphérique détecté est celui que vous souhaitez formater.