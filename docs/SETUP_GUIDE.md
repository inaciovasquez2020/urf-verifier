# Setup Guide

This guide is for contributors who want a reliable local environment for URF Verifier.

## Prerequisites

```bash
python3 --version
git --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/urf-verifier.git
cd urf-verifier
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Local verification model

The repository currently includes:

- signature examples under `certs/`
- the public key under `keys/`
- verifier code under `scripts/`

It does not currently include a sample certificate payload plus hash payload.

To run the verifier locally, provide:

- `certs/YOUR_CERT.json`
- `certs/YOUR_CERT.hash`
- `certs/YOUR_CERT.json.sig`
- `certs/YOUR_CERT.hash.sig`

Then run:

```bash
./scripts/verify_cert.sh certs/YOUR_CERT.json
```

## Tests

```bash
python3 -m pytest -q
```

## Recommended edit loop

```bash
git pull --ff-only origin main
python3 -m pytest -q
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `README.md`
- `SCOPE_LIMITATIONS_STATUS.md`
- `schema/aiv-cert.schema.json`
- `certs/`
- `keys/`
