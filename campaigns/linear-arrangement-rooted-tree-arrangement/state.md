# Campaign state

Budget: 20 rounds. Used: 2. Remaining: 18.
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
received an [independent advance review](reviews/initial/review.md) at commit
`4f88baf`. Round 002 repaired the executable encoding: both graphs now list
vertices explicitly, including isolated ones, and the polynomial bit bound
uses that actual representation. All prepared and separate checks passed again.
The [focused review](reviews/encoding/review.md) found a large-integer CLI
failure, which is repaired and checked end to end; focused re-review of that
last change remains. Novelty
relative to Gavril 1977 remains unknown
because the original paper has not been checked. Significance: executable
witness recovery addresses the fixed gap; practical overhead is unmeasured.
Prospects of completing this candidate within the remaining budget: high,
uncalibrated, based on the short cost proof and passing checks.

Next action: commit the large-integer repair and obtain focused re-review
before writing.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Original-vertex clique spine plus one edge vertex per source edge; first mechanism | 114-case injected target solve and recovery | supported; initial review advanced | [round 001](rounds/001/round.md) |
| 002 | Explicit graph encoding and arbitrary-length integer I/O; closes the executable size and totality proof premise without changing the gadget | Existing 114-case corpus gate must still pass with explicit vertices | supported after repair; focused re-review pending | [round 002](rounds/002/round.md) |
