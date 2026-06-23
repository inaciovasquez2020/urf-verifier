#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

artifact_path = ROOT / "artifacts/verifier/public_sample_payload_gap_target_2026_06_23.json"
doc_path = ROOT / "docs/status/PUBLIC_SAMPLE_PAYLOAD_GAP_TARGET_2026_06_23.md"
readme_path = ROOT / "README.md"

for path in [artifact_path, doc_path, readme_path]:
    if not path.exists():
        raise SystemExit(f"MISSING_OBJECT := {path.relative_to(ROOT)}")

artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
doc = doc_path.read_text(encoding="utf-8")
readme = readme_path.read_text(encoding="utf-8")

readme_required = [
    "does not currently ship a sample certificate payload or matching hash payload",
    "It does not generate proofs, establish mathematical truth",
    "do not constitute theorem-level closure",
]

for token in readme_required:
    if token not in readme:
        raise SystemExit(f"missing README boundary token: {token}")

assert artifact["object"] == "PublicSamplePayloadGapTarget"
assert artifact["status"] == "PUBLIC_SAMPLE_PAYLOAD_GAP_TARGET_ONLY"
assert artifact["theorem_closure"] is False
assert artifact["proof_claim"] is False
assert artifact["minimal_missing_object"] == "PublicSampleCertificatePayloadAndHashPair"

present_signature_files = [
    "certs/AIV_CERT_CLAIM_0001.json.sig",
    "certs/AIV_CERT_CLAIM_0001.hash.sig",
]

missing_payload_files = [
    "certs/AIV_CERT_CLAIM_0001.json",
    "certs/AIV_CERT_CLAIM_0001.hash",
]

assert artifact["currently_present_signature_files"] == present_signature_files
assert artifact["currently_missing_payload_files"] == missing_payload_files

for rel in present_signature_files:
    if not (ROOT / rel).exists():
        raise SystemExit(f"missing expected signature file: {rel}")

for rel in missing_payload_files:
    if (ROOT / rel).exists():
        raise SystemExit(f"payload unexpectedly present; target is superseded: {rel}")

required_future_outputs = [
    "public sample certificate payload",
    "matching public hash payload",
    "sample-payload verifier entry point",
    "README quickstart that runs against the checked-in sample payload",
]

for token in required_future_outputs:
    if token not in artifact["required_future_outputs"]:
        raise SystemExit(f"missing required future output: {token}")

required_non_claims = [
    "does not add a sample certificate payload",
    "does not add a matching hash payload",
    "does not verify a real certificate payload",
    "does not generate proofs",
    "does not establish mathematical truth",
    "does not claim theorem-level closure",
    "does not claim external validation or peer-reviewed acceptance",
]

for token in required_non_claims:
    if token not in artifact["non_claims"]:
        raise SystemExit(f"missing non-claim: {token}")

required_doc_tokens = [
    "Status: `PUBLIC_SAMPLE_PAYLOAD_GAP_TARGET_ONLY`",
    "`PublicSamplePayloadGapTarget`",
    "`PublicSampleCertificatePayloadAndHashPair`",
    "`certs/AIV_CERT_CLAIM_0001.json.sig`",
    "`certs/AIV_CERT_CLAIM_0001.hash.sig`",
    "`certs/AIV_CERT_CLAIM_0001.json`",
    "`certs/AIV_CERT_CLAIM_0001.hash`",
    "public sample certificate payload",
    "matching public hash payload",
    "sample-payload verifier entry point",
    "does not claim theorem-level closure",
]

for token in required_doc_tokens:
    if token not in doc:
        raise SystemExit(f"missing doc token: {token}")

print("PUBLIC_SAMPLE_PAYLOAD_GAP_TARGET_OK")
