from final.coloringutil import is_balanced, defines_bijection
from final.coloring import alpha_coloring, minimization_partitioning
from final.graphIO import loadgraph
from final.fastgraphs import FastGraph
from final.graphutil import disjoint_union
from time import time


def is_isomorphism(g, D=[], I=[], iso_found=False):
    coloring = alpha_coloring(g, D, I)
    highest_degree = -1
    for key in coloring.keys():
        if key > highest_degree:
            highest_degree = key
    coloring = minimization_partitioning(coloring, highest_degree)

    for key in coloring.keys():
        color_class = coloring[key]
        for vertex in color_class:
            vertex.setColornum(key)

    if not is_balanced(coloring, len(g.V())):
        return False
    if defines_bijection(coloring):
        return True
    if iso_found:
        return True
    color_class = None
    for key in coloring.keys():
        if len(coloring.get(key)) >= 4:
            color_class = coloring.get(key)
            break
    x = None
    for node in color_class:
        if node.getLabel() < len(g.V()) // 2:
            x = node
    iso_found = False
    C_intersect_H = []
    for v in color_class:
        if v.getLabel() >= len(g.V()) // 2:
            C_intersect_H.append(v)
    D_x = []
    D_x.extend(D)
    D_x.append(x)
    for y in C_intersect_H:
        I_y = []
        I_y.extend(I)
        I_y.append(y)
        iso_found = is_isomorphism(g, D_x, I_y, iso_found) > 0
        if iso_found:
            return True
    return iso_found

def printTimeList(timeList):
    averageUnion = 0
    averageIso = 0
    no = 0
    for key in timeList.keys():
        no += 1
        averageUnion += timeList[key][0]
        averageIso += timeList[key][2]
        print("**************************")
        print(key + ":")
        print("Disjoint union:      " + str(timeList[key][0]))
        print("Is isomorphism:      " + str(timeList[key][1]))
        print("Time isomorphism:    " + str(timeList[key][2]))
    averageIso = averageIso / no
    averageUnion = averageUnion / no
    print("\n")
    print("Average time for disjoint union:     " + str(averageUnion))
    print("Average time for is isommorphism:    " + str(averageIso))
    print("Total average time:                  " + str(averageIso + averageUnion))
# ----- MAIN -----

GL, settings = loadgraph("graphs\\tree150.grl", FastGraph, True)
timeList = dict()
x = 0
y = 0
for j in range(len(GL)):
    x += len(GL[j].E())
    y += 1
print(x / y)
for j in range(len(GL)):
    if j != 0:
        timeEntry = []
        G = GL[x]
        H = GL[j]
        key = str(x) + " and " + str(j)
        start = time()
        union = disjoint_union(G, H)
        timeEntry.append(time() - start)
        start = time()
        timeEntry.append(is_isomorphism(union))
        timeEntry.append(time() - start)
        timeList[key] = timeEntry
printTimeList(timeList)
timeList = dict()
for i in range(len(GL)):
    for j in range(len(GL)):
        if i == j:
            timeEntry = []
            G = GL[i]
            H = GL[j]
            key = str(i) + " and " + str(j)
            start = time()
            union = disjoint_union(G, H)
            timeEntry.append(time() - start)
            start = time()
            timeEntry.append(is_isomorphism(union))
            timeEntry.append(time() - start)
            timeList[key] = timeEntry
printTimeList(timeList)
