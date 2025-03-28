# Frontend

Ce dossier contient le code responsable de l'interface utilisateur (GUI) de la station blanche USB. Il permet aux utilisateurs d'interagir avec les fonctionnalités proposées par le backend de manière intuitive et conviviale.

## Prérequis
- **Python** : Assurez-vous d'avoir Python 3.8 ou une version ultérieure installée sur votre machine.
  - Pour vérifier votre version de Python, exécutez :
    ```bash
    python3 --version
    ```
- **Bibliothèques nécessaires** : Les scripts utilisent `tkinter`, qui est inclus par défaut avec Python. Aucun package supplémentaire n'est requis.

## Scripts
### `accueil.py`
Ce script affiche une interface d'accueil qui invite l'utilisateur à insérer un périphérique USB. Il :
- Vérifie périodiquement si un périphérique USB a été détecté.
- Lance l'interface principale (`main_interface.py`) une fois un périphérique détecté.

### `main_interface.py`
Ce script lance l'interface principale de la station blanche USB. Il :
- Affiche un menu avec plusieurs options : analyser, formater, éjecter, ou quitter.
- Permet de naviguer vers d'autres interfaces en fonction des actions choisies.

### `format_interface.py`
Ce script affiche une interface permettant de choisir le format du périphérique USB. Il :
- Propose trois options de formatage : FAT32, NTFS, et EXT4.
- Permet de revenir à l'interface principale en cas d'annulation.

### `analyse_good.py`
Ce script affiche une interface indiquant qu'aucun virus n'a été détecté après l'analyse. Il :
- Permet de revenir à l'interface principale.

### `analyse_bad.py`
Ce script affiche une interface d'alerte lorsqu'un élément suspect est détecté. Il :
- Propose des options pour formater ou nettoyer le périphérique USB.
- Permet de revenir à l'interface principale en cas d'annulation.

### `end_clean_interface.py`
Ce script affiche une interface indiquant que le nettoyage du périphérique USB est terminé. Il :
- Permet de revenir à l'interface principale.

### `endFormat_interface.py`
Ce script affiche une interface indiquant le résultat du formatage du périphérique USB. Il :
- Affiche un message de succès ou d'échec.
- Permet de revenir à l'interface principale.

## Utilisation
1. **Lancement de l'interface principale :**
   - Exécutez `accueil.py` pour démarrer l'application.
   - Insérez un périphérique USB pour accéder au menu principal.

2. **Navigation entre les interfaces :**
   - Utilisez les boutons pour naviguer entre les différentes interfaces en fonction des actions souhaitées (analyse, formatage, nettoyage, etc.).

3. **Lancement d'une page spécifique :**
   - Pour tester une page spécifique, exécutez directement le script correspondant. Par exemple :
     ```bash
     python3 main_interface.py
     ```

## Notes
- Les interfaces sont conçues pour fonctionner en mode plein écran.
- Les scripts utilisent `tkinter` pour créer les interfaces graphiques.
- Assurez-vous que les scripts backend nécessaires sont disponibles pour exécuter les actions associées (analyse, formatage, etc.).