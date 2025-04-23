#!/bin/bash

# Exécute hash.sh et attend qu'il se termine
bash "/usr/share/projet/backend/hash.sh"
wait

# Exécute analyse.sh après la fin de hash.sh
bash "/usr/share/projet/backend/analyse.sh"
exit_code=$?

if [ $exit_code -eq 1 ]; then
    bash "/usr/share/projet/backend/hash.sh"
    wait
    python3 /usr/share/projet/frontend/analyse_bad.py
    pkill -f main_interface.py

elif [ $exit_code -eq 0 ]; then
    bash "/usr/share/projet/backend/hash.sh"
    wait
    echo "redirection vers analyse_good.py [pre_analyse.sh]"
    python3 /usr/share/projet/frontend/analyse_good.py
    pkill -f main_interface.py
fi
