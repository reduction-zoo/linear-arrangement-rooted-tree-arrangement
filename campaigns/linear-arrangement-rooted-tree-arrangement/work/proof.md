# Clique-spine reduction

Let the source graph have `n` vertices, `m` edges and threshold `k`. If `k<0`,
output a triangle with target threshold 1. Its three pairwise comparable
vertices form a chain and have total edge distance 4,
so its only valid output is `NO-SOLUTION`, as required for the source. If
`n<=1` and `k>=0`, output a single isolated target vertex with threshold 1;
both problems then have a witness. These choices keep the target threshold
positive even under the classical formulation of the target problem.

For `n>=2` and `k>=0`,
construct a target graph with the original vertices as a clique and one new
vertex `g_e` for each original edge `e=uv`. Join `g_e` to `u` and `v`, and add no
other gadget edges. Set

`C_n = sum_{1<=i<j<=n}(j-i) = n(n²-1)/6` and `K = C_n + k + 2m`.

The target graph is simple. Its vertex count is `n+m` and its edge count is
`n(n-1)/2+2m` in the main case. The source empty arrangement has cost zero,
as does the one-vertex target tree in its special case.

## Exact optimum identity

Write `L(G)` for minimum linear arrangement cost and `T(H)` for minimum rooted
tree arrangement cost. We claim

`T(H) = C_n + L(G) + 2m` for the main case.

For the upper bound, take any source order. Put the original vertices on a
root-to-leaf path in that order. For each edge `uv`, attach `g_e` as a child of
the later endpoint. The two gadget edges then have total tree distance
`|position(u)-position(v)|+2`. All clique edges have comparable endpoints and
total cost `C_n`. This is a valid rooted tree and achieves the displayed sum.

For the lower bound, take *any* valid target tree. Every pair of original
vertices is joined by a clique edge and hence ancestor-comparable. Therefore
the original vertices lie on a common root-to-leaf chain. List them by depth;
this gives a source order. For each gadget `g` on the chain between the first
and last original vertices, let `a_g` be the number of original vertices above
it. Its contribution to the clique's distances, beyond `C_n`, is
`a_g(n-a_g) >= 1`: precisely that many original pairs straddle it. Gadgets
outside that chain segment contribute zero extra clique distance. Thus the
clique costs at least `C_n` plus the number of gadgets internal to the chain
segment.

Now consider the gadget `g_e` for edge `e=uv`, with `u` above `v`. Let `d` be
their rank difference in the extracted order, and `D` their tree distance.
Always `D>=d`. Because `g_e` must be comparable with both endpoints, it is
either on their ancestor path, above `u`, or below `v`. If it is strictly
between `u` and `v`, its two incident edge distances sum to `D>=d+1`. This
gadget lies inside the original chain segment and accounts for at least one
unit of extra clique cost. Otherwise the sum is `D+2t>=d+2` for an integer
`t>=1`. Hence every gadget contributes at least `d+2`, except that an internal
one may save one unit, which its extra clique cost pays for. Summing gives
`T(H)>=C_n+L(G)+2m`, proving equality.

## Recovery and bounds

Given a valid target tree in the main case, recover the source permutation by sorting original
vertices by depth. The lower bound above shows its source cost is at most
`target_cost-C_n-2m<=k`. Given target `NO-SOLUTION`, exact optimum equality
implies source infeasibility, so return source `NO-SOLUTION`. In the special
`k<0` case, only target `NO-SOLUTION` is valid and it recovers source
`NO-SOLUTION`. In the `n<=1`, `k>=0` case, any valid target tree recovers the
empty or singleton permutation. Thus recovery works for every valid target
output, including alternate trees and negative source thresholds.

The input JSON explicitly lists all `n` source vertices, including isolated
ones, so `n` is at most the input length. The forward map writes `O(n²)` edges
and explicitly lists `n+m=O(n²)` target vertices, in polynomial time and
`O(n² log n + bitlength(k))` output bits. Arithmetic on `C_n+k+2m` has
`O(log(n+1)+bitlength(k))` bits. The recovery map follows at most `n+m` parent
arcs for each original vertex and sorts `n` depths, using
`O(n(n+m)+n log n)` operations on polynomial-size integers. No solver or state
from the forward process is used. This is a newly derived argument in this
campaign; the 1979 Garey–Johnson listing and upstream issue are context, not
the source of this proof.
