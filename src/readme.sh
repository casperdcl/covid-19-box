#!/usr/bin/env bash
set -exuo pipefail
src="$(realpath "$(dirname "${0}")")"
pushd "$src"/..

dvc repro world.txt.dvc

set +x
README="$(cat README.md)"
(
  echo "$README" | head -n5
  cat world.txt
  echo "$README" | tail -n+18
) > README.md
set -x

popd
