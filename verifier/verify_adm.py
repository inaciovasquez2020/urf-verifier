import json
import hashlib
import sys
import os
from jsonschema import Draft202012Validator

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def resolve(path):
    if os.path.isabs(path):
        return path
    return os.path.join(ROOT, path)

def main():
    if len(sys.argv) != 3:
        print("usage: verify_adm.py <adm_schema.json> <adm_certificate.json>")
        sys.exit(2)

    schema_path = resolve(sys.argv[1])
    cert_path = resolve(sys.argv[2])

    with open(schema_path) as f:
        schema = json.load(f)

    with open(cert_path) as f:
        cert = json.load(f)

    Draft202012Validator(schema).validate(cert)

    for artifact in cert["evidence"]["artifacts"]:
        path = resolve(artifact["path"])
        declared = artifact["sha256"]
        computed = sha256_file(path)
        if declared != computed:
            print(f"hash mismatch: {artifact['path']}")
            sys.exit(1)

    print("ADMISSIBLE")

if __name__ == "__main__":
    main()

