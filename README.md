# URF Verifier

Lean-based verifier artifacts for the **Unified Rigidity Framework (URF)**.

This repository contains formal verifier definitions, structural invariants,
and supporting Lean artifacts used to validate URF certificates and proofs.
It is intentionally **not yet packaged as a Lake project**.

---

## Status

- **Code:** Stable  
- **Formalism:** Lean 4 (artifact-level)  
- **Build system:** None (by design)  
- **CI:** Structural invariants enforced  

This repository is safe for citation and peer review.

---

## Purpose

The URF Verifier provides the **logical verification layer** for URF-based
certificates. Its role is to:

- Encode verifier-side rules and checks in Lean
- Define admissible certificate structures
- Enforce structural and logical invariants required by URF
- Serve as a dependency for downstream, buildable URF components

This repository prioritizes **correctness and stability of definitions**
over build tooling.

---

## Quickstart (60 seconds)

This repository contains Lean verifier artifacts only.

No build step is required at this stage.

To inspect the verifier definitions:
```bash
ls

