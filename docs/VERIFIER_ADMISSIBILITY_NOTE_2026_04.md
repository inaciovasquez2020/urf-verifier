# Verifier Admissibility Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository is verifier-only.
It contains:
1. artifact verification tooling;
2. checksum recomputation;
3. invariant validation against published artifacts.

It does not contain:
1. theory;
2. discovery;
3. modification of URF-Core.

## Weakest structural extension
Let
\[
A
\]
be a declared artifact bundle,
\[
R_\ast
\]
the frozen URF-Core release this repository depends on,
and
\[
V(A,R_\ast)\in\{\mathrm{pass},\mathrm{fail}\}
\]
the verifier outcome.

The minimal admissibility condition is:
\[
V(A,R_\ast)=\mathrm{pass}
\Longrightarrow
A \text{ is evaluated against the exact frozen release } R_\ast.
\]

Equivalently, if
\[
R\neq R_\ast,
\]
then any outcome must be marked non-canonical.

## Minimal next artifact
The weakest next artifact is an executable admissibility audit emitting:
1. verification runs lacking frozen-release provenance;
2. checksums computed against non-canonical artifact sets;
3. invariant validations lacking release-pin metadata;
4. pass results produced outside the declared verifier boundary.

## Label
This note is CONDITIONAL.
It preserves the repository's verifier-only scope.
