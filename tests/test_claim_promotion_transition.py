import unittest
import sys
from pathlib import Path
from dataclasses import FrozenInstanceError
from itertools import product
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from claim_promotion_transition import Claim, promote, verify_all_states


class ClaimPromotionTransitionTests(unittest.TestCase):
    def test_exhaustive_declared_domain(self):
        self.assertEqual(verify_all_states(), 16)
        for status, evidence, dependencies, boundary in product(
            ("conditional", "proved"), (False, True), (False, True), (False, True)
        ):
            c = Claim(status, evidence, dependencies, boundary)
            expected = "proved" if status == "proved" or (evidence and dependencies and boundary) else "conditional"
            self.assertEqual(promote(c).status, expected)
            self.assertEqual(promote(promote(c)), promote(c))

    def test_reject_invalid_status(self):
        for value in (None, "PROVED", "verified", "", 0, 1, True, False, [], ("conditional",)):
            with self.subTest(value=repr(value)):
                with self.assertRaises(ValueError):
                    Claim(value, True, True, True)

    def test_reject_invalid_gates(self):
        for status in ("conditional", "proved"):
            for field in ("evidence_ok", "dependencies_ok", "boundary_ok"):
                for value in ("yes", "", 0, 1, None, [], [True], {}, 0.0):
                    kwargs = dict(status=status, evidence_ok=True, dependencies_ok=True, boundary_ok=True)
                    kwargs[field] = value
                    with self.subTest(status=status, field=field, value=repr(value)):
                        with self.assertRaises(TypeError):
                            Claim(**kwargs)

    def test_frozen(self):
        c = Claim("conditional", True, True, True)
        with self.assertRaises(FrozenInstanceError):
            c.evidence_ok = False

    def test_no_evidence_authentication(self):
        # True is an asserted gate, not an independently certified proof.
        c = Claim("conditional", True, True, True)
        self.assertEqual(promote(c).status, "proved")


if __name__ == "__main__":
    unittest.main()
