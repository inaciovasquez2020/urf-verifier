from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from network_capability_invariant import (
    authorize_external_network_action,
    external_network_capability_invariant,
)


def test_external_network_capability_truth_table() -> None:
    cases = [
        (True, False, False),
        (True, None, False),
        (True, True, True),
        (False, False, True),
        (False, None, True),
        (False, True, True),
    ]

    for requests_external_network, capability, expected_authorized in cases:
        decision = authorize_external_network_action(
            requests_external_network=requests_external_network,
            externally_issued_capability=capability,
        )
        assert decision.authorized is expected_authorized
        assert external_network_capability_invariant(decision) is True
