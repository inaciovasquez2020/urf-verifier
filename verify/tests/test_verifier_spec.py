from pathlib import Path

def test_verifier_spec_exists():
    assert Path("docs/VERIFIER_SPEC.md").exists()

def test_minimal_example_exists():
    assert Path("examples/minimal_verification.md").exists()
