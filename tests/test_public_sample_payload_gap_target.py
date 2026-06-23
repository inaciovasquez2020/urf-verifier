import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_public_sample_payload_gap_target_verifier():
    result = subprocess.run(
        [sys.executable, "scripts/verify_public_sample_payload_gap_target.py"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    assert "PUBLIC_SAMPLE_PAYLOAD_GAP_TARGET_OK" in result.stdout
