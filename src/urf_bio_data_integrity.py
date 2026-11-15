#!/usr/bin/env python3
"""Bounded biological set-integrity and patient-level randomization audits."""
import argparse
import csv
import itertools
import json
import math
from pathlib import Path


def audit_aggregate(a):
    errors = []
    n, r, nr = a.get("matched_baseline_patients"), a.get("responders"), a.get("nonresponders")
    if any(type(x) is not int for x in (n, r, nr)) or n < 2 or not 0 < r < n or nr != n - r:
        return ["invalid patient counts"]
    total = math.comb(n, r)
    found = False

    def walk(v, path=""):
        nonlocal found
        if isinstance(v, dict):
            keys = ("extreme_permutations", "total_permutations", "exact_two_sided_p")
            if any(k in v for k in keys):
                found = True
                k, t, p = (v.get(key) for key in keys)
                if (type(k) is not int or not 0 <= k <= total or type(t) is not int
                        or t != total or type(p) not in (float, int)
                        or not math.isfinite(p) or not math.isclose(p, k / total, rel_tol=0, abs_tol=1e-12)):
                    errors.append("inconsistent permutation statistic: " + path)
            for key, sub in v.items():
                walk(sub, path + "." + key)
        elif isinstance(v, list):
            for i, sub in enumerate(v):
                walk(sub, f"{path}[{i}]")

    walk(a.get("results", {}), "results")
    if not found:
        errors.append("missing results")
    return errors


def exact_test(rows, direction="nonresponder_minus_responder"):
    """Enumerate all patient-label allocations; float arithmetic, conservative near-tie policy."""
    if direction not in ("nonresponder_minus_responder", "responder_minus_nonresponder"):
        raise ValueError("invalid statistic direction")
    ids = [row["patient_id"] for row in rows]
    if any(not isinstance(x, str) or not x.strip() for x in ids) or len(ids) != len(set(ids)):
        raise ValueError("invalid or duplicate patient identifiers")
    if len(ids) < 2:
        raise ValueError("need at least two patients")
    labels = [row["response"] for row in rows]
    if set(labels) != {"R", "PD"}:
        raise ValueError("response labels must include R and PD")
    vals = [float(row["value"]) for row in rows]
    if not all(math.isfinite(x) for x in vals):
        raise ValueError("nonfinite measurement")
    n = len(vals)
    responders = labels.count("R")
    total = math.comb(n, responders)
    if total > 2_000_000:
        raise ValueError("resource guard: more than 2 million assignments")
    selected = frozenset(i for i, label in enumerate(labels) if label == "R")

    def statistic(group):
        response = sum(vals[i] for i in group) / responders
        nonresponse = sum(vals[i] for i in range(n) if i not in group) / (n - responders)
        return nonresponse - response if direction == "nonresponder_minus_responder" else response - nonresponse

    observed = statistic(selected)
    tolerance = 1e-12 * max(1.0, max(abs(x) for x in vals))
    extremes = sum(abs(statistic(frozenset(combo))) + tolerance >= abs(observed)
                   for combo in itertools.combinations(range(n), responders))
    return {"n": n, "responders": responders, "observed_difference": observed,
            "extreme_permutations": extremes, "total_permutations": total,
            "exact_two_sided_p": extremes / total,
            "arithmetic": "float64 with 1e-12 scaled conservative tie tolerance"}


def audit_cells(data):
    candidates, malignant = data["candidate_cell_ids"], data["known_malignant_cell_ids"]
    if (not isinstance(candidates, list) or not isinstance(malignant, list)
            or any(type(x) is not str or not x.strip() for x in candidates + malignant)):
        raise ValueError("cell IDs must be nonempty string lists")
    if len(candidates) != len(set(candidates)) or len(malignant) != len(set(malignant)):
        raise ValueError("duplicate cell IDs")
    c, m = set(candidates), set(malignant)
    clean = c - m
    return {"candidate_count": len(c), "known_malignant_count": len(m),
            "overlap_count": len(c & m), "retained_count": len(clean),
            "disjoint_from_known_malignant": not bool(clean & m),
            "macrophage_identity_verified": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--aggregate", type=Path)
    parser.add_argument("--patients", type=Path, help="CSV: patient_id,response,value; response R or PD")
    parser.add_argument("--cells", type=Path, help="JSON: candidate_cell_ids, known_malignant_cell_ids")
    args = parser.parse_args()
    if not any((args.aggregate, args.patients, args.cells)):
        parser.error("supply a mode")
    output, failed = {}, False
    try:
        if args.aggregate:
            errors = audit_aggregate(json.loads(args.aggregate.read_text(encoding="utf-8")))
            output["aggregate"] = {"status": "FAIL" if errors else "ARITHMETIC_PASS_ONLY",
                                   "errors": errors, "recomputed_from_patient_data": False}
            failed |= bool(errors)
        if args.patients:
            with args.patients.open(newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                if reader.fieldnames != ["patient_id", "response", "value"]:
                    raise ValueError("expected exact CSV header patient_id,response,value")
                rows = list(reader)
            if not rows or any(set(row) != {"patient_id", "response", "value"} for row in rows):
                raise ValueError("invalid patient rows")
            output["patients"] = {"status": "COMPUTATION_PASS", "result": exact_test(rows)}
        if args.cells:
            output["cells"] = {"status": "COMPUTATION_PASS",
                               "result": audit_cells(json.loads(args.cells.read_text(encoding="utf-8")))}
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
        output["error"] = str(error)
        failed = True
    print(json.dumps(output, indent=2, sort_keys=True))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
