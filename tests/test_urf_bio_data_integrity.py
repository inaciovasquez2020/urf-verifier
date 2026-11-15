from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from urf_bio_data_integrity import audit_aggregate, audit_cells, exact_test


def test_exclusion():
    result = audit_cells({"candidate_cell_ids": ["a", "b", "c"], "known_malignant_cell_ids": ["a", "z"]})
    assert result["overlap_count"] == 1
    assert result["retained_count"] == 2
    assert result["disjoint_from_known_malignant"]
    assert not result["macrophage_identity_verified"]


@pytest.mark.parametrize("data", [
    {"candidate_cell_ids": ["a", "a"], "known_malignant_cell_ids": []},
    {"candidate_cell_ids": ["a"], "known_malignant_cell_ids": ["z", "z"]},
    {"candidate_cell_ids": [1], "known_malignant_cell_ids": []},
    {"candidate_cell_ids": [""], "known_malignant_cell_ids": []},
])
def test_bad_cells_rejected(data):
    with pytest.raises(ValueError):
        audit_cells(data)


def test_exact_enumeration():
    rows = [{"patient_id": str(i), "response": "R" if i == 0 else "PD", "value": str(i)} for i in range(4)]
    result = exact_test(rows)
    assert (result["total_permutations"], result["extreme_permutations"]) == (4, 2)
    assert math.isclose(result["exact_two_sided_p"], 0.5)


def test_duplicate_patient_rejected():
    with pytest.raises(ValueError):
        exact_test([{"patient_id": "x", "response": "R", "value": "1"},
                    {"patient_id": "x", "response": "PD", "value": "0"}])


def test_invalid_direction_rejected():
    with pytest.raises(ValueError):
        exact_test([{"patient_id": "x", "response": "R", "value": "1"},
                    {"patient_id": "y", "response": "PD", "value": "0"}], direction="oops")


def test_inconsistent_aggregate_rejected():
    record = {"matched_baseline_patients": 12, "responders": 4, "nonresponders": 8,
              "results": {"stat": {"extreme_permutations": 288, "total_permutations": 495,
                                   "exact_two_sided_p": 0.1}}}
    assert audit_aggregate(record)


def test_consistent_aggregate_passes():
    record = {"matched_baseline_patients": 12, "responders": 4, "nonresponders": 8,
              "results": {"stat": {"extreme_permutations": 288, "total_permutations": 495,
                                   "exact_two_sided_p": 288 / 495}}}
    assert not audit_aggregate(record)


def test_empty_results_rejected():
    record = {"matched_baseline_patients": 12, "responders": 4, "nonresponders": 8,
              "results": {"metadata": "not a statistic"}}
    assert audit_aggregate(record)


def test_resource_guard():
    rows = [{"patient_id": str(i), "response": "R" if i < 12 else "PD", "value": "0"}
            for i in range(24)]
    with pytest.raises(ValueError, match="resource guard"):
        exact_test(rows)
