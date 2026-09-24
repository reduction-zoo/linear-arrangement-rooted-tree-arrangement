# Linear Arrangement with a threshold → Rooted Tree Arrangement with a threshold

**Status:** `ready_for_expert_review` · **Research model:** `gpt-6-sol` · **Submitted:** 2026-09-23

The public campaign supplies deterministic polynomial-time construction and recovery for the fixed Linear Arrangement with a threshold to Rooted Tree Arrangement with a threshold contract. Every valid target output recovers a valid source output, including NO-SOLUTION where applicable.

## Construction

Make the original vertices a clique, which forces them onto one ancestor chain in every valid target tree. Add one vertex adjacent to the endpoints of each source edge. The clique contributes a fixed baseline, and the edge vertices encode the source arrangement cost: in the main case, the target optimum is `n(n²-1)/6 + OPT_source + 2m`. The proof covers branching target trees, the decoder for every valid output, and the small and negative-threshold cases.

## Evidence

- **Mathematical correctness and recovery: Written proof; independent agent review advanced.** The general proof covers the fixed endpoint semantics and every valid target output. The [final fresh-context review](campaigns/linear-arrangement-rooted-tree-arrangement/reviews/final/review.md) found no remaining correctness gap and advanced the candidate to expert review. Human expert acceptance remains pending.
- **Construction and recovery complexity: Written polynomial bounds.** The [proof](campaigns/linear-arrangement-rooted-tree-arrangement/work/proof.md) covers explicit graph encodings, polynomial runtime and output size, and arbitrary-length numerical parameters. No formal certification or optimality claim is made.
- **Executable verification: Finite checks passed.** The prepared suite passed 114 source instances and 188 actual target outputs; a separate exhaustive suite passed 102 instances and 166 actual target outputs. Large-integer CLI checks also passed. These checks supplement the general proof; see the [verification record](campaigns/linear-arrangement-rooted-tree-arrangement/work/verification.md).
- **Formal certification, human acceptance and historical novelty: Pending or unresolved.** No Lean certification or human expert acceptance is recorded. Garey–Johnson GT45 attributes this reduction to Gavril; the original proof was unavailable, so novelty of this exact gadget remains unknown. See the [campaign state](campaigns/linear-arrangement-rooted-tree-arrangement/state.md).

## Reproduce

Run from the repository root with Python 3.12 or later:

```sh
uv sync --locked
uv run --locked python campaigns/linear-arrangement-rooted-tree-arrangement/work/check.py --candidate campaigns/linear-arrangement-rooted-tree-arrangement/work/algorithm.py
uv run --locked python campaigns/linear-arrangement-rooted-tree-arrangement/work/verify.py --candidate campaigns/linear-arrangement-rooted-tree-arrangement/work/algorithm.py
```

The [verification record](campaigns/linear-arrangement-rooted-tree-arrangement/work/verification.md) lists the oracle self-test and focused encoding and large-integer checks. The finite checks exercise the executable maps; the general claim rests on the written proof.

## Artifacts

- [Fixed question](campaigns/linear-arrangement-rooted-tree-arrangement/question.md)
- [Campaign state](campaigns/linear-arrangement-rooted-tree-arrangement/state.md)
- [Manuscript](campaigns/linear-arrangement-rooted-tree-arrangement/work/manuscript.pdf)
- [Construction and recovery](campaigns/linear-arrangement-rooted-tree-arrangement/work/algorithm.py)
- [General proof](campaigns/linear-arrangement-rooted-tree-arrangement/work/proof.md)
- [Independent review](campaigns/linear-arrangement-rooted-tree-arrangement/reviews/final/review.md)
- [Verification evidence](campaigns/linear-arrangement-rooted-tree-arrangement/work/verification.md)

## Scope

The independent agent review advanced this result to expert review. The board records it as a submitted solution; no human expert acceptance, formal proof, or upstream integration is claimed. The existence of a reduction is classical, and the exact gadget's historical novelty remains unresolved.
