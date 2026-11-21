#!/usr/bin/env python3
"""SCIRP 144194: offline chronology and idealized detector-model audit.

The publication dates are fixtures independently sourced from the SCIRP PDF
and PubMed. The detector example is a NONPARALYZABLE DEAD-TIME MODEL,
not a measurement of the studied scanners.
"""
from datetime import date
from fractions import Fraction

scirp_received = date(2025, 2, 3)
scirp_accepted = date(2025, 3, 28)
scirp_published = date(2025, 3, 31)
shah_accepted = date(2025, 5, 6)
shah_journal_published = date(2025, 5, 16)
checks = []
def check(name, proposition):
    assert proposition, name
    checks.append(name)
    print(name + ' := PASS')

check('SCIRP_INTERNAL_DATE_ORDER', scirp_received < scirp_accepted < scirp_published)
check('REF36_ACCEPTANCE_AFTER_SCIRP_PUBLICATION', scirp_published < shah_accepted)
check('REF36_JOURNAL_PUBLICATION_AFTER_SCIRP_PUBLICATION', scirp_published < shah_journal_published)
print('REF36_ACCEPTANCE_LAG_DAYS :=', (shah_accepted - scirp_published).days)
print('REF36_PUBLICATION_LAG_DAYS :=', (shah_journal_published - scirp_published).days)

# Nonparalyzable detector: observed event rate mu=lambda/(1+lambda*tau).
# Use the dimensionless arrival intensity x=lambda*tau.
def detected_fraction(x):
    return Fraction(1, 1) / (1+x)
for x in [Fraction(0), Fraction(1,10), Fraction(1), Fraction(4)]:
    frac = detected_fraction(x)
    check('DEADTIME_FRACTION_X_' + str(x).replace('/', '_'), 0 < frac <= 1)
    print('X',x,'DETECTED_FRACTION',frac,'LOSS_FRACTION',1-frac)
check('DEADTIME_HALF_LOSS_AT_UNIT_OCCUPANCY', detected_fraction(Fraction(1)) == Fraction(1,2))
check('DEADTIME_HIGHER_FLUX_LOWER_FRACTION', detected_fraction(Fraction(4)) < detected_fraction(Fraction(1,10)))
print('RESULT := CHRONOLOGY_ANOMALY_PLUS_CONDITIONAL_DEADTIME_COUNTEREXAMPLE')
print('SOURCE_VERSION_HISTORY := OPEN')
print('EMPIRICAL_SCANNER_VALIDATION := NOT_RUN')
print('URF_AI_INTEGRATION := NOT_RUN')
print('ASSERTION_COUNT :=', len(checks))
