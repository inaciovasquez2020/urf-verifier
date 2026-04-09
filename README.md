URF-Core Verifier

This repository contains verifier-only tooling for URF-Core.

Scope:
- Verify artifacts produced under URF-Core
- Recompute checksums
- Validate claimed invariants against published artifacts


## Conditional note
- `docs/VERIFIER_ADMISSIBILITY_NOTE_2026_04.md` — conditional note specifying the weakest release-pin admissibility audit compatible with the repository's verifier-only scope.


## Conditional notes
- `docs/FROZEN_RELEASE_PROVENANCE_NOTE_2026_04.md` — conditional note specifying the weakest frozen-release provenance audit compatible with the repository's verifier-only scope.
- `docs/CHECKSUM_TOTALITY_NOTE_2026_04.md` — conditional note specifying the weakest checksum totality audit compatible with the repository's verifier-only scope.
- `docs/INVARIANT_TRACEABILITY_NOTE_2026_04.md` — conditional note specifying the weakest invariant claim traceability audit compatible with the repository's verifier-only scope.
- `docs/VERIFIER_VERSION_ADMISSIBILITY_NOTE_2026_04.md` — conditional note specifying the weakest verifier-revision admissibility audit compatible with the repository's verifier-only scope.
- `docs/NON_GOAL_OVERREACH_NOTE_2026_04.md` — conditional note specifying the weakest non-overreach audit compatible with the repository's explicit non-goal boundary.

Non-goals:
- No theory
- No discovery
- No modification of URF-Core

This repo depends on a frozen URF-Core release.
