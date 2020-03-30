#!/usr/bin/env bash
set -exuo pipefail
dvc config core.no_scm True

# updata source data
dvc update COVID-19.csv.dvc

# update README.md
src/readme.sh

# update gist
python covid19.py -c "$INPUT_COUNTRIES" -o covid-19.txt
cat covid-19.txt # print here
cat covid-19.txt | python src/gistup.py
