# Non-Goal Overreach Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository explicitly excludes:
1. theory;
2. discovery;
3. modification of URF-Core.

## Weakest structural extension
Let
\[
\mathcal V
\]
be the set of verifier-certified outputs and
\[
\mathcal T
\]
the set of broader theory or discovery claims.

The minimal non-overreach condition is:
\[
c\in\mathcal T\setminus\mathcal V
\Longrightarrow
c\text{ must not be presented as certified by this repository.}
\]

## Minimal next artifact
The weakest next artifact is an executable documentation audit emitting:
1. prose upgrading verifier outcomes into theory claims;
2. discovery language unsupported by artifact verification;
3. release notes implying URF-Core modification;
4. documentation omitting the declared verifier-only boundary.

## Label
This note is CONDITIONAL.
It preserves the repository's verifier-only scope.
