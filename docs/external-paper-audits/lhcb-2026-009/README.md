# LHCb-PAPER-2026-009: independent public-number consistency audit

Source: https://cds.cern.ch/record/2959557/files/LHCb-PAPER-2026-009.pdf
Date of package: 2026-11-21

## Verification

- `lhcb_2026_009_arithmetic_audit.py`: ten assertions on publicly quoted rounded quantities, including mass subtraction, quadrature, and simple yield ratios.
- `lhcb_mass_ordering_robustness.py`: seven assertions on a **conditional** nuisance-shift interval and independent-quadrature approximation.
- `arithmetic_replay.txt` and `robustness_replay.txt` are runs in the packaging execution environment; they are **not** captured from the user's Mac.
- The user reported successful Mac runs on 2026-11-21 for both scripts (10 and 7 assertions respectively). This is a user-supplied receipt, not an independently obtained Mac log.
- Reproduce with `python3 -B lhcb_2026_009_arithmetic_audit.py` and `python3 -B lhcb_mass_ordering_robustness.py`.

## Conditional calculation and inference boundary

The published central mass difference is -1.77 MeV/c^2, with statistical 0.84, systematic 0.15 and asymmetric lifetime-dependent terms -1.30/+1.90 MeV/c^2. **Assuming** these lifetime terms can be interpreted as shifts applied to that central difference at the same baseline, the nuisance-shifted central range is [-3.07, +0.13] MeV/c^2. This is *not* a measured confidence interval, nor a joint likelihood/profile fit. Assuming independent statistical and systematic terms gives sqrt(0.84^2+0.15^2) ~= 0.8533 MeV/c^2, with nominal |central|/sigma ~= 2.074. This is not the >7 sigma baryon observation significance.

Outcome: PUBLIC_ARITHMETIC := COMPUTATION_PASS; UNCONDITIONAL_MASS_ORDERING := NOT_ESTABLISHED_BY_THESE_NUMBERS; PAPER_ERROR := NONE_CONFIRMED; EVENT_LEVEL_LIKELIHOOD := NOT_RUN.

## Project transfer assessment

- URF-AI: **benchmark candidate** for false-discrepancy rejection, asymmetric nuisance-parameter caution and evidence-scope discipline. No blind autonomous discovery or model run performed. Its public oracle scripts are not appropriate as a hidden answer key.
- Chronos-URF-RR: methodological analogy (event -> selection -> likelihood -> parameter), no derived transfer theorem or empirical link.
- DFM-MKC cosmology: no constraint on a 5D model without an explicit prediction for the baryon observable and a justified comparison likelihood. Does not establish fifth-dimensional physics, NEC satisfaction or five-dimensional stability.
- Poincare: no direct application identified.

No event data, likelihood, detector-specific model, external physics code or paper-author communication is bundled. This package is not a theorem proof of particle physics or a substitute for collaboration data.

## Provenance

`SHA256SUMS.txt` lists exact package contents excluding itself. `arithmetic_replay.txt` and `robustness_replay.txt` reflect the scripts executed by the packaging agent. The scripts are deliberately unchanged from the prior user-tested files; hashes may be compared against the user's downloads.
