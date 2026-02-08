#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [ "$#" -ne 2 ]; then
echo "usage: replay.sh <schema.json> <certificate.json>"
exit 2
fi
SCHEMA="$ROOT/$1"
CERT="$ROOT/$2"
python3 "$ROOT/verifier/verify.py" "$SCHEMA" "$CERT"
