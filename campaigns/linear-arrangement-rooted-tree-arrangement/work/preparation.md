# Prepared independent tests

The corpus contains 114 distinct legal source instances: 100 seeded random
instances (25 with 3 vertices, 37 with 4, 38 with 5) and 14 edge cases (two
each with 0, 1 and 4 vertices, four each with 2 and 3 vertices). There are 76
YES and 38 NO source answers. `generate_cases.py` records a seed on each random
case and its independent exhaustive optimum. It generates the same case from
each seed; deduplication makes the retained seeds nonconsecutive. It covers
empty and edgeless graphs, negative bounds, thresholds below/at/above optimum,
and multiple optimal arrangements.

`check.py` uses Z3 5.1.0 for independent source and target oracles. The source
variables form a permutation of positions; minimizing the exact sum of edge
lengths returns a witness and optimum. The target variables give one parent and
depth per vertex, exactly one root, depth increasing by one along parent arcs,
and ancestor relations recursively determined by parent arcs. Every graph edge
must have comparable endpoints. The exact sum of depth differences is bounded
by `K`. These constraints are equivalent to the target definition: depth
increase rules out parent cycles, one root gives a spanning tree, and the
ancestor recurrence follows the unique parent chain. Z3 SAT yields a directly
validated witness; UNSAT yields NO-SOLUTION; unknown raises an error. All
arithmetic is integer, so there is no tolerance or numerical ambiguity.

The self-test runs the corpus gate, regenerates each random input, recomputes
all source optima with Z3 and exhaustive permutations, validates returned
witnesses, and checks invalid permutations, over-budget arrangements, wrong
NO-SOLUTION answers, malformed/cyclic/incomparable target trees, and target
YES/NO decisions. It cross-checks the target solver's decision with exhaustive
parent enumeration for every graph on up to three vertices and thresholds -1
through 4. The candidate mode executes both candidate subprocess modes afresh,
solves each actual target instance independently, validates target witnesses,
and checks every recovered source output against the stored optimum. It seeks
two distinct target witnesses per YES target, where available.

Reproduction from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/linear-arrangement-rooted-tree-arrangement/work/generate_cases.py
uv run --locked python research/validate_preparation.py campaigns/linear-arrangement-rooted-tree-arrangement/work/cases.json
uv run --locked python campaigns/linear-arrangement-rooted-tree-arrangement/work/check.py --self-test
```

Observed: `Preparation corpus passed: 114 distinct cases, 100 random, 14 edge`;
`Self-test passed: 114 source labels, target witnesses and NO-SOLUTION`.
Oracle coverage is finite (source at most 5 vertices, target encoding checked
exhaustively through 3 vertices). These checks establish a testing foundation,
not a reduction. No test expectation was changed after fixing a candidate;
two initial oracle self-test coding errors were corrected before this result.
