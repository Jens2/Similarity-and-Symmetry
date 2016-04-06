from final.graphutil import disjoint_union
from final.countisomorphism import count_isomorphism


def count_automorphism(g):
    h = disjoint_union(g, g)
    return count_isomorphism(h)
