#!/usr/bin/env bash
set -euo pipefail

CORE_DIR="${1:-urf-core}"

if [ ! -f "$CORE_DIR/CHECKSUMS.txt" ]; then
  echo "CHECKSUMS.txt not found"
  exit 1
fi

cd "$CORE_DIR"
sha256sum -c CHECKSUMS.txt
