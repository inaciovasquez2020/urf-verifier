#!/usr/bin/env python3
"""Finite, exhaustively checked URF claim-promotion transition.

Scope: exactly 16 states (two statuses x three Boolean gates).
The three gates summarize evidence, dependency, and publication-boundary checks.
Their correctness and the truth of mathematical claims are OUTSIDE this model.
"""
from dataclasses import dataclass, replace
from itertools import product
from typing import Literal

Status = Literal["conditional", "proved"]


@dataclass(frozen=True)
class Claim:
    status: Status
    evidence_ok: bool
    dependencies_ok: bool
    boundary_ok: bool


def promote(c: Claim) -> Claim:
    """A single transition, preserving the three input gates."""
    if (c.status == "conditional" and c.evidence_ok
            and c.dependencies_ok and c.boundary_ok):
        return replace(c, status="proved")
    return c


def verify_all_states() -> int:
    states = list(product(("conditional", "proved"), (False, True),
                          (False, True), (False, True)))
    for status, evidence, dependencies, boundary in states:
        before = Claim(status, evidence, dependencies, boundary)
        after = promote(before)
        if before.status == "conditional" and after.status == "proved":
            assert before.evidence_ok and before.dependencies_ok and before.boundary_ok
        if not (evidence and dependencies and boundary):
            assert after == before
        assert after.evidence_ok == evidence
        assert after.dependencies_ok == dependencies
        assert after.boundary_ok == boundary
        assert not (before.status == "proved" and after.status == "conditional")
        assert promote(after) == after
    assert len(states) == 16
    return len(states)


if __name__ == "__main__":
    print(f"FINITE_CLAIM_PROMOTION_GATE := PASS ({verify_all_states()}/16 states)")
    print("BOUNDARY := gate booleans are inputs, not independently certified evidence")
