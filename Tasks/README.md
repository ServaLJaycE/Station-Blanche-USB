# Tasks

Ce dossier contient des scripts essentiels pour le fonctionnement automatique de la station blanche USB. Ces scripts sont conçus pour être exécutés automatiquement, notamment via le cron, afin de garantir le bon fonctionnement du système.


## Utilisation
Ces scripts sont conçus pour être exécutés automatiquement au démarrage du système via le cron. Ils garantissent que l'application principale est lancée correctement et que les fichiers critiques ne sont pas altérés.
Il est necessaire de les ajouter manuellement au Cron, avec les droits d'execution et d'écriture root.


### `start.sh`
Ce script est responsable de lancer l'application principale écrite en Python (utilisant Tkinter pour l'interface graphique). Il :
- Vérifie que le script est exécuté avec les privilèges root.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt` pour un suivi des événements.
- Exécute le fichier Python spécifié (`le_fichier.py`) en tant que root.

### `check.sh`
Ce script vérifie l'intégrité du fichier `start.sh` en le comparant à une version de référence (`start_reference.sh`). Il :
- Calcule les empreintes de hachage (SHA-256) des deux fichiers.
- Remplace `start.sh` par la version de référence si une modification est détectée.
- Exécute ensuite `start.sh` en tant que root.
- Redirige également toutes les sorties vers le fichier `logs.txt`.

### `start_reference.sh`
**/!\ Veuillez changer les permissions de ce fichier avec la commande suivante, avant de rendre toute modification impossible :**
```cmd
chattr +i start_reference.sh
```
Ce fichier est une copie de référence de `start.sh`. Il est utilisé par `check.sh` pour vérifier si `start.sh` a été modifié. Toute modification de `start.sh` sera remplacée par ce fichier.

### `logs.txt`
Ce fichier contient les journaux générés par les scripts `start.sh` et `check.sh`. Il enregistre :
- Les événements importants, comme les vérifications et les exécutions.
- Les erreurs éventuelles ou les messages d'information.
- Les horodatages pour chaque action.


