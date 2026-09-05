from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import signed_network_capability as snc


NOW = datetime(2026, 9, 5, 0, 0, tzinfo=timezone.utc)
TARGET = "https://timestamp.digicert.com"


def _write_inputs(tmp_path: Path, payload: object) -> tuple[Path, Path, Path]:
    token = tmp_path / "network-capability.json"
    signature = tmp_path / "network-capability.json.minisig"
    public_key = tmp_path / "aiv_pub.key"
    token.write_text(json.dumps(payload), encoding="utf-8")
    signature.write_text("test-signature", encoding="utf-8")
    public_key.write_text("test-public-key", encoding="utf-8")
    return token, signature, public_key


def _verify(tmp_path: Path, monkeypatch, payload: object, *, target: str = TARGET) -> bool:
    token, signature, public_key = _write_inputs(tmp_path, payload)
    monkeypatch.setattr(
        snc.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=0),
    )
    return snc.verify_signed_network_capability(
        token_path=token,
        signature_path=signature,
        public_key_path=public_key,
        expected_target=target,
        now=NOW,
    )


def test_signed_network_capability_accepts_only_matching_unexpired_payload(
    tmp_path: Path, monkeypatch
) -> None:
    valid = {
        "version": 1,
        "capability": "external_network",
        "target": TARGET,
        "expires_at": "2026-09-05T00:05:00Z",
    }
    assert _verify(tmp_path, monkeypatch, valid) is True

    rejected = [
        {**valid, "version": 2},
        {**valid, "capability": "filesystem_write"},
        {**valid, "target": "https://example.invalid"},
        {**valid, "expires_at": "2026-09-05T00:00:00Z"},
        {**valid, "expires_at": "not-a-timestamp"},
        {key: value for key, value in valid.items() if key != "expires_at"},
    ]
    for index, payload in enumerate(rejected):
        case_dir = tmp_path / f"case-{index}"
        case_dir.mkdir()
        assert _verify(case_dir, monkeypatch, payload) is False


def test_signed_network_capability_fails_closed_on_signature_or_verifier_failure(
    tmp_path: Path, monkeypatch
) -> None:
    payload = {
        "version": 1,
        "capability": "external_network",
        "target": TARGET,
        "expires_at": "2026-09-05T00:05:00Z",
    }
    token, signature, public_key = _write_inputs(tmp_path, payload)

    monkeypatch.setattr(
        snc.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=1),
    )
    assert snc.verify_signed_network_capability(
        token_path=token,
        signature_path=signature,
        public_key_path=public_key,
        expected_target=TARGET,
        now=NOW,
    ) is False

    def missing_minisign(*args, **kwargs):
        raise FileNotFoundError("minisign unavailable")

    monkeypatch.setattr(snc.subprocess, "run", missing_minisign)
    assert snc.verify_signed_network_capability(
        token_path=token,
        signature_path=signature,
        public_key_path=public_key,
        expected_target=TARGET,
        now=NOW,
    ) is False


def test_signed_network_capability_fails_closed_on_missing_inputs(
    tmp_path: Path,
) -> None:
    assert snc.verify_signed_network_capability(
        token_path=tmp_path / "missing-token.json",
        signature_path=tmp_path / "missing.minisig",
        public_key_path=tmp_path / "missing.pub",
        expected_target=TARGET,
        now=NOW,
    ) is False
