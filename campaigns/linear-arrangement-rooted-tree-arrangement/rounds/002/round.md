# Round 002 — explicit graph encoding repair

## Plan

The mathematical mechanism in round 001 passed an independent review, but
the executable JSON wrote `n` as a number and did not enumerate isolated
vertices. On that encoding an edgeless graph with huge binary `n` is a short
input, so constructing its clique is not polynomial in the encoded length.
The fixed question requires graphs to be explicit. Repair source and target
JSON encodings with vertex lists `[0,...,n-1]`, require them to match `n`, and
regenerate the fixed cases with unchanged graph meanings, seeds and optima.
Both F and G continue to use the same mathematical rule.

First discriminating check: the unchanged 114 graph meanings must regenerate
with explicit vertices and pass the corpus gate, oracle self-test, candidate
suite and separate exhaustive verifier. A failure will identify an encoding
or implementation mismatch; passing checks will leave the bit-size argument
and focused independent re-review.

Experience retrieval: [clique-spine charging](../../../../research/experience/clique-spine-charging.md)
continues to apply because graph adjacency and gadget geometry are unchanged.
No other local or board entry addresses explicit vertex-list encoding.

## Evidence and diagnosis

The original JSON encoded an edgeless graph of order `n` with only `O(log n)`
digits. The prior output bound therefore needed an unstated explicit-graph
premise. This was an executable encoding defect, not a counterexample to the
clique charging lemma. The repaired contract requires a vertex array of length
`n` on both sides. `algorithm.py` writes that array in every branch, including
the fixed NO triangle and the singleton YES instance; `proof.md` now bounds
output bits against the actual input array length. The mathematical map and
decoder are unchanged.

The pre-implementation self-test failed with `KeyError: 'vertices'`, detecting
the missing field. After regeneration, the corpus gate again passed 114
distinct cases (100 random, 14 edge). All source graph meanings, seeds,
thresholds and independently derived optima match the previous corpus.
Self-test passed; the prepared loop passed 114 instances, 188 target outputs;
and the separate brute-force verifier passed 102 instances, 166 target outputs.
The output counts and YES/NO splits are unchanged; see
[verification](../../work/verification.md). No target solver result was treated
as a proof of the size bound.

Outcome: **supported**, pending focused independent re-review of the repaired
encoding and proof bound. Experience extraction: no new entry; this is an
encoding obligation specific to the repository contract. The existing
[clique-spine entry](../../../../research/experience/clique-spine-charging.md)
remains valid; its use here left the charging argument unchanged.

## Next action

Commit this repair and request focused re-review, then write the manuscript.
