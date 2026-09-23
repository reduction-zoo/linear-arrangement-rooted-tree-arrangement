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
passed 114 prepared instances plus 102 separately enumerated instances and
354 actual target outputs total, including positive, negative and alternate
tree answers. Large-integer CLI cases also passed. Universal correctness rests
on the proof, not these finite counts. The [initial independent review](reviews/initial/review.md)
advanced the mathematical result. Round 002 repaired the explicit-graph
encoding and arbitrary-length integer I/O, prompted by the
[focused review](reviews/encoding/review.md). The
[final fresh-context review](reviews/final/review.md) advanced the repaired
candidate. The [four-page Typst paper](work/manuscript.pdf) was compiled and
visually inspected page by page. Status: **ready_for_expert_review**, an agent
assessment rather than human certification.

Novelty of this exact gadget relative to Gavril 1977 remains unknown because
the original proof was unavailable. The reduction's existence and hardness
consequence are classical. Significance here is the explicit F/G rule and
all-output recovery for the fixed question. The dense target's practical
solver cost is unmeasured. Earlier prospect assessment before review: high,
uncalibrated, based on the short cost proof and passing finite checks. The
actual outcome is a reviewed candidate within two rounds.

Closeout: 20 authorized rounds, 2 used, 18 unused. One distinct mathematical
construction mechanism was attempted; round 002 repaired its executable
encoding and proof bound. Experience extraction: one distinct
[entry](../../research/experience/clique-spine-charging.md) created, the same
entry updated once, and one local entry pending promotion to the board's
uncommitted collection. The board was not edited. No formal proof was
requested; Mathlib and CP-SAT remain unavailable but did not block this
result. Next decision: human expert review and, separately, a historical
comparison with Gavril's primary proof if obtained. Publication and board
updates require human authorization.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Original-vertex clique spine plus one edge vertex per source edge; first mechanism | 114-case injected target solve and recovery | supported; initial review advanced | [round 001](rounds/001/round.md) |
| 002 | Explicit graph encoding and arbitrary-length integer I/O; closes the executable size and totality proof premise without changing the gadget | Existing 114-case corpus gate must still pass with explicit vertices | supported; final review advanced | [round 002](rounds/002/round.md) |
