# Frozen Release Provenance Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository depends on a frozen URF-Core release.

## Weakest structural extension
Let
\[
R_\ast
\]
be the declared frozen release and
\[
P
\]
a verifier pass result.

The minimal provenance condition is:
\[
P\text{ is canonical}
\Longrightarrow
P \text{ names } R_\ast \text{ explicitly}.
\]

If a run omits
\[
R_\ast,
\]
then the run must be marked non-canonical.

## Minimal next artifact
The weakest next artifact is an executable provenance audit emitting:
1. pass results without release identifiers;
2. release identifiers not matching the declared frozen release;
3. reports with ambiguous or multiple release references;
4. canonical labels applied to unpinned runs.

## Label
This note is CONDITIONAL.
It preserves the repository's verifier-only scope.
