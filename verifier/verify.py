import json
import hashlib
import sys
from jsonschema import Draft202012Validator
def sha256_file(path):
h = hashlib.sha256()
with open(path, "rb") as f:
for chunk in iter(lambda: f.read(8192), b""):
h.update(chunk)
return h.hexdigest()

def sha256_bytes(b):
return hashlib.sha256(b).hexdigest()

def main():
if len(sys.argv) != 3:
print("usage: verify.py <schema.json> <certificate.json>")
sys.exit(2)

schema_path = sys.argv[1]
cert_path = sys.argv[2]

with open(schema_path) as f:
    schema = json.load(f)

with open(cert_path, "rb") as f:
    cert_bytes = f.read()
    cert = json.loads(cert_bytes)

Draft202012Validator(schema).validate(cert)

computed_cert_hash = sha256_bytes(cert_bytes)
declared_cert_hash = cert["hashes"]["certificate_sha256"]

if computed_cert_hash != declared_cert_hash:
    print("hash mismatch: certificate")
    sys.exit(1)

for artifact in cert["evidence"]["artifacts"]:
    path = artifact["path"]
    declared = artifact["sha256"]
    computed = sha256_file(path)
    if declared != computed:
        print(f"hash mismatch: {path}")
        sys.exit(1)

print("VERIFIED")
print(f"certificate_sha256={computed_cert_hash}")
if name == "main":
main()
