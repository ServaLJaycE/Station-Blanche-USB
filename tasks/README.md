# Tasks

Le dossier `tasks` contient des scripts essentiels pour le fonctionnement automatique de la station blanche USB. Ces scripts sont conçus pour être exécutés automatiquement, notamment via `cron`, afin de garantir le bon fonctionnement du système.

---

## Contenu des scripts

### 1. `start.sh`
Ce script est responsable de lancer l'application principale écrite en Python (utilisant Tkinter pour l'interface graphique). Il :
- Vérifie que le script est exécuté avec les privilèges root.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt` pour un suivi des événements.
- Exécute le fichier Python principal (`accueil.py`) en tant que root.

### 2. `check.sh`
Ce script vérifie l'intégrité du fichier `start.sh` en le comparant à une version de référence (`start_reference.sh`). Il :
- Calcule les empreintes de hachage (SHA-256) des deux fichiers.
- Remplace `start.sh` par la version de référence si une modification est détectée.
- Exécute ensuite `start.sh` en tant que root.
- Redirige toutes les sorties (stdout et stderr) vers le fichier `logs.txt`.

### 3. `start_reference.sh`
Ce fichier est une copie de référence de `start.sh`. Il est utilisé par `check.sh` pour vérifier si `start.sh` a été modifié. Toute modification de `start.sh` sera remplacée par ce fichier.

> **Note importante :** Pour protéger ce fichier contre toute modification, utilisez la commande suivante :
> ```bash
> sudo chattr +i start_reference.sh
> ```

### 4. `logs.txt`
Ce fichier contient les journaux générés par les scripts `start.sh` et `check.sh`. Il enregistre :
- Les événements importants, comme les vérifications et les exécutions.
- Les erreurs éventuelles ou les messages d'information.
- Les horodatages pour chaque action.

---

## Configuration automatique avec `cron`

Les scripts de ce dossier sont conçus pour être exécutés automatiquement via `cron`. Voici les étapes pour configurer `cron` :

1. **Ajout des tâches `cron` :**
   - Exécutez le script d'installation avec l'option `--complete` pour configurer automatiquement les tâches `cron` :
     ```bash
     sudo ./install.sh --complete
     ```

2. **Tâches configurées :**
   - `check.sh` : Exécuté  pour vérifier l'intégrité de `start.sh` et lancer l'application.
   - `start.sh` : Exécuté automatiquement au démarrage du système.

3. **Vérification des tâches `cron` :**
   - Pour vérifier que les tâches ont été correctement ajoutées, utilisez la commande suivante :
     ```bash
     sudo crontab -l
     ```
   - Vous devriez voir la ligne suivantes :
     ```bash
     @reboot bash /usr/share/projet/tasks/start.sh
     ```

---

## Notes importantes

- **Protection de `start_reference.sh` :**
  - Pour éviter toute modification accidentelle ou malveillante, utilisez la commande suivante :
    ```bash
    sudo chattr +i start_reference.sh
    ```

- **Logs :**
  - Les journaux des scripts sont enregistrés dans `logs.txt`. Vous pouvez consulter ce fichier pour diagnostiquer les problèmes ou suivre les actions effectuées.

---

## Résumé des scripts

| Script               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `start.sh`           | Lance l'application principale (`accueil.py`) avec les privilèges root.    |
| `check.sh`           | Vérifie l'intégrité de `start.sh` et le remplace si nécessaire.            |
| `start_reference.sh` | Copie de référence utilisée pour vérifier l'intégrité de `start.sh`.       |
| `logs.txt`           | Fichier contenant les journaux des scripts `start.sh` et `check.sh`.       |

---