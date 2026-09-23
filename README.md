# Linear Arrangement with a threshold → Rooted Tree Arrangement with a threshold

Independent research campaign. A complete clique-spine reduction with
forward construction and recovery is [ready for expert review](campaigns/linear-arrangement-rooted-tree-arrangement/state.md).
The exact gadget's historical novelty remains unresolved because Gavril's
1977 proof was unavailable for comparison. Nothing has been published or
changed on the board.

[Question](campaigns/linear-arrangement-rooted-tree-arrangement/question.md) ·
[State](campaigns/linear-arrangement-rooted-tree-arrangement/state.md) ·
[Proof](campaigns/linear-arrangement-rooted-tree-arrangement/work/proof.md) ·
[Algorithm](campaigns/linear-arrangement-rooted-tree-arrangement/work/algorithm.py) ·
[Paper](campaigns/linear-arrangement-rooted-tree-arrangement/work/manuscript.pdf) ·
[Verification](campaigns/linear-arrangement-rooted-tree-arrangement/work/verification.md) ·
[Final independent review](campaigns/linear-arrangement-rooted-tree-arrangement/reviews/final/review.md).

Reproduce from this repository with `uv sync --locked`, then run the commands
in the paper's verification appendix. The candidate needs Python 3.12 or later;
the test oracles use the locked Z3 binding.

Board source commit: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.
