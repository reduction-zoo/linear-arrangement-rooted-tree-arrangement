# Clique-spine charging for rooted-tree layout gadgets

## Claim and applicability

Tags: rooted tree arrangement, ancestor comparability, clique spine, cost
charging. If designated graph vertices form a clique, they form an ancestor
chain in every valid rooted-tree arrangement. Their pair-distance baseline is
order-independent. A nonclique vertex inserted between designated vertices
adds `a(b)` to clique cost, where `a` and `b` count designated vertices on
opposite sides. This can pay for a bounded cost saving by that vertex's own
edges. The numerical saving must be proved for the particular gadget; the
lemma alone does not give a reduction.

## Evidence and status

General counting lemma, proved for a two-edge gadget in
[round 001](../../campaigns/linear-arrangement-rooted-tree-arrangement/rounds/001/round.md)
and [proof](../../campaigns/linear-arrangement-rooted-tree-arrangement/work/proof.md).
Finite checks are in [verification](../../campaigns/linear-arrangement-rooted-tree-arrangement/work/verification.md).
Independent review is pending. This entry was created 2026-09-23 in the
campaign repository; promotion to the board's local collection is pending
separate authorization.

## Consequence for search

When branching spoils direct recovery, a clique can force just the decoded
vertices onto a chain. Count the clique-distance increase caused by auxiliary
vertices on that chain before trying to force every auxiliary vertex off it.

## Use history

- [Round 001](../../campaigns/linear-arrangement-rooted-tree-arrangement/rounds/001/round.md): originated the lemma; the complete reduction passed finite checks.
