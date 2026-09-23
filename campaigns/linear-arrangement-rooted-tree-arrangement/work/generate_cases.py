"""Regenerate the fixed preparation corpus; no candidate construction is used."""

import itertools
import json
import random
from pathlib import Path


def optimum(n, edges):
    best = None
    for order in itertools.permutations(range(n)):
        positions = {v: i for i, v in enumerate(order)}
        cost = sum(abs(positions[u] - positions[v]) for u, v in edges)
        if best is None or cost < best:
            best = cost
    return best


def main():
    cases = []
    seen = set()

    def add(n, edges, k, kind, seed=None):
        source = {"n": n, "vertices": list(range(n)), "edges": [list(e) for e in edges], "k": k}
        key = json.dumps(source, sort_keys=True)
        if key in seen:
            return False
        seen.add(key)
        case = {"source": source, "kind": kind, "optimum": optimum(n, edges)}
        if seed is not None:
            case["seed"] = seed
        cases.append(case)
        return True

    # Hand-verifiable boundary inputs, including the empty graph and negative bounds.
    for n, edges, k in [
        (0, [], -1), (0, [], 0), (1, [], -1), (1, [], 0),
        (2, [], -1), (2, [], 0), (2, [(0, 1)], 0), (2, [(0, 1)], 1),
        (3, [(0, 1), (1, 2)], 1), (3, [(0, 1), (1, 2)], 2),
        (3, [(0, 1), (0, 2), (1, 2)], 3),
        (3, [(0, 1), (0, 2), (1, 2)], 4),
        (4, [(0, 1), (0, 2), (0, 3)], 3),
        (4, [(0, 1), (0, 2), (0, 3)], 4),
    ]:
        assert add(n, edges, k, "edge")

    for seed in range(400):
        rng = random.Random(seed)
        n = rng.choice((3, 4, 5))
        density = rng.choice((0.2, 0.45, 0.7, 0.95))
        edges = [e for e in itertools.combinations(range(n), 2) if rng.random() < density]
        value = optimum(n, edges)
        k = value + rng.choice((-2, -1, 0, 0, 1, 2))
        add(n, edges, k, "random", seed)
        if sum(case["kind"] == "random" for case in cases) == 100:
            break
    assert len(cases) == 114
    Path(__file__).with_name("cases.json").write_text(json.dumps(cases, indent=2) + "\n")


if __name__ == "__main__":
    main()
