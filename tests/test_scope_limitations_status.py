from pathlib import Path

def test_scope_limitations_status():
    text = Path("SCOPE_LIMITATIONS_STATUS.md").read_text(encoding="utf-8")
    assert "- canonical" in text
    assert "- verifier-infrastructure-layer" in text
    assert "- stable" in text
    assert "- release-certified" in text
    assert "- deterministic" in text
    assert "- not theorem-prover-complete" in text
    assert "- not a primary mathematics-closure repository" in text
    assert "no live missing-math theorem lock" in text
    assert "verifier-surface hardening and audit reproducibility depth" in text

def test_readme_scope_sync():
    readme = Path("README.md").read_text(encoding="utf-8")
    scope = Path("SCOPE_LIMITATIONS_STATUS.md").read_text(encoding="utf-8")
    assert "## Current Status" in readme
    assert "- verifier-infrastructure-layer" in readme
    assert "- stable" in readme
    assert "- release-certified" in readme
    assert "- deterministic" in readme
    assert "- not theorem-prover-complete" in readme
    assert "does not generate proofs" in readme
    assert "SCOPE_LIMITATIONS_STATUS.md" in readme
    assert "verification tooling for Unified Rigidity Framework artifacts" in scope
