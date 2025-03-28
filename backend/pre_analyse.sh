#!/bin/bash

# Exécute hash.sh et attend qu'il se termine
bash "hash.sh"
wait

# Exécute analyse.sh après la fin de hash.sh
bash "analyse.sh"
wait
if [ $? -eq 1 ]; then
    python3 ../Backend/analyse_bad.py
    pkill -f main_interface.py

elif [ $? -eq 0 ]; then
    python3 ../Backend/analyse_good.py
    pkill -f main_interface.py
fi