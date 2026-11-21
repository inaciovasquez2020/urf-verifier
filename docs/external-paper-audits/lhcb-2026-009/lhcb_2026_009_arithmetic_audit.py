#!/usr/bin/env python3
"""Independent public-number arithmetic audit; NOT an event-level LHCb reproduction."""
from decimal import Decimal as D
from decimal import getcontext
getcontext().prec = 35
Q=lambda x:D(str(x))
def check(name, truth):
    if not truth: raise AssertionError(name)
    print(name+' := PASS')

def quadrature(xs):return sum((Q(x)**2 for x in xs), D(0)).sqrt()
check('MASS_DIFFERENCE',Q('3619.97')-Q('3621.74')==Q('-1.77'))
check('MASS_SYSTEMATIC_QUADRATURE',abs(quadrature(['0.14','0.10','0.10','0.10','0.14'])-Q('.26')) < Q('.005'))
check('DELTA_SYSTEMATIC_QUADRATURE',abs(quadrature(['0.03','0.05','0.10','0.10'])-Q('.15')) < Q('.005'))
check('DELTA_STAT_INDEPENDENT_APPROX',abs(quadrature(['.83','.10'])-Q('.84')) < Q('.005'))
check('LIFETIME_LOWER_SHIFT',Q('2.0')-Q('3.3')==Q('-1.3'))
check('LIFETIME_UPPER_SHIFT',Q('2.0')-Q('.1')==Q('1.9'))
check('SELEX_DIFFERENCE_ROUNDING',round(Q('3619.97')-Q('3518.7'))==101)
check('CONTROL_YIELD_PER_LUM',abs(Q('8712')/Q('6.9')-Q('1262'))<Q('1'))
check('CONTROL_EFFICIENCY_APPROX',Q('4') < (Q('1262')/Q('285')) < Q('4.5'))
check('SIGNAL_YIELD_OVER_ERROR',Q('915')/Q('120')==Q('7.625'))
print('MASS_SYSTEMATIC_EXACT :=',quadrature(['.14','.10','.10','.10','.14']))
print('DELTA_SYSTEMATIC_EXACT :=',quadrature(['.03','.05','.10','.10']))
print('DELTA_STAT_INDEPENDENT_APPROX :=',quadrature(['.83','.10']))
print('FIT_SIGNIFICANCE := NOT_REPRODUCED_LIKELIHOOD_REQUIRED')
print('CORRECTION_CONVENTION := NEEDS_DETAILED_PROVENANCE')
print('EVENT_DATA_REPLAY := NOT_RUN')
print('RESULT := PUBLIC_ARITHMETIC_PASS_NO_CONFIRMED_DISCREPANCY')
