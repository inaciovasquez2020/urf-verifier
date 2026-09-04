from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ExternalNetworkDecision:
    requests_external_network: bool
    externally_issued_capability: Optional[bool]
    authorized: bool


def authorize_external_network_action(
    *,
    requests_external_network: bool,
    externally_issued_capability: Optional[bool],
) -> ExternalNetworkDecision:
    """Fail closed: external network use is authorized only by explicit external capability."""
    authorized = (not requests_external_network) or (externally_issued_capability is True)
    return ExternalNetworkDecision(
        requests_external_network=requests_external_network,
        externally_issued_capability=externally_issued_capability,
        authorized=authorized,
    )


def external_network_capability_invariant(decision: ExternalNetworkDecision) -> bool:
    """Any authorized external-network action must carry an externally issued capability."""
    return (
        not decision.authorized
        or not decision.requests_external_network
        or decision.externally_issued_capability is True
    )
