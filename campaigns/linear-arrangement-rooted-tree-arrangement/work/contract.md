# Executable problem contract

Vertices have labels `0..n-1`; edges are distinct pairs `[u,v]` with `u<v`.
The source input is `{"n": n, "vertices": [0,...,n-1], "edges": [...], "k": k}`,
where `n>=0` and `k` is an integer. The target input is
`{"n": n, "vertices": [0,...,n-1], "edges": [...], "K": K}`, where `n>=1`
and `K` is an integer. The vertex array is mandatory and must list all graph
vertices, including isolated ones. Thus graph order is at most input length;
the redundant `n` field must equal the array length. Numerical thresholds
use ordinary JSON decimal notation as a binary-size encoding. Malformed inputs
are outside the legal instance sets.

Source output is `{"order": [v_1,...,v_n]}` when the listed permutation has
edge-length sum at most `k`, or the JSON string `"NO-SOLUTION"` exactly when
there is no such permutation. This includes the empty permutation for `n=0`.

Target output is `{"parent": [p_0,...,p_{n-1}]}` where exactly one entry is
`-1` (the root), other entries are vertex labels, and the arcs form a tree.
Every graph edge has ancestor-comparable endpoints and its tree distance is
counted in the total, which must be at most `K`. `"NO-SOLUTION"` is the only
valid output when no such rooted tree exists.

`algorithm.py` reads one source JSON input from stdin and writes one target JSON
instance to stdout. `algorithm.py --extract` reads a JSON object with `source`
and `target_solution` and writes a source output. Each invocation is a fresh
process; diagnostics go to stderr and execution failures exit nonzero.
