from lfn.individualizationrefinement import *
# P := {F, Q \ F};
# W := {F};
# while (W is not empty) do
#      choose and remove a set A from W

#      for each c in Σ do
#           let X be the set of states for which a transition on c leads to a state in A

#           for each set Y in P for which X ∩ Y is nonempty and Y \ X is nonempty do
#                replace Y in P by the two sets X ∩ Y and Y \ X
#                if Y is in W
#                     replace Y in W by the same two sets
#                else
#                     if |X ∩ Y| <= |Y \ X|
#                          add X ∩ Y to W
#                     else
#                          add Y \ X to W
#           end;
#      end;
# # end;
# 1: P ← {F, Fc}                                ⊲ The initial partition
# 2: for all a ∈ A do
# 3:    Add((min(F, Fc), a),W)                  ⊲ The initial waiting set
# 4: while W != ∅ do
# 5:    (W , a) ← TakeSome(W)                   ⊲ takes some splitter in W and remove it
# 6:    for each P ∈ P which is split by (W , a) do
# 7:        P′,P′′ ← (W , a)|P                          ⊲ Compute the split
# 8:        Replace P by P′ and P′′ in P                 ⊲ Refine the partition
# 9:        for all b ∈ A do                        ⊲ Update the waiting set
# 10:           if (P, b) ∈ W then
# 11:               Replace (P, b) by (P′, b) and (P′′, b) in W
# 12:           else
# 13:               Add((min(P', P′′), b), W)


def minimizationpartitioning(colouringmap, highestDeg):
    W = [pick_smallest_splitter(colouringmap)]
    if None in W:
        W = []
    while len(W) > 0:
        # print(colouringmap)
        A = W.pop()
        classes_to_split = count_and_sort_neighbours(colouringmap, A)
        for colour_class in classes_to_split.keys():
            wcontains = False
            first = True
            new_minimal_entry = []
            nodecount = classes_to_split[colour_class]
            if colouringmap[colour_class] in W:
                W.remove(colouringmap[colour_class])
                wcontains = True
            for key in nodecount.keys():
                if len(new_minimal_entry) == 0 or (len(new_minimal_entry) != 0 and len(nodecount[key]) < len(new_minimal_entry)):
                    new_minimal_entry = nodecount[key]
                if not first:
                    highestDeg += 1
                    colouringmap[highestDeg] = nodecount[key]
                    if wcontains:
                        W.append(nodecount[key])
                    for node in nodecount[key]:
                        colouringmap[colour_class].remove(node)
                else:
                    if wcontains:
                        W.append(nodecount[key])
                    first = False
            if not wcontains:
                W.append(new_minimal_entry)
    return colouringmap

def pick_smallest_splitter(colouringmap):
    list_of_P = []
    for colour_class in colouringmap.values():
        list_of_P.append(colour_class)
    mergeSort(list_of_P)
    for i in range(len(list_of_P) - 1):
        if len(count_and_sort_neighbours(colouringmap, list_of_P[i])) > 0:
            return list_of_P[i]

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if len(lefthalf[i]) < len(righthalf[j]):
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def count_and_sort_neighbours(colouring, colour_class):
    no_of_neighbours = dict()
    list_of_colours = []
    for node in colour_class:
        for neighbour in node.nbs():
            if neighbour in no_of_neighbours:
                no_of_neighbours[neighbour] += 1
            else:
                no_of_neighbours[neighbour] = 1
            if neighbour.getColornum() not in list_of_colours:
                list_of_colours.append(neighbour.getColornum())
    classes_to_split = dict()
    for colour in list_of_colours:
        class_with_nodecount = dict()
        for node in colouring[colour]:
            if no_of_neighbours.get(node) is not None:
                count = no_of_neighbours[node]
            else:
                count = 0
            if class_with_nodecount.get(count) is not None:
                class_with_nodecount[count].append(node)
            else:
                class_with_nodecount[count] = [node]
        # print(colour)
        # print(class_with_nodecount)
        if len(class_with_nodecount) > 1:
            classes_to_split[colour] = class_with_nodecount
    return classes_to_split

start = time()
GL, settings = loadgraph("testGraphs\\colorref_smallexample_2_49.grl", FastGraph, True)
GL1, setting = loadgraph("testGraphs\\colorref_smallexample_2_49.grl", FastGraph, True)
# GL, settings = loadgraph("testGraphs\\bigtrees2.grl", FastGraph, True)
# GL1, setting = loadgraph("testGraphs\\bigtrees2.grl", FastGraph, True)
union = disjointunion(GL[0], GL[1])
colored,highestDeg, numberofV = colorref(union, True)
countIsomorphism(numberofV, minimizationpartitioning(colored,highestDeg))
ref, a = colorref(GL1[0])
# print(individualizationref(ref, a, True))
