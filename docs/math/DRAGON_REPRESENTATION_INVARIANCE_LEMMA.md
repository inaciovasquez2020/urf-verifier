
# DraG0n Representation-Invariance Lemma

## Status

LOCKED

## Statement

Let (D) and (D') be equivalent encodings of the same diagnostic state under the admissible representation equivalence relation (D \sim D').
Assume the component scores (S_{\mathrm{res}}, S_{\mathrm{miss}}, S_{\mathrm{block}}, S_{\mathrm{regime}}) are preserved under equivalence.
Then the diagnostic functional
[
\widehat{\mathcal C}(D)=\sum_j w_j S_j,\qquad w_j>0,\qquad \sum_j w_j=1
]
is representation-invariant:
[
D \sim D' \implies \widehat{\mathcal C}(D)=\widehat{\mathcal C}(D').
]

## Weakest sufficient use

This is the canonical lock needed before any theorem using (\widehat{\mathcal C}) as an admissible comparison functional across equivalent encodings.

## Consequence

Any trigger rule defined only through (\widehat{\mathcal C}) is well-defined on equivalence classes of admissible diagnostic representations.

## Canonical formula lock

[
D \sim D' \implies \widehat{\mathcal C}(D)=\widehat{\mathcal C}(D').
]
