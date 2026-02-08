URF Verifier
This repository provides the canonical, deterministic verifier for Unified Rigidity Framework certificates.
Scope
The verifier checks URF certificates against frozen admissibility axioms and returns a reproducible verdict. It is designed to be audit-safe, hash-stable, and replayable across machines and CI environments.
What this is
A strict verifier. It does not search, optimize, or infer.
A boundary checker. It rejects near-violations deterministically.
A trust anchor. All higher-level URF claims reduce to this tool.
What this is not
Not a solver
Not a heuristic analyzer
Not an interactive assistant
Determinism contract
Given identical inputs, hashes, and schema versions, the verifier output is identical bit-for-bit.
Repository contents
schema JSON Schemas defining admissible URF certificates
verifier Reference verifier implementation
tests Boundary and adversarial test certificates
replay Deterministic replay scripts and hash logs
Versioning
Schema and verifier versions are locksteped.
Breaking changes require a new major version.
Status
v1.0.0-initial
License
MIT
