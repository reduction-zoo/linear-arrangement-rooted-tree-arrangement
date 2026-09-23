"""Clique-spine reduction and recovery for the fixed arrangement problems."""

import json
import sys


def forward(source):
    n, edges, k = source["n"], source["edges"], source["k"]
    if k < 0:
        return {"n": 3, "vertices": [0, 1, 2], "edges": [[0, 1], [0, 2], [1, 2]], "K": 1}
    if n <= 1:
        return {"n": 1, "vertices": [0], "edges": [], "K": 1}
    m = len(edges)
    clique = [[u, v] for u in range(n) for v in range(u + 1, n)]
    gadget_edges = [[endpoint, n + i] for i, pair in enumerate(edges) for endpoint in pair]
    return {"n": n + m, "vertices": list(range(n + m)), "edges": clique + gadget_edges,
            "K": n * (n * n - 1) // 6 + k + 2 * m}


def extract(source, target_solution):
    if target_solution == "NO-SOLUTION":
        return "NO-SOLUTION"
    n = source["n"]
    parent = target_solution["parent"]
    depths = []
    for vertex in range(n):
        depth, current = 0, vertex
        while parent[current] != -1:
            current = parent[current]
            depth += 1
            if depth > len(parent):
                raise ValueError("cyclic parent array")
        depths.append(depth)
    return {"order": sorted(range(n), key=lambda vertex: depths[vertex])}


def main():
    payload = json.load(sys.stdin)
    result = (extract(payload["source"], payload["target_solution"])
              if sys.argv[1:] == ["--extract"] else forward(payload))
    json.dump(result, sys.stdout)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
