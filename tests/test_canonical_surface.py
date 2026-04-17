from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_surface_files():
    req = [
        "README.md",
        "STATUS.md",
        "FREEZE.md",
        ".gitignore",
        ".github/workflows/canonical-surface.yml",
    ]
    for r in req:
        assert (ROOT / r).exists(), r

def test_readme_mentions_reproduce_scope():
    t = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    assert "reproduc" in t or "verification" in t or "urf" in t

def test_scope_language():
    s = (ROOT / "STATUS.md").read_text(encoding="utf-8").lower()
    assert "repository" in s
    assert "scope" in s
    assert "reproducibility" in s
