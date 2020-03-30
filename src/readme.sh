#!/usr/bin/env bash
set -exuo pipefail

dvc repro world.txt.dvc

README="$(cat README.md)"
echo "$README" | head -n5
cat world.txt
echo "$README" | tail -n+18
