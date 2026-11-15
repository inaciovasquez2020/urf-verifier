# URF biological data-integrity verifier — bounded research prototype

**Status: conditional integration candidate.** This component is not a Lean theorem, universal verifier, macrophage annotation, clinical diagnostic, or independent scientific replication.

## Interfaces

- `audit_cells` checks that a cleaned candidate cell-ID set is disjoint from **supplied known malignant IDs**. It cannot detect unlabelled malignant cells or independently establish macrophage identity.
- `exact_test` enumerates finite patient-level response-label assignments for a specified difference-of-means statistic. Python floating-point arithmetic and a conservative scaled near-tie tolerance are used: **exact enumeration does not mean exact rational arithmetic**. A guard rejects more than 2,000,000 assignments.
- `audit_aggregate` checks internally consistent numerator/denominator/p-value triples against `math.comb(n, responders)`. It cannot reproduce a numerator without the patient-level measurements; unfamiliar statistic fields are not validated.

## Source and evidence boundary

Public source: `inaciovasquez2020/biological-friction-framework`, exact source commit `510bc502d67e6ac5289f56d2b73a44f2ba6bd313`, under `research/melanoma/cd36-paired-baseline-2026-11-15`.

Five aggregate permutation triples were checked for arithmetic consistency. The corrected primary 288/495 result is documented separately in `METHOD_RECONCILIATION_2026_11_15.md`, but cannot be independently recomputed from the public aggregate file. Patient-level recomputation: **NOT_RUN**. Macrophage annotation: **OPEN**. External clinical replication: **NOT_RUN**. A universal mathematical URF transfer theorem: **OPEN**.

## Validation

Run `python3 -m pytest -q tests/test_urf_bio_data_integrity.py` from the repository root. A passing test suite demonstrates the fixture behaviors only, not correctness for all input datasets. Resource-guard aborts are **INCOMPLETE**, never PASS.

No raw patient-level data, cell IDs, or source RNA sequencing files are stored in this module or tests.
