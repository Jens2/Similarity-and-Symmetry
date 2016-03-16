from lfn.colorrefinement import checkNeighbourhood

def put(coloring, color, v):
    v.setColornum(color)
    if coloring.get(color) is not None:
        coloring[color].append(v)
    else:
        coloring[color] = [v]

def remove(coloring, v):
    coloring[v.getColornum()].remove(v)

def move(coloring, v, to):
    remove(coloring, v)
    put(coloring, to, v)

def move_all(coloring, vs, to):
    for v in vs:
        move(coloring, v, to)

def get_color_classes(coloring):
    return [coloring.get(key) for key in coloring.keys()]

def colors(coloring):
        return [c for c in coloring.keys() if coloring.get(c) is not None and len(coloring.get(c)) > 0]

def deepcopy(coloring):
    deep_copy = dict()
    for c in colors(coloring):
        deep_copy[c] = coloring[c]
    return deep_copy

def k_of(coloring):
    k = 0
    for color_class in coloring.keys():
        if len(coloring.get(color_class)) > 0:
            k += 1
    return k

def isStable(coloring):
    for color_class in coloring.colors():
        v = coloring[color_class][0]
        for u in coloring[color_class][1:]:
            if not checkNeighbourhood(u, v):
                return False
    return True

def isUniform(coloring):
    return k_of(coloring) == 1

def isDiscrete(coloring):
    for color_class in coloring.keys():
        if len(coloring[color_class]) > 1:
            return False
    return True


def get_coloring(G):
    alpha = dict()
    highest_degree = -1
    for v in G.V():
        put(alpha, v.getDegree(), v)
        if highest_degree < v.getColornum():
            highest_degree = v.getColornum()
    changed = True
    # De colour refinement:
    while changed:
        changed = False
        for colour_list in get_color_classes(alpha):
            change_list = []
            u = colour_list[0]
            for v in colour_list[1:]:
                if not checkNeighbourhood(u, v):
                    changed = True
                    change_list.append(v)
            move_all(alpha, change_list, highest_degree + 1)
            if changed:
                highest_degree += 1
    return alpha

def coloring_refinement(coloring, highest_degree = -1):
    if highest_degree == -1:
        for key in coloring.keys():
            if key > highest_degree:
                highest_degree = key
    changed = True
    while changed:
        changed = False
        for colour_list in get_color_classes(coloring):
            change_list = []
            u = colour_list[0]
            for v in colour_list[1:]:
                if not checkNeighbourhood(u, v):
                    changed = True
                    change_list.append(v)
            move_all(coloring, change_list, highest_degree + 1)
            if changed:
                highest_degree += 1
    return coloring




"############################## Testing ##############################"

from util.graphutil import *


GL, options = loadgraph('testGraphs\\colorref_smallexample_4_7.grl', FastGraph, True)
G = loadgraph("bigtrees1.grl", FastGraph, True)[0][0]
H = disjointunion(GL[1], GL[3])
alpha = get_coloring(G)
beta = get_coloring(H)

writeDOT(G, "test_get_coloring_alpha.dot")
writeDOT(H, "test_get_coloring_beta.dot")

