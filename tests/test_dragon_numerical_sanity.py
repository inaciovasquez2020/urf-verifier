from itertools import combinations

WEIGHTS = {"res": 0.25, "miss": 0.25, "block": 0.25, "regime": 0.25}

def score(d):
    return sum(WEIGHTS[k] * d[k] for k in WEIGHTS)

def apply_augmentation(base, effects):
    return {k: max(0.0, base[k] - effects.get(k, 0.0)) for k in base}

def dragon_k(base, tau, augmentations, k):
    base_score = score(base)
    best_score = base_score
    best_choice = ()
    for r in range(k + 1):
        for combo in combinations(augmentations, r):
            total = {key: 0.0 for key in WEIGHTS}
            names = []
            for name, eff in combo:
                names.append(name)
                for key in WEIGHTS:
                    total[key] += eff.get(key, 0.0)
            state = apply_augmentation(base, total)
            s = score(state)
            if s < best_score:
                best_score = s
                best_choice = tuple(names)
    gain = base_score - best_score
    return {
        "base_score": base_score,
        "best_score": best_score,
        "gain": gain,
        "fires": gain >= tau - 1e-12,
        "choice": best_choice,
    }

def test_irreducible_one_wall():
    base = {"res": 2.0, "miss": 1.6, "block": 1.8, "regime": 1.4}
    tau = 1.2
    augmentations = [
        ("Z_common", {"res": 1.4, "miss": 1.1, "block": 1.3, "regime": 1.0}),
        ("Z_partial_A", {"res": 0.8, "miss": 0.2, "block": 0.3, "regime": 0.0}),
        ("Z_partial_B", {"res": 0.2, "miss": 0.7, "block": 0.4, "regime": 0.3}),
    ]
    r1 = dragon_k(base, tau, augmentations, 1)
    r2 = dragon_k(base, tau, augmentations, 2)
    assert abs(r1["base_score"] - 1.7) < 1e-12
    assert abs(r1["best_score"] - 0.5) < 1e-12
    assert abs(r1["gain"] - 1.2) < 1e-12
    assert r1["fires"] is True
    assert r1["choice"] == ("Z_common",)
    assert r2["fires"] is True
    assert r2["best_score"] < r1["best_score"]

def test_independent_two_walls():
    base = {"res": 1.0, "miss": 1.0, "block": 1.0, "regime": 1.0}
    tau = 0.75
    augmentations = [
        ("Z_A", {"res": 1.0, "miss": 1.0, "block": 0.0, "regime": 0.0}),
        ("Z_B", {"res": 0.0, "miss": 0.0, "block": 1.0, "regime": 1.0}),
        ("Z_weak", {"res": 0.3, "miss": 0.1, "block": 0.2, "regime": 0.1}),
    ]
    r1 = dragon_k(base, tau, augmentations, 1)
    r2 = dragon_k(base, tau, augmentations, 2)
    assert abs(r1["base_score"] - 1.0) < 1e-12
    assert abs(r1["best_score"] - 0.5) < 1e-12
    assert abs(r1["gain"] - 0.5) < 1e-12
    assert r1["fires"] is False
    assert r2["fires"] is True
    assert r2["choice"] == ("Z_A", "Z_B")
    assert abs(r2["best_score"] - 0.0) < 1e-12
