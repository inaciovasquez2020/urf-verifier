# Contributing to URF Verifier

This repository is the authoritative verifier surface for URF certificates, provenance validation, and deterministic reproducibility checks.

## Contribution classes

### 1. Documentation improvements

- clarify onboarding wording
- improve navigation across verifier surfaces
- tighten quickstart and setup text
- fix broken or ambiguous references

### 2. Verification and reproducibility hardening

- improve certificate checks
- tighten schema-facing validation
- strengthen provenance documentation
- harden verifier and status consistency

### 3. Scope or authority changes

These require explicit justification.

- changing verifier-authority language
- changing scope-limitations wording
- expanding claims beyond deterministic verification infrastructure
- altering canonical verifier role declarations

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run repository tests before commit:

```bash
python3 -m pytest -q
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- changing verifier-authority language without synchronized documentation updates
- expanding scope or status claims without updating scope-limitations surfaces
