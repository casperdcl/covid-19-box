#!/usr/bin/env bash
set -exuo pipefail
dvc config core.no_scm True
dvc update COVID-19.csv.dvc
exec python covid19.py -c "$INPUT_COUNTRIES" -o stdout.txt
