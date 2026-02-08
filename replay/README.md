Deterministic Replay
This directory provides a one-command, deterministic replay path for URF verification.
Usage
./replay.sh <schema.json> <certificate.json>
Contract
No network access
No nondeterminism
Identical inputs yield identical outputs
Exit codes
0 verified
1 hash mismatch
2 usage error
