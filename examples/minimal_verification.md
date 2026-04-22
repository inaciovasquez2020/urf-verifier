# Minimal Verification Example

Minimal local workflow:

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -q
```

To run the certificate verifier itself, provide your own certificate
payload and matching supporting artifacts under `certs/`, then run:

```bash
./scripts/verify_cert.sh certs/YOUR_CERT.json
```
