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

Pending.

## Next action

Repair the executable encoding and bounds, then request focused re-review.
