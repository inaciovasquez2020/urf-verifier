#!/usr/bin/env bash
set -euo pipefail

SUB=urf-counterexamples

if [[ ! -d "$SUB" ]]; then
  echo "ERROR: submodule $SUB not found"
  exit 1
fi

git submodule update --init --recursive

cd "$SUB"
git fetch origin
git checkout origin/main
NEW_SHA=$(git rev-parse --short HEAD)
cd ..

git add "$SUB"
git commit -m "chore(submodule): bump urf-counterexamples to ${NEW_SHA}"
