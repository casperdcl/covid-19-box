#!/usr/bin/env bash
set -exuo pipefail
dvc config core.no_scm True

dvc update COVID-19.csv.dvc
python covid19.py -c "$INPUT_COUNTRIES" -o covid-19.txt
cat covid-19.txt

cat covid-19.txt | python gistup.py
