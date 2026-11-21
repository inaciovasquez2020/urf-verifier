#!/usr/bin/env python3
"""LHCb-PAPER-2026-009: bounded interval/uncertainty claim audit.

No event-level likelihood reconstruction; model assumes published lifetime shifts
are applicable to the quoted mass difference. Standard deviation combination
assumes independence of quoted stat and syst uncertainties.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
getcontext().prec = 45
D = Decimal
central = D('-1.77')
stat = D('0.84')
syst = D('0.15')
lower_lifetime = D('-1.30')
upper_lifetime = D('1.90')
sigma = (stat * stat + syst * syst).sqrt()
z = abs(central)/sigma
low = central + lower_lifetime
high = central + upper_lifetime
assert sigma > 0
assert D('0.85') < sigma < D('0.86')
assert D('2.07') < z < D('2.08')
assert low == D('-3.07')
assert high == D('0.13')
assert low < 0 < high, 'Lifetime nuisance does not straddle zero'
assert central < 0
assert z < D('3')
print('SOURCE := LHCb-PAPER-2026-009 (published mass-difference summary)')
print('CENTRAL_MASS_DIFFERENCE_MEV :=', central)
print('ASSUMED_INDEPENDENT_STAT_SYST_SIGMA_MEV :=', sigma)
print('CENTRAL_SIGNIFICANCE_Z_APPROX :=', z)
print('LIFETIME_SHIFTED_CENTRAL_RANGE_MEV :=', low, high)
print('LIFETIME_ROBUST_NEGATIVE_ORDERING := NOT_ESTABLISHED')
print('CONDITIONAL_INTERVAL_COUNTEREXAMPLE := PASS')
print('EVENT_LIKELIHOOD := NOT_REPRODUCED')
print('ACTUAL_MODEL_FIT := NOT_RUN')
print('THEORY_CONSTRAINT_ON_5D := NOT_ESTABLISHED')
print('ASSERTION_COUNT := 7')
