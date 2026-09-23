"""Separate exhaustive verification through order 3 and sparse order 4."""

import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path


def call(candidate, payload, extract=False):
    command = [sys.executable, str(candidate)] + (["--extract"] if extract else [])
    run = subprocess.run(command, input=json.dumps(payload), text=True, capture_output=True,
                         check=True)
    return json.loads(run.stdout)


def cost_of_tree(graph, parent):
    n = graph["n"]
    if len(parent) != n or parent.count(-1) != 1:
        return None
    paths = []
    for start in range(n):
        path, vertex = [], start
        while vertex != -1:
            if vertex in path or vertex >= n:
                return None
            path.append(vertex)
            vertex = parent[vertex]
        paths.append(path)
    if len({path[-1] for path in paths}) != 1:
        return None
    total = 0
    for u, v in graph["edges"]:
        if u not in paths[v] and v not in paths[u]:
            return None
        total += abs(len(paths[u]) - len(paths[v]))
    return total


def source_cost(order, edges):
    position = {v: i for i, v in enumerate(order)}
    return sum(abs(position[u] - position[v]) for u, v in edges)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", required=True, type=Path)
    candidate = parser.parse_args().candidate.resolve()
    instances = outputs = yes = no = alternate = 0
    for n in range(5):
        pairs = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            if n == 4 and mask.bit_count() > 2:
                continue
            edges = [list(e) for i, e in enumerate(pairs) if mask & (1 << i)]
            orders = list(itertools.permutations(range(n)))
            optimum = min(source_cost(order, edges) for order in orders)
            tree_cache = {}
            for bound in (optimum - 1, optimum, optimum + 1):
                source = {"n": n, "edges": edges, "k": bound}
                target = call(candidate, source)
                assert target["n"] >= 1 and target["K"] >= 1
                assert len({tuple(edge) for edge in target["edges"]}) == len(target["edges"])
                assert all(0 <= u < v < target["n"] for u, v in target["edges"])
                key = (target["n"], tuple(map(tuple, target["edges"])))
                if key not in tree_cache:
                    trees = []
                    for parent in itertools.product(range(-1, target["n"]), repeat=target["n"]):
                        value = cost_of_tree(target, parent)
                        if value is not None:
                            trees.append((value, {"parent": list(parent)}))
                    assert trees
                    tree_cache[key] = trees
                trees = tree_cache[key]
                candidates = [tree for value, tree in trees if value <= target["K"]]
                chosen = candidates[:2] or ["NO-SOLUTION"]
                for answer in chosen:
                    recovered = call(candidate, {"source": source, "target_solution": answer}, True)
                    if optimum > bound:
                        assert recovered == "NO-SOLUTION", (source, target, answer, recovered)
                    else:
                        assert isinstance(recovered, dict) and sorted(recovered["order"]) == list(range(n))
                        assert source_cost(recovered["order"], edges) <= bound
                    outputs += 1
                    yes += answer != "NO-SOLUTION"
                    no += answer == "NO-SOLUTION"
                alternate += len(chosen) == 2
                instances += 1
    print(f"Exhaustive verification passed: {instances} instances, {outputs} target outputs; "
          f"{yes} witnesses, {no} NO-SOLUTION, {alternate} alternate witness pairs")


if __name__ == "__main__":
    main()
