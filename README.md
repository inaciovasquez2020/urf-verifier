This repository ships verifier logic, signature examples, and the public key.
It does not currently ship a sample certificate payload or matching hash payload.
To run the verifier locally, provide your own certificate artifacts under `certs/`.


AIV Standard (v1.0)

Quickstart
  ./scripts/verify_cert.sh certs/YOUR_CERT.json

Artifacts
- standard/AIV_STANDARD_v1.md
- schema/aiv-cert.schema.json
- certs/YOUR_CERT.json
- dist/AIV_Founding_Standard_v1.pdf

## Current Status

- canonical
- verifier-infrastructure-layer
- stable
- release-certified
- deterministic
- not theorem-prover-complete
- not a primary mathematics-closure repository

This repository is verifier infrastructure for URF artifacts.
It does not generate proofs, establish mathematical truth, or serve as the canonical location
for final theorem closure of URF mathematics.

## Canonical Scope Pointer

See `SCOPE_LIMITATIONS_STATUS.md` for the authoritative scope and limitations surface.

## Citation

Canonical citation:

> Vasquez, Inacio. *urf-verifier*. GitHub repository. Version main. 2026-04-20.

Machine-readable metadata:

- `CITATION.cff`
- `CITATION.json`
- `ATTRIBUTION.md`

## Input artifacts

To run the verifier locally, provide:

- `certs/YOUR_CERT.json`
- `certs/YOUR_CERT.hash`
- `certs/YOUR_CERT.json.sig`
- `certs/YOUR_CERT.hash.sig`
- `keys/aiv_pub.key`

## External status

This repository is governed by [`docs/status/EXTERNAL_STATUS_LOCK.md`](docs/status/EXTERNAL_STATUS_LOCK.md). Build success, CI success, dashboards, ledgers, axioms, admits, `sorry`, or placeholder witnesses do not constitute theorem-level closure.
