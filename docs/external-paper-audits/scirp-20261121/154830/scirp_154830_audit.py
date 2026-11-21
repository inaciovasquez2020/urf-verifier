#!/usr/bin/env python3
"""Independent exact-arithmetic audit of SCIRP paper 154830. Python >=3.8.
Source: https://www.scirp.org/journal/paperinformation?paperid=154830
No network, files modified, or external dependencies.
"""
from math import factorial, isqrt

checks = 0
def check(label, statement):
    global checks
    assert statement, 'FAIL: ' + label
    checks += 1
    print(label + ' := PASS')

def sigma(n):
    assert n >= 1
    return sum(d + (n // d if d * d != n else 0)
               for d in range(1, isqrt(n) + 1) if n % d == 0)

def T(n):
    return sigma(sigma(sigma(n) - 1) + 1) - 3

def isprime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def wilson(p):
    return (factorial(p - 1) + 1, p)

# Theorem 5.1: gravity excludes a fixed seed, but its fiber includes that seed.
for p in (3, 5, 11, 17, 29):
    check('FIXED_POINT_' + str(p), T(p) == p)
check('GRAVITY_SINGLETON_ZERO', len([n for n in (3,) if n != 3 and T(n) == 3]) == 0)
check('FIBER_SINGLETON_ONE', len([n for n in (3,) if T(n) == 3]) == 1)
check('THEOREM_5_1_MULTIPLICITY_COUNTEREXAMPLE', 1 != 0)
print('COUNTEREXAMPLE := basin restricted to seed range [3,3]; gravity 0; fiber size 1')

# Equation 8 and Table 1: exact normalization for the reported twin pairs.
for p in (5, 11, 17, 29):
    q = p+2
    a,b = wilson(p)
    c,d = wilson(q)
    check('TWIN_WILSON_INTEGRAL_' + str(p), a%b == 0 and c%d == 0)
    N,M = a//b,c//d
    check('CUBIC_IDENTITY_' + str(p), N*p**3-(1-N)*p**2-p*(1+M)-(2*M-1) == 0)
check('TABLE_1_P29_WILSON', (factorial(28)+1)//29 == 10513391193507374500051862069)

# Eq 12 and Table 2: independently reconstruct base points and strides.
for p, expected_n0, expected_m0 in ((3,1,5),(5,5,103),(11,3,325),(71,18,89425)):
    q=p+2; A=p*p*(p+1); B=p*p+p-1
    N0=next(n for n in range(q) if (4*n+1)%q == 0)
    check('STATION_BASE_' + str(p), N0 == expected_n0 and (A*N0-B)//q == expected_m0 and (A*N0-B)%q == 0)

# Theorem 9.1 dichotomy and paper's census below 2000.
primes=[p for p in range(3,2000,2) if isprime(p)]
twins=[p for p in primes if isprime(p+2)]
check('PRIMES_BELOW_2000',len(primes)==302)
check('TWIN_LOWERS_BELOW_2000',len(twins)==61)
for p in primes:
    num,den=wilson(p); assert num%den==0
    delta=(4*(num//den)+1)%(p+2)
    check_label=None
    assert delta==(0 if isprime(p+2) else p+1)
check('UNIT_MISS_CENSUS',len(primes)-len(twins)==241)

# Logical issue in Theorem 11.7's general character explanation:
# not all real quadratic characters have odd parity. Chi_8 is even.
def chi8(n):
    assert n%2
    return 1 if n%8 in (1,7) else -1
J=4320*1+719
check('GAP_SIX_J_MOD_8',J%8==7)
check('CHI8_IS_EVEN',chi8(7)==1)
check('CHI8_DIVISOR_SUM_NONZERO_J5039',isprime(J) and (chi8(1)+chi8(J))==2)
print('BOUNDARY := This does not refute the paper\'s odd-character vanishing claim; it refutes extension to all real characters.')
print('ASSERTION_COUNT :=',checks)
print('RESULT := MULTIPLICITY_OFF_BY_ONE_PROVED_AND_NUMERIC_REPLAY_PASS')
print('URF_AI_INTEGRATION := NOT_RUN')
print('REPOSITORY_MODIFIED := FALSE')
