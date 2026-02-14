#!/bin/bash

SETUP_FLAG="src/cfg/setup_flag.dat"
SETUP_FILE="src/cfg/setup.sh"

FLAG=$(tr -d '[:space:]' < "$SETUP_FLAG")

if [[ "$FLAG" != "1" ]]; then
    echo "Iniciando configuración inicial"

    chmod +x "$SETUP_FILE"
    ./"$SETUP_FILE"    
fi

pwd
RUTA=$(pwd)

RUTA_EJECUTAR="${RUTA}/src" 

cd $RUTA_EJECUTAR

python3 GUI.py

