# Verifier Version Admissibility Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository is itself a verifier and therefore part of the provenance of any canonical pass result.

## Weakest structural extension
Let
\[
V_\ast
\]
be the canonical verifier revision.

For any reported result
\[
P,
\]
the minimal version-admissibility condition is:
\[
P\text{ is canonical}
\Longrightarrow
P \text{ was produced by } V_\ast.
\]

If
\[
V\neq V_\ast,
\]
then the result must be marked non-canonical or experimental.

## Minimal next artifact
The weakest next artifact is an executable version audit emitting:
1. pass results lacking verifier revision identifiers;
2. runs from dirty working trees;
3. reports generated from untagged or unmatched verifier revisions;
4. canonical labels applied to non-canonical verifier states.

## Label
This note is CONDITIONAL.
It preserves the repository's verifier-only scope.
