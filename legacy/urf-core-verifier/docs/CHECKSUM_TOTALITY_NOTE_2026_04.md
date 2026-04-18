# Checksum Totality Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository recomputes checksums for artifact bundles.

## Weakest structural extension
Let
\[
\mathcal A
\]
be the declared artifact scope and
\[
H:\mathcal A\to \mathcal D
\]
the checksum map into digests.

The minimal totality condition is:
\[
\forall A\in\mathcal A,\quad H(A)\text{ is defined and unique.}
\]

The minimal traceback condition is:
\[
\forall d\in \operatorname{im}(H),\quad \exists! A\in\mathcal A\text{ such that }H(A)=d.
\]

## Minimal next artifact
The weakest next artifact is an executable checksum audit emitting:
1. artifacts in scope lacking checksums;
2. duplicate digests with ambiguous artifact identity;
3. checksum reports not mapping to a concrete artifact bundle;
4. artifact bundles declared canonical but excluded from checksum coverage.

## Label
This note is CONDITIONAL.
It preserves the repository's verifier-only scope.
