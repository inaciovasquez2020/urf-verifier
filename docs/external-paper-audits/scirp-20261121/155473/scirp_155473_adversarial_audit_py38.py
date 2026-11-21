#!/usr/bin/env python3
"""Bounded, stdlib-only adversarial audit of SCIRP paper 155473, §7.2 and §8.
No dataset download; synthetic counterexamples, not empirical performance claims.
"""
from dataclasses import dataclass
from typing import Optional
from itertools import product
from fractions import Fraction
from math import exp

@dataclass(frozen=True)
class Session:
    sid: str
    user: str
    host: str
    start: int
    end: int

@dataclass(frozen=True)
class Event:
    eid: str
    host: str
    time: int
    user: Optional[str] = None
    sid: Optional[str] = None

def candidates(event, sessions):
    return tuple(s.sid for s in sessions
                 if s.host == event.host and s.start <= event.time < s.end
                 and (event.user is None or event.user == s.user)
                 and (event.sid is None or event.sid == s.sid))

def require(cond, label):
    if not cond:
        raise AssertionError(label)
    print(f'{label} := PASS')

# Publication's printed aggregate claims; these confirm arithmetic only.
require(sum((27,56,153,153,72,23)) == 484, 'QUERY_YIELD_ARITHMETIC')
require(sum((2,17,35,49,29,5)) == 137, 'QUERY_INCLUDED_APPEARANCES')
require(sum((88,27,6,12,2)) == 135, 'DEPLOYMENT_CONTEXT_ARITHMETIC')
require(sum((71,56,1,7)) == 135, 'IDENTITY_TYPE_ARITHMETIC')
require(sum((35,28,26,22,18,6)) == 135, 'THREAT_TYPE_ARITHMETIC')
require(sum((30,29,26,19,9,3,3,16)) == 135, 'METHOD_TYPE_ARITHMETIC')
require(sum((38,25,22,17,12,1,15,5)) == 135, 'DATASET_TYPE_ARITHMETIC')
require(3+10+24 == 37, 'APPRAISAL_BAND_ARITHMETIC')

# Two sessions of different users on a shared machine overlap for 10 units.
sessions = (Session('s_A','alice','h_shared',0,20),
            Session('s_B','bob','h_shared',10,30))
events = (Event('proc','h_shared',15), Event('flow','h_shared',16))
C = tuple(candidates(e,sessions) for e in events)
possible_worlds = tuple(product(*C))
require(all(len(c)==2 for c in C), 'SHARED_HOST_JOIN_AMBIGUOUS')
require(len(possible_worlds)==4, 'EXHAUSTIVE_TWO_EVENT_ASSIGNMENTS')
require(len(set(possible_worlds))==4, 'DISTINCT_INDISCERNIBLE_WORLDS')
# All candidate worlds emit exactly the same observable records.
observed = tuple((e.eid,e.host,e.time,e.user,e.sid) for e in events)
require(len({observed for _ in possible_worlds}) == 1,
        'OBSERVATIONAL_EQUIVALENCE')
# User attribution uniquely disambiguates this constructed case.
identified = Event('proc','h_shared',15,user='alice')
require(candidates(identified,sessions)==('s_A',), 'USER_IDENTIFIER_REPAIRS_CASE')
# Session identifiers work even if two sessions belong to one user.
identified_sid = Event('proc','h_shared',15,sid='s_B')
require(candidates(identified_sid,sessions)==('s_B',), 'SESSION_ID_REPAIRS_CASE')
# Boundary of exclusivity: no overlap -> unique host-time candidate.
require(candidates(Event('proc','h_shared',5),sessions)==('s_A',),
        'NONOVERLAP_UNIQUE_CASE')

# Verify all 2^4 true assignments to four identical-field host-only events.
events4 = tuple(Event(f'e{k}','h_shared',15+k) for k in range(4))
worlds4 = tuple(product(*(candidates(e,sessions) for e in events4)))
require(len(worlds4)==16, 'FOUR_EVENT_WORLD_ENUMERATION')
require(all(len(candidates(e,sessions))==2 for e in events4),
        'FOUR_EVENT_AMBIGUITY')

# Separately, the illustrative logistic specialization of equation (1)
# does not guarantee calibration from the score formula alone.
sigmoid = lambda z: 1/(1+exp(-z))
require(sigmoid(0)==0.5, 'ZERO_SCORE_LOGISTIC_HALF')
prevalence=Fraction(1,10000)
brier_model = Fraction(1,4)  # constant 0.5: mean squared error 1/4
brier_prior = prevalence*(1-prevalence)
require(brier_model > brier_prior, 'UNCALIBRATED_BASE_RATE_COUNTEREXAMPLE')
print('TRUE_PREVALENCE :=', str(prevalence))
print('BASERATE_CONSTANT_BRIER :=', str(brier_prior))
print('LOGISTIC_ZERO_CONSTANT_BRIER :=', str(brier_model))
print('RESULT := SYNTHETIC_NONIDENTIFIABILITY_PROVED_WITHIN_MODEL')
print('FULL_LANL_REPLAY := NOT_RUN')
print('ZENODO_WORKBOOK_AUDIT := NOT_RUN')
print('URF_AI_INTEGRATION := NOT_RUN')
