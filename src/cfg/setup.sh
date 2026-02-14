#!/bin/bash

cd "src/cfg"

python3 -m venv .metsa

source .metsa/bin/activate

pip install matplotlib pandas

echo "1" > "setup_flag.dat"

