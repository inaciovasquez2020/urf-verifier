#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 2 ]; then
echo "usage: replay.sh <schema.json> <certificate.json>"
exit 2
fi
SCHEMA="$1"
CERT="$2"
python3 verifier/verify.py "$SCHEMA" "$CERT"
