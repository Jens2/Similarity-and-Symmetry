from graphImplementations.fastgraphs import graph
def colorref(G):
    a = dict()
    for v in G.V():
        a[v] = 1
    i = 0
