# Canonical Verifier Lock

Status: Conditional

This repository defines the URF verification layer.

Constraints:

1. All artifacts must be evaluated deterministically under the verifier.
2. Verification must be reproducible under CI without external state.
3. The verifier does not upgrade or reinterpret mathematical claims beyond declared evidence.
4. No completeness or global soundness claim is valid without a formal meta-proof.

Do not promote beyond Conditional on repository-surface evidence alone.
