# URF Core Verifier Specification

## Purpose
The URF Core Verifier checks URF Core object properties against stated invariants.
It outputs a deterministic structured JSON result.

## Invariants Checked
- Structural well-formedness
- Axiom conformity
- Property bounds (if applicable)

## Output Contract
A JSON object with:
- `object_id`: unique identifier
- `verdict`: PASS | FAIL | INCONCLUSIVE
- `evidence`: structured details
- `timestamp`: ISO 8601
