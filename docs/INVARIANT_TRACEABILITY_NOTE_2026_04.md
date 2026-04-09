# Invariant Traceability Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository validates claimed invariants against published artifacts.

## Weakest structural extension
Let
\[
C
\]
be a claimed invariant validation,
\[
A
\]
the artifact bundle,
\[
R_\ast
\]
the frozen URF-Core release,
and
\[
V_\ast
\]
the verifier revision.

The minimal traceability condition is:
\[
C\text{ is canonical}
\Longrightarrow
C \leftrightarrow (A,R_\ast,V_\ast)
\]
with a unique linked witness triple.

## Minimal next artifact
The weakest next artifact is an executable traceability audit emitting:
1. validated invariant claims lacking artifact references;
2. claims lacking frozen-release provenance;
3. claims lacking verifier-revision provenance;
4. claims mapping to multiple inconsistent witness triples.

## Label
This note is CONDITIONAL.
It preserves the repository's verifier-only scope.
