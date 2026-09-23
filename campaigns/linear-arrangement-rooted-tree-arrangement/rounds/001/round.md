# Round 001 — clique spine with one edge vertex per source edge

## Plan

Gap: a target tree can branch, so an arbitrary target witness need not yield a
linear arrangement of equal or lower cost. The bare graph fails already on a
four-vertex star (tree cost 3, minimum linear cost 4).

Mechanism: make all original vertices a clique. They must lie on one ancestor
chain, and the clique's baseline distance sum is independent of their order.
For each source edge, add one vertex adjacent to its endpoints. The candidate
threshold is the clique baseline plus `k+2m`; recover the order of original
vertices by depth. A gadget on the ancestor chain between its endpoints can
save at most one relative to a leaf placement, while it increases the clique
cost by at least one. This is the proposed charging lemma.

First discriminating check: implement both maps and run the prepared 114-case
candidate loop, including negative instances and alternate target witnesses.
A mismatch refutes the claimed formula or implementation; passing finite checks
will leave the general charging lemma and independent review to establish.

Experience retrieval: searched local and board entries for `tree arrangement`,
`linear arrangement`, `ancestor`, and `branching` on 2026-09-23; no relevant
entry was found. Composition assumption: all original clique vertices share a
single ancestor chain, and leaf edge gadgets can be attached independently.

## Evidence and diagnosis

The construction and exact optimum identity are in
[the candidate proof](../../work/proof.md). The first prepared run with a
generic Z3 target encoding was interrupted after more than two minutes in a
larger case; Z3 returned `unknown` on interruption. This was an execution
failure, not a NO answer. Replacing that target-solving path with the exact
component subset DP produced a conclusive suite. No source case or expected
answer changed. The target DP was cross-checked against Z3 and direct tree
enumeration on all graphs through three vertices.

The prepared loop passed 114 instances and 188 target outputs (150 witnesses,
38 NO-SOLUTION; 74 pairs of alternate optimal trees). An independently coded
brute-force verifier passed 102 other threshold instances and 166 outputs,
including 34 NO-SOLUTION and 64 alternate-tree pairs. It enumerated every
target parent array in its family. See [verification](../../work/verification.md).

The bare identity map's failed assumption is recorded in the plan: branching
can lower cost. The clique forces only the original vertices onto a chain;
the charging lemma handles gadget vertices that remain on the chain. The
candidate has a general proof, so this round's outcome is **supported**, with
novelty and independent assessment pending. The original Gavril 1977 paper
has not been located or read. The [upstream issue](https://github.com/CodingThrust/problem-reductions/issues/888)
documents the failed identity map but does not give this construction; it was
checked 2026-09-23. A broad web search found the Garey–Johnson GT45 listing
but no accessible original proof, so the construction's global novelty remains
unsettled.

Experience extraction: [clique-spine charging](../../../../research/experience/clique-spine-charging.md)
created 2026-09-23; its general lemma may guide other ancestor-layout
reductions. No board entry was edited.

## Next action

Commit this round, request fresh-context independent review, then write the
paper if the reviewer advances it.
