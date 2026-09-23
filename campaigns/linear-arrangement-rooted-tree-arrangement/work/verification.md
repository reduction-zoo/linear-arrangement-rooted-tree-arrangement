# Independent executable verification

Candidate: `work/algorithm.py` and `work/proof.md` from round 001. Commands from
the repository root:

```sh
uv run --locked python campaigns/linear-arrangement-rooted-tree-arrangement/work/check.py --self-test
uv run --locked python campaigns/linear-arrangement-rooted-tree-arrangement/work/check.py --candidate campaigns/linear-arrangement-rooted-tree-arrangement/work/algorithm.py
uv run --locked python campaigns/linear-arrangement-rooted-tree-arrangement/work/verify.py --candidate campaigns/linear-arrangement-rooted-tree-arrangement/work/algorithm.py
```

Results on 2026-09-23: self-test passed; prepared suite passed 114 source
instances and 188 actual target outputs (150 tree witnesses, 38 NO-SOLUTION,
74 instances with two distinct optimal target trees). `verify.py` independently
enumerated all simple source graphs through three vertices and all graphs with
four vertices and at most two edges. It tested thresholds one below, at and one
above each exact source optimum: 102 instances, 166 actual target outputs (132
tree witnesses, 34 NO-SOLUTION, 64 instances with two target trees). It does
not import `check.py` or `algorithm.py`; both candidate modes run as subprocesses.
All target trees through six vertices in this extra family were enumerated and
checked against the target definition before recovery.

The prepared suite covers source size up to five and constructed target size
up to fifteen. Verification is finite, and the generic subset DP is exponential
test machinery. Neither run proves the universal cost identity; that obligation
is in `proof.md` and pending independent review. Practical cost claims beyond
these small instances are unmeasured.
