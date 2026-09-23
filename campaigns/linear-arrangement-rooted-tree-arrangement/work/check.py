"""Independent Z3 oracles and end-to-end checker for the fixed search problems."""

import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path

import z3

ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parent


def source_cost(order, edges):
    position = {v: i for i, v in enumerate(order)}
    return sum(abs(position[u] - position[v]) for u, v in edges)


def source_optimum(source):
    n, edges = source["n"], source["edges"]
    if n == 0:
        return 0, []
    positions = [z3.Int(f"position_{i}") for i in range(n)]
    opt = z3.Optimize()
    opt.add(z3.Distinct(positions), *(z3.And(p >= 0, p < n) for p in positions))
    cost = z3.Sum([z3.Abs(positions[u] - positions[v]) for u, v in edges] + [z3.IntVal(0)])
    opt.minimize(cost)
    assert opt.check() == z3.sat
    model = opt.model()
    order = sorted(range(n), key=lambda v: model.eval(positions[v]).as_long())
    return source_cost(order, edges), order


def valid_source(source, answer, optimum=None):
    if answer == "NO-SOLUTION":
        if optimum is None:
            optimum, _ = source_optimum(source)
        return optimum > source["k"]
    if not isinstance(answer, dict) or set(answer) != {"order"}:
        return False
    order = answer["order"]
    return (isinstance(order, list) and all(type(v) is int for v in order)
            and sorted(order) == list(range(source["n"]))
            and source_cost(order, source["edges"]) <= source["k"])


def target_cost(target, answer):
    n, edges = target["n"], target["edges"]
    if not isinstance(answer, dict) or set(answer) != {"parent"}:
        return None
    parent = answer["parent"]
    if (not isinstance(parent, list) or len(parent) != n
            or any(type(p) is not int or p < -1 or p >= n for p in parent)
            or parent.count(-1) != 1):
        return None
    paths = []
    for vertex in range(n):
        path, current = [], vertex
        while current != -1:
            if current in path:
                return None
            path.append(current)
            current = parent[current]
        paths.append(path)
    root = parent.index(-1)
    if any(path[-1] != root for path in paths):
        return None
    cost = 0
    for u, v in edges:
        if u not in paths[v] and v not in paths[u]:
            return None
        cost += abs(len(paths[u]) - len(paths[v]))
    return cost


def target_solver(target):
    n = target["n"]
    parent = [z3.Int(f"parent_{i}") for i in range(n)]
    depth = [z3.Int(f"depth_{i}") for i in range(n)]
    ancestor = [[z3.Bool(f"ancestor_{i}_{j}") for j in range(n)] for i in range(n)]
    solver = z3.Solver()
    for j in range(n):
        solver.add(parent[j] >= -1, parent[j] < n, parent[j] != j)
        solver.add(depth[j] >= 0, depth[j] < n)
        solver.add(z3.Implies(parent[j] == -1, depth[j] == 0))
        for k in range(n):
            if k != j:
                solver.add(z3.Implies(parent[j] == k, depth[j] == depth[k] + 1))
        for i in range(n):
            solver.add(ancestor[i][j] == z3.Or(i == j, *(
                z3.And(parent[j] == k, ancestor[i][k]) for k in range(n) if k != j)))
    solver.add(z3.Sum([z3.If(p == -1, 1, 0) for p in parent]) == 1)
    for u, v in target["edges"]:
        solver.add(z3.Or(ancestor[u][v], ancestor[v][u]))
    cost = z3.Sum([z3.Abs(depth[u] - depth[v]) for u, v in target["edges"]] + [z3.IntVal(0)])
    solver.add(cost <= target["K"])
    return solver, parent


def target_answers(target, count=2):
    solver, parent = target_solver(target)
    answers = []
    for _ in range(count):
        result = solver.check()
        if result == z3.unsat:
            break
        if result != z3.sat:
            raise RuntimeError(f"Target solver returned {result}")
        model = solver.model()
        values = [model.eval(p).as_long() for p in parent]
        answer = {"parent": values}
        assert target_cost(target, answer) is not None
        assert target_cost(target, answer) <= target["K"]
        answers.append(answer)
        solver.add(z3.Or(*(p != v for p, v in zip(parent, values))))
    return answers or ["NO-SOLUTION"]


def candidate_call(candidate, payload, extract=False):
    command = [sys.executable, str(candidate)] + (["--extract"] if extract else [])
    run = subprocess.run(command, input=json.dumps(payload), text=True, capture_output=True,
                         cwd=WORK, check=True)
    return json.loads(run.stdout)


def self_test(cases):
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location("corpus_gate", ROOT / "research/validate_preparation.py")
    gate = module_from_spec(spec)
    spec.loader.exec_module(gate)
    gate.validate_cases(cases)
    from generate_cases import optimum
    for case in cases:
        source = case["source"]
        rng_case = None
        if case["kind"] == "random":
            rng_case = regenerated_random(case["seed"])
            assert rng_case == source, case["seed"]
        brute = optimum(source["n"], source["edges"])
        z3_value, order = source_optimum(source)
        assert brute == z3_value == case["optimum"], source
        expected = {"order": order} if brute <= source["k"] else "NO-SOLUTION"
        assert valid_source(source, expected, brute)
        assert not valid_source(source, {"order": list(range(source["n"] + 1))}, brute)
        assert valid_source(source, "NO-SOLUTION", brute) == (brute > source["k"])
    assert target_cost({"n": 3, "edges": [[0, 1], [1, 2]], "K": 2},
                       {"parent": [-1, 0, 1]}) == 2
    assert target_cost({"n": 3, "edges": [[0, 1], [0, 2]], "K": 2},
                       {"parent": [-1, 0, 0]}) == 2
    assert target_cost({"n": 3, "edges": [[1, 2]], "K": 2},
                       {"parent": [-1, 0, 0]}) is None
    assert target_cost({"n": 2, "edges": [], "K": 0}, {"parent": [1, 0]}) is None
    assert target_answers({"n": 2, "edges": [[0, 1]], "K": 0}) == ["NO-SOLUTION"]
    assert len(target_answers({"n": 2, "edges": [[0, 1]], "K": 1})) == 2
    # Cross-check the tree encoding against direct parent enumeration on all
    # graphs with at most three vertices and several thresholds.
    for n in range(1, 4):
        pairs = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [list(e) for i, e in enumerate(pairs) if mask & (1 << i)]
            for bound in range(-1, 5):
                target = {"n": n, "edges": edges, "K": bound}
                brute_yes = any(
                    (cost := target_cost(target, {"parent": list(parents)})) is not None
                    and cost <= bound
                    for parents in itertools.product(range(-1, n), repeat=n)
                )
                assert (target_answers(target, 1)[0] != "NO-SOLUTION") == brute_yes
    assert not valid_source({"n": 3, "edges": [[0, 2]], "k": 1},
                            {"order": [0, 1, 2]})
    print(f"Self-test passed: {len(cases)} source labels, target witnesses and NO-SOLUTION")


def regenerated_random(seed):
    from generate_cases import optimum
    import random
    rng = random.Random(seed)
    n = rng.choice((3, 4, 5))
    density = rng.choice((0.2, 0.45, 0.7, 0.95))
    edges = [list(e) for e in itertools.combinations(range(n), 2) if rng.random() < density]
    k = optimum(n, edges) + rng.choice((-2, -1, 0, 0, 1, 2))
    return {"n": n, "edges": edges, "k": k}


def candidate_test(cases, candidate):
    outputs = yes = no = alternate = 0
    for index, case in enumerate(cases):
        source = case["source"]
        target = candidate_call(candidate, source)
        assert isinstance(target, dict) and isinstance(target.get("n"), int)
        assert target["n"] >= 1 and isinstance(target.get("K"), int)
        assert isinstance(target.get("edges"), list)
        assert all(isinstance(e, list) and len(e) == 2 and all(type(v) is int for v in e)
                   and 0 <= e[0] < e[1] < target["n"] for e in target["edges"])
        assert len({tuple(e) for e in target["edges"]}) == len(target["edges"])
        answers = target_answers(target)
        for answer in answers:
            recovered = candidate_call(candidate, {"source": source, "target_solution": answer}, True)
            assert valid_source(source, recovered, case["optimum"]), (index, source, target, answer, recovered)
            outputs += 1
            no += answer == "NO-SOLUTION"
            yes += answer != "NO-SOLUTION"
        alternate += len(answers) == 2
    print(f"Candidate passed: {len(cases)} instances, {outputs} target outputs; "
          f"{yes} witnesses, {no} NO-SOLUTION, {alternate} alternate witness pairs")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test", action="store_true")
    group.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    cases = json.loads((WORK / "cases.json").read_text())
    if args.self_test:
        self_test(cases)
    else:
        candidate_test(cases, args.candidate.resolve())


if __name__ == "__main__":
    main()
