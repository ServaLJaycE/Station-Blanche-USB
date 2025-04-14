#!/bin/bash

# Exécute hash.sh et attend qu'il se termine
bash "hash.sh"
wait

# Exécute analyse.sh après la fin de hash.sh
bash "analyse.sh"
wait
if [ $? -eq 1 ]; then
    bash "hash.sh"
    wait
    python3 usr/share/projet/frontend/analyse_bad.py
    pkill -f main_interface.py

elif [ $? -eq 0 ]; then
    bash "hash.sh"
    wait
    python3 usr/share/projet/frontend/analyse_good.py
    pkill -f main_interface.py
fi