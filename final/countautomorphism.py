from final.graphutil import disjoint_union
from final.countisomorphism import count_isomorphism
from final.graphIO import loadgraph
from final.fastgraphs import FastGraph


def count_automorphism(g):
    h = disjoint_union(g, g)
    return count_isomorphism(h)

# ----- MAIN -----

GL, settings = loadgraph("graphs\\torus24.grl", FastGraph, True)
G = GL[0]
print(count_automorphism(G))

