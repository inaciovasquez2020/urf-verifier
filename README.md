This repository ships verifier logic, signature examples, and the public key.
It does not currently ship a sample certificate payload or matching hash payload.
To run the verifier locally, provide your own certificate artifacts under `certs/`.


## Quickstart

Run the included boundary check from the repository root with Python 3:

```bash
python3 scripts/verify_verifier_boundary_certificate.py
```

The check reports whether the required public files and boundary declaration are present. For signed certificate verification, follow [Quickstart](QUICKSTART.md).

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

For `./scripts/verify_cert.sh certs/YOUR_CERT.json`, install `minisign` and ensure `shasum` is available. Provide:

- `certs/YOUR_CERT.json`
- `certs/YOUR_CERT.hash`
- `certs/YOUR_CERT.hash.minisig`
- `keys/aiv_pub.key`

## External status

This repository is governed by [`docs/status/EXTERNAL_STATUS_LOCK.md`](docs/status/EXTERNAL_STATUS_LOCK.md). Build success, CI success, dashboards, ledgers, axioms, admits, `sorry`, or placeholder witnesses do not constitute theorem-level closure.
