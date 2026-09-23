# Campaign state

Budget: 20 rounds. Used: 0.
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
committed before construction. Next action: round 001, inspect relevant
experience and test a branching-control mechanism.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
