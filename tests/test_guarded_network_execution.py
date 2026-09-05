from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import guarded_network_execution as guarded


def test_denied_capability_never_calls_opener(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(guarded, "verify_signed_network_capability", lambda **_: False)

    opener_calls: list[object] = []

    def forbidden_opener(*args: object, **kwargs: object) -> object:
        opener_calls.append((args, kwargs))
        raise AssertionError("network opener must not be called when capability is denied")

    with pytest.raises(guarded.NetworkCapabilityDenied):
        guarded.guarded_http_post(
            target="https://example.invalid/endpoint",
            body=b"payload",
            token_path="missing-token.json",
            signature_path="missing-token.minisig",
            public_key_path="missing-pub.key",
            opener=forbidden_opener,
        )

    assert opener_calls == []
