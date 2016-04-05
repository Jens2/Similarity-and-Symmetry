from lfn.colorrefinement import *
from lfn.coloringmanipulation import *

def individualizationref(dict, numberOfVertices, count=False):
    # arrays = dict.values()
    # result = []
    # for array in arrays:
    #     for element in array:
    #         result.append(element)
    # length = len(result)
    # D = []
    # I = []
    # for key in dict.keys():
    #     vertices = dict.get(key)
    #     for vertex in vertices:
    #         if vertex.getLabel() < length//2:
    #             D.append(vertex)
    #         else:
    #             I.append(vertex)
    # print(D)
    # print(I)
    # return D, I
    if count:
        print(countIsomorphism(numberOfVertices, dict))
    else:
        print(isIsomorphism(numberOfVertices, dict))

def isIsomorphism(numberOfVertices, colourmap):
    if not isBalanced(colourmap, numberOfVertices):
        return 0
    if isBijection(colourmap):
        return 1
    num = 0
    highestDeg = -1
    for key in colourmap.keys():
        if key > highestDeg:
            highestDeg = key
    for key in colourmap.keys():
        if len(colourmap.get(key)) >= 4:
            colorclass = colourmap.get(key)
            for node in colorclass:
                if node.getLabel() < numberOfVertices//2:
                    x = node
                    dictionary = deepCopyMap(colourmap)

                    dictionary.get(key).remove(x)

                    x.setColornum(highestDeg + 1)

                    newColourClass = [x]
                    dictionary[highestDeg + 1] = newColourClass

                    for secondNode in colorclass:
                        if secondNode.getLabel() >= numberOfVertices//2:
                            dictionary2 = deepCopyMap(dictionary)

                            dictionary2.get(key).remove(secondNode)

                            secondNode.setColornum(highestDeg + 1)

                            newColourClass.append(secondNode)
                            dictionary2[highestDeg + 1] = newColourClass

                            dictionary2 = minimizationpartitioning(dictionary2, highestDeg + 1)
                            if isBijection(dictionary2):
                                return 1
                            else:
                                oldColourClass = dictionary2[key]
                                oldColourClass.append(secondNode)
                                dictionary2[key] = oldColourClass
                                secondNode.setColornum(key)
                                newColourClass.remove(secondNode)
                    x.setColornum(key)
                    oldColourClass1 = dictionary[key]
                    oldColourClass1.append(x)
                    dictionary[key] = oldColourClass1
    return num

def isBalanced(dict, numberOfVertices):
    counter = 0
    for key in dict.keys():
        for vertex in dict.get(key):
            if vertex.getLabel() < numberOfVertices//2:
                counter+=1
            else:
                counter-=1
    return counter == 0


def isBijection(dict):
    for key in dict.keys():
        if len(dict.get(key)) != 2:
            return False
    return True


# # GL, options = loadgraph('testGraphs\\colorref_smallexample_4_16.grl', FastGraph, True)
# start = time()
# graph1 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
# graph2 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
# graph11 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
# graph22 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
# startUnion = time()
# print("Done loading: " + str(startUnion - start))
# # savegraph(create_complete(640), 'testGraphs\\bigComplete640.gr')
# # GL, options = loadgraph('testGraphs\\colorref_smallexample_4_16.grl', FastGraph, True)
# startUnion = time()
# graphUnion2 = disjointunion(graph11, graph22)
# print(graphUnion2)
# endUnion = time()
# print("******************************")
# print("Time for disjointunion normal: " + str(endUnion - startUnion))
# print("******************************")
# startComplement = time()
#
# graphComplement = complement(graph1)
# graphComplement2 = complement(graph2)
# graphUnion = disjointunion(graphComplement, graphComplement2)
#
# endUnion = time()
# print("******************************")
# print("Time for complement: " + str(endUnion - startComplement))
# print("******************************")
# startColour = time()
# dicti, numberOfVertices = colorref(graphUnion2)
# print(dicti)
# individualizationref(dicti, numberOfVertices)
# end = time()
# # endColour = time()
# print()
# print("******************************")
# print("Colouring complete graph: " + str(end - startColour) + " sec")
# # start = time()
# # individualizationref(dict, numberOfVertices)
# start = time()
# dicti, numberOfVertices = colorref(graphUnion)
# individualizationref(dicti, numberOfVertices)
# # colour, numberOfVertices = get_coloring(graph2)
# # individualizationref(colour, numberOfVertices, True)
# end = time()
# print("******************************")
# print("Colouring complement graph: " + str(end - start))
# print(dict)
# print(colour)

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


def minimizationpartitioning(colouringmap, highestDeg = -1):

    if highestDeg == -1:
        for key in colouringmap.keys():
            if key > highestDeg:
                highestDeg = key

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

def countIsomorphism(dictionary, highestDeg, numberOfVertices):
    dict = minimizationpartitioning(dictionary, highestDeg)

    if not isBalanced(dict, numberOfVertices):
        return 0
    if isBijection(dict):
        return 1
    colorclass = None
    for key in dict.keys():
        if len(dict.get(key)) >= 4:
            colorclass = dict.get(key)
            break
    x = 0
    for element in colorclass:
        x = element
        break
    num = 0
    for y in colorclass:
        dDict = deepcopy(dict)
        newColourClass = [x, y]
        dDict[highestDeg + 1] = newColourClass
        highestDeg += 1
        num += countIsomorphism(dDict, highestDeg)
    return num



def pick_smallest_splitter(colouringmap):
    list_of_P = []
    for colour_class in colouringmap.values():
        list_of_P.append(colour_class)
    heapSort(list_of_P)
    for i in range(len(list_of_P) - 1):
        if len(count_and_sort_neighbours(colouringmap, list_of_P[i])) > 0:
            return list_of_P[i]

def heapSort(E):
    buildHeap(E)
    heapsize = len(E)
    for i in range(len(E)-1,0,-1):
        E[0],E[i]=E[i],E[0]
        heapsize -= 1
        heapify(E,0, heapsize)

def buildHeap(E):
    heapSize = len(E)
    lastparent=(len(E)-2)//2
    for i in range(lastparent,-1,-1):
        heapify(E,i, heapSize)

def heapify(E,i, heapsize):
    left,right=2*i+1,2*i+2
    if left < heapsize and len(E[left])>len(E[i]):
        max=left
    else:
        max=i
    if right < heapsize and len(E[right])>len(E[max]):
        max=right
    if max!=i:
        E[i],E[max]=E[max],E[i]
        heapify(E,max, heapsize)

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
#
# start = time()
# # GL, settings = loadgraph("testGraphs\\colorref_smallexample_2_49.grl", FastGraph, True)
# # GL1, setting = loadgraph("testGraphs\\colorref_smallexample_2_49.grl", FastGraph, True)
# # GL, settings = loadgraph("testGraphs\\bigtrees2.grl", FastGraph, True)
# # GL1, setting = loadgraph("testGraphs\\bigtrees2.grl", FastGraph, True)
# graph1 = loadgraph("testGraphs\\threepaths2560.gr", FastGraph)
# graph2 = loadgraph("testGraphs\\threepaths2560.gr", FastGraph)
# # graph3 = loadgraph("testGraphs\\threepaths320.gr", FastGraph)
# # graph4 = loadgraph("testGraphs\\threepaths320.gr", FastGraph)
# print("Done loading: " + str(time() - start))
# # union2 = disjointunion(graph3, graph4)
# start = time()
# union = disjointunion(graph1, graph2)
# print("Disjoint union: " + str(time() - start))
# start = time()
# colored, highestDeg, numberofV = colorref(union, True)
# print("Ref: " + str(time() - start))
# start = time()
# individualizationref(colored, numberofV)
# # print("First ref: " + str(time() - start))
# # start = time()
# # print(countIsomorphism(numberofV, minimizationpartitioning(colored,highestDeg)))
# print("Time for partitioning etc.: " + str(time() - start))
# # start = time()
# # ref, a = colorref(union2)
# # individualizationref(ref, a, True)
# # print("Time: " + str(time() - start))

graph3 = loadgraph("testGraphs\\threepaths320.gr", FastGraph)
map, high, number = colorref(graph3, True)
print(countIsomorphism(map, high, number))