# URF Verifier Quickstart

This is the shortest path from clone to a first successful local verifier pass.

## Requirements

- `git`
- `bash`
- `python3`

## 1. Clone

```bash
git clone https://github.com/inaciovasquez2020/urf-verifier.git
cd urf-verifier
```

## 2. Check tools

```bash
python3 --version
git --version
```

## 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## 4. Inspect shipped artifacts

```bash
ls -la certs keys
```

## 5. Run the verifier with your own certificate payload

The repository currently ships signature examples and the public key,
but not a sample certificate payload or matching hash payload.

Provide these files:

- `certs/YOUR_CERT.json`
- `certs/YOUR_CERT.hash`
- `certs/YOUR_CERT.json.sig`
- `certs/YOUR_CERT.hash.sig`
- `keys/aiv_pub.key`

Then run:

```bash
./scripts/verify_cert.sh certs/YOUR_CERT.json
```

## 6. Run tests

```bash
python3 -m pytest -q
```

## 7. Review main verifier surfaces

- `README.md`
- `SCOPE_LIMITATIONS_STATUS.md`
- `schema/aiv-cert.schema.json`
- `certs/`
- `keys/`
- `docs/`
