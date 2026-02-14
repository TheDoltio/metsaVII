#!/bin/bash

cd ../../data || exit 1

yr=$(date -u +"%Y")
mn=$(date -u +"%m")

mkdir -p "${yr}/${mn}"

