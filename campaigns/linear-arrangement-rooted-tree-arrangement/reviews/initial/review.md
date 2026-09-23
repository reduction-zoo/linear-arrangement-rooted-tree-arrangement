# Initial independent review — candidate `4f88baf`

**Decision: advance to expert review.** The current construction, proof and
implemented decoder satisfy the fixed search reduction contract. The existence
of an Optimal Linear Arrangement to Rooted Tree Arrangement transformation is
classical; this review does **not** establish that the clique and edge-vertex
construction is historically new. The fixed question explicitly permits a
reconstruction of a published reduction.

## Correctness

For `n >= 2` and `k >= 0`, [the construction](../../work/algorithm.py#L7)
makes the original vertices a clique and adds one vertex adjacent to the two
endpoints of each source edge. The new graph is simple even when the source edge
list presents endpoints in either order. It has `n+m` vertices,
`binom(n,2)+2m` edges, and positive integer threshold `C_n+k+2m`.

I checked the key inequality in [the proof](../../work/proof.md#L35)
independently. Clique vertices are ancestor-comparable in every valid target
tree, hence form one chain. Their edge cost is exactly `C_n + sum_g
a_g(n-a_g)`, summing over gadget vertices strictly between the first and last
original vertices on that chain. Each such summand is at least one. For a
source edge whose endpoints have rank difference `d`, its gadget's two edges
cost at least `d+2` unless the gadget is strictly between those endpoints.
In that case the cost is at least `d+1`, and this gadget incurs its own clique
surcharge of at least one. A gadget in a branch below the lower endpoint is
still comparable with both endpoints and falls in the full-cost case. Thus
every valid target tree has cost at least `C_n + cost_G(decoded order) + 2m`.
The path with each gadget as a child of its later endpoint attains
`C_n + cost_G(order) + 2m` for any source order. The optimum identity at
[proof lines 24–55](../../work/proof.md#L24) follows. I found no missing
premise in that inference.

The implemented [decoder](../../work/algorithm.py#L20) follows parent arcs to
compute depths and sorts the original vertices. Valid target outputs have a
well-formed parent array on graph-vertex labels; the clique makes these depths
distinct, so this is exactly the order in the inequality. The array is a
canonical encoding of the tree and its bijection: rename each tree vertex by
the graph vertex mapped to it. This normalization is polynomial if a solver
uses separate tree labels. The proof could state this encoding convention
explicitly in [the recovery section](../../work/proof.md#L57); it is a
presentation clarification, not a correctness gap.

For `k < 0`, every source arrangement has nonnegative cost, and the output
triangle with `K=1` has minimum rooted-tree cost four. For `n <= 1` and
`k >= 0`, the one-vertex target has a witness and the decoder returns the empty
or singleton source order. In all cases the target has a valid semantic output:
a witness or `NO-SOLUTION`. The optimum identity gives the equivalence of
`NO-SOLUTION` in the main case, so [decoder lines 20–34](../../work/algorithm.py#L20)
cover every valid target output, including alternate trees.

Both maps are deterministic. With an explicitly encoded source graph,
`m <= binom(n,2)` and `n` is bounded by input length. Forward output has
`O(n²)` edges and `O(n² log n + bitlength(k))` bits; integer arithmetic on the
threshold is polynomial. On a valid target parent array, the decoder uses at
most `n(n+m)` parent steps and a polynomial sort. Its output has `O(n log n)`
bits. These are the bounds claimed at [proof lines 68–72](../../work/proof.md#L68).

I inspected the full injected-instance path in [check.py lines 258–278](../../work/check.py#L258):
it calls both candidate modes as subprocesses, solves each constructed target
instance independently with the exact subset DP, and validates recovered
orders against independent source optima. [verify.py](../../work/verify.py)
uses a separate brute-force target enumerator on its smaller family. The DP's
cut recurrence is justified because a tree arc contributes the cut of its
child subtree, and connected components after removing a root can be detached
into separate child branches without increasing any edge distance. Its finite
cross-checks against Z3 and direct parent enumeration support the test oracle,
not the universal theorem. I did not rerun those suites. As a targeted current
implementation check, I invoked both CLI modes on the two-vertex one-edge
source with `k=1`: the target was a triangle with `K=4`, and both an
endpoint-leaf tree and an internal-gadget tree had independently calculated
cost four and decoded to source order `[0,1]`. With `k=0`, the target threshold
was three and `NO-SOLUTION` decoded correctly. The check passed on 2026-09-23.

## Novelty

The [Garey–Johnson GT45 entry](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf)
already states a transformation from Optimal Linear Arrangement to Rooted Tree
Arrangement and attributes it to Gavril, *Some NP-complete problems on graphs*,
1977, pp. 91–95. The GT45 problem definition matches the ancestor-comparability
and sum-of-tree-distances target here, so the existence of this reduction and
the NP-hardness consequence are not new. The [upstream rule issue](https://github.com/CodingThrust/problem-reductions/issues/888)
discusses why the identity graph map fails and names Gavril but supplies no
gadget or decoder; it does not settle whether this particular construction was
published. A [1996 primary CSP paper](https://www.cs.utexas.edu/~miranker/papers/1996/aaai96.pdf),
in its “Rooted-Tree Arrangements” section, confirms the same comparability
notion but supplies no matching reduction in that section.

Search performed 2026-09-23 for the exact 1977 title, the cited report number,
the two problem names, and clique/gadget variants. A later bibliography points
to a Technion reprint `CS-2011-05`, but the [reported PDF URL](https://www.cs.technion.ac.il/users/wwwb/cgi-bin/tr-get.cgi/2011/CS/CS-2011-05.pdf)
currently returns 404. I could not inspect Gavril's proof, so equivalence of
the exact gadget, optimum offset or recovery algorithm to that original remains
unresolved. The review supports “newly derived in this campaign,” as stated at
[proof line 73](../../work/proof.md#L73), but not a global originality claim.
This literature limit must accompany any manuscript or public claim.

## Significance

Relative to the GT45 listing and the upstream issue, the concrete contribution
is a short, executable instance map and a decoder that handles every target
witness and `NO-SOLUTION`. The clique controls branching among the vertices
that need decoding; the edge gadgets encode source distances, and the charging
argument handles gadgets inserted on the clique chain. This meets the fixed
rule-completion criterion even if Gavril used an equivalent construction.

The dominant construction overhead is the `Theta(n²)` clique edges, `m` extra
vertices, and an additive `Theta(n³)` baseline in the threshold. The encoding
remains polynomial, but the dense target may be costly for solvers. Evidence
only covers the small instances recorded in [verification.md](../../work/verification.md);
there are no practical-scale measurements or performance claims to accept.

## Isolation and route

This reviewer received a fresh task context with the candidate paths and
commit, without the proposer's reasoning. The registered
[Codex reviewer instructions](../../../../.codex/agents/research-reviewer.toml)
and [research-review charter](../../../../.agents/skills/research-review/SKILL.md)
were in force as instructions. The actual tool surface still exposed agent
spawning, there was no enforced delegation depth cap, and filesystem mode was
`danger-full-access` with no write sandbox. I obeyed the instruction to write
only here; it was not technically enforced by tool denial or a sandbox. The
model route available to this review was **Codex GPT-6**; the exact variant and
the proposer's route were not exposed, so no cross-model independence is
claimed. The fresh context and explicit review boundary provided process
separation, while the proof and checks above provide the correctness evidence.
