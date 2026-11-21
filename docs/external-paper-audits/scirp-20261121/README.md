# Independent SCIRP external-paper audit fixtures — 2026-11-21

STATUS: LOCAL_CERTIFICATE_REPLAY := COMPUTATION_PASS (55 / 55 assertions)
MAC_REPLAY := USER_REPORTED_PASS (19 / 19, 9 / 9, 27 / 27)
URF_AI_INTEGRATION := NOT_RUN
AUTHOR_INQUIRY_154830 := SENT_USER_CONFIRMED (response pending)
REPOSITORY_PROMOTION := NOT_PERFORMED

All three scripts are standard-library Python and have been kept byte-for-byte identical to the earlier certificates. `replay_python3.txt` files were generated independently in this execution environment; they are NOT the user's original Mac logs. No source version archive, full study workbook, scanner experiment or LANL replay is bundled.

## Included audits

- `155473`: [SCIRP original](https://www.scirp.org/journal/paperinformation?paperid=155473). Synthetic overlapping-session attribution cannot be identified from host/time alone (conditional on that observation model). Logistic zero-score example shows calibration is not guaranteed. No empirical failure rate established.
- `144194`: [SCIRP original](https://www.scirp.org/journal/paperinformation?paperid=144194). Reference chronology needs historical version verification. Dead-time calculations concern an idealized nonparalyzable model, not an observed defect in an actual CT scanner.
- `154830`: [SCIRP original](https://www.scirp.org/journal/paperinformation?paperid=154830). Theorem 5.1 calls gravity the number of captured *nonfixed* seeds, while its fiber is the entire basin including the terminal fixed point. Under fiber-cardinality multiplicity, the finite-range correction is |fiber intersect S| = G_S(p)+1_{p in S}. Because Proposition 5.0 says T(n)>=n, unrestricted basins of fixed points p lie in [2,p], so multiplicity=gravity+1. Example p=3 has fiber 1 and gravity 0. 'Multiplicity' is not independently defined in the paper, so the author may clarify a different convention. The published cubic and the twin-prime conjecture are not refuted.

## Run

From this folder: `python3 -B 154830/scirp_154830_audit.py` (and analogous scripts). Hashes of the exact scripts are in `SHA256SUMS.txt`.

## Verification boundaries

- Synthetic/model tests and exact arithmetic are not a full formal proof of each paper.
- The mathematical counting identity for 154830 follows directly from the source's definitions under the stated interpretation.
- No Lean formalization or autonomous URF-AI discrepancy discovery has been performed.
- Any author correspondence and its response should be retained privately unless separately approved for publication.
