# Campaign state

Budget: 20 rounds. Used: 1. Remaining: 19.
Board source: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.

Capability probe (2026-09-23):

| Capability | Version / provider or path | Status |
|---|---|---|
| Python | 3.12.14, `/Users/xiweipan/.local/bin/python3` | available |
| uv | 0.12.17, `/Users/xiweipan/.local/bin/uv` | available |
| SMT and Python binding | Z3 5.1.0, `/opt/homebrew/bin/z3`; `z3-solver` 5.1.0.0 in `uv.lock` | available and selected oracle |
| SAT | Kissat 4.0.4, `/opt/homebrew/bin/kissat` | available |
| CP-SAT | OR-Tools executable and Python package absent | pending; not needed by selected oracle |
| Typst | 0.15.1, `/opt/homebrew/bin/typst` | available |
| Lean / Lake | Lean 4.34.0 and Lake 5.0.0, `/opt/homebrew/bin` | available |
| Mathlib | no local Mathlib project or installed library found | pending; formalization not requested |
| Writing skill | `sci-brain:how-to-technical-writing` SKILL.md in local plugin cache | available |

Prepare: [114 fixed cases and passing independent oracle self-tests](work/preparation.md),
committed as `aa17760` before construction.

Current claim: [clique-spine reduction](work/proof.md) with executable
[forward and recovery maps](work/algorithm.py). The derived cost identity is
`OPT_target = n(n²-1)/6 + OPT_source + 2m` in the main case, with explicit
negative-threshold and trivial-size cases. [Verification](work/verification.md)
passed 114 prepared instances plus 102 separately enumerated instances;
universal correctness rests on the proof, not those finite counts. Correctness
is pending independent review. Novelty relative to Gavril 1977 remains unknown
because the original paper has not been checked. Significance: executable
witness recovery addresses the fixed gap; practical overhead is unmeasured.
Prospects of completing this candidate within the remaining budget: high,
uncalibrated, based on the short cost proof and passing checks.

Next action: commit round 001, then fresh-context independent review.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Original-vertex clique spine plus one edge vertex per source edge; first mechanism | 114-case injected target solve and recovery | supported, review pending | [round 001](rounds/001/round.md) |
