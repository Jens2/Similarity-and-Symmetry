from lfn.coloringmanipulation import *


# def equal_coloring(c1, c2):
#     if len(c1) is not len(c2):
#         return False
#     for color in c1.keys():
#         if len(c2[color]) is not len(c1[color]):
#             return False
#         for index in range(c1[color]):
#             if c1[color][index] is not c2[color][index]:
#                 return False
#     return True
#
#
# def color_refinement(coloring):
#     i = 0
#     new_coloring = dict()
#     while not equal_coloring(coloring, new_coloring):
#         i = i + 1

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
                if len(new_minimal_entry) == 0 or (
                        len(new_minimal_entry) != 0 and len(nodecount[key]) < len(new_minimal_entry)):
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
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if len(lefthalf[i]) < len(righthalf[j]):
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


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


def deepCopyMap(mapc):
    result = dict()
    for key in mapc.keys():
        result[key] = mapc[key]
    return result


def checkNeighbourhood(u, v):
    nodedone = []
    for node in u.nbs():
        done = False
        for neighbour in v.nbs():
            if node.getColornum() == neighbour.getColornum() and neighbour not in nodedone:
                nodedone.append(neighbour)
                done = True
                break
        if not done:
            return False
    return True


def beta_coloring(coloring, highest_degree=-1):
    changed = True
    buffer = coloring
    if highest_degree == -1:
        for key in coloring.keys():
            if key > highest_degree:
                highest_degree = key
    # De colour refinement:
    while changed:

        changed = False
        coloring = deepCopyMap(buffer)

        for key in coloring.keys():
            color_class = buffer[key]

            if len(color_class) > 1:
                u = color_class[0]
                changelist = []
                for v in color_class[1:]:
                    if not checkNeighbourhood(u, v):
                        changed = True
                        color_class.remove(v)
                        changelist.append(v)
                        # Voeg de afwijkende vertices toe aan een nieuwe lijst in de buffer map
                        if buffer.get(highest_degree + 1) is not None:
                            oldList = buffer.get(highest_degree + 1)
                            oldList.append(v)
                            buffer[highest_degree + 1] = oldList
                        else:
                            newList = [v]
                            buffer[highest_degree + 1] = newList
                for v in changelist:
                    v.setColornum(highest_degree + 1)
                if changed:
                    highest_degree += 1
    return buffer


def is_balanced(coloring, number_of_vertices):
    for key in coloring.keys():
        counter = 0
        for v in coloring.get(key):
            if v.getLabel() < number_of_vertices // 2:
                counter += 1
            else:
                counter -= 1
        if counter is not 0:
            return False
    return True


def defines_bijection(coloring):
    for key in coloring.keys():
        if not (len(coloring.get(key)) is 2 or len(coloring.get(key)) is 0):
            return False
    return True


def alpha_coloring(g, d, i):
    coloring = dict()
    for index in range(len(d) + 1):
        coloring[index] = []
    zero_color = []
    zero_color.extend(g.V())
    for D_v in d:
        zero_color.remove(D_v)
    for I_v in i:
        zero_color.remove(I_v)
    for v in zero_color:
        coloring[0].append(v)
        v.setColornum(0)
    for index in range(len(d)):
        coloring[index + 1].append(d[index])
        d[index].setColornum(index + 1)
    for index in range(len(i)):
        coloring[index + 1].append(i[index])
        i[index].setColornum(index + 1)
    return coloring


def count_isomorphism(g, D, I):
    coloring = alpha_coloring(g, D, I)
    highest_degree = -1
    for key in coloring.keys():
        if key > highest_degree:
            highest_degree = key
    # coloring = beta_coloring(coloring, highest_degree)
    coloring = minimizationpartitioning(coloring, highest_degree)

    for key in coloring.keys():
        color_class = coloring[key]
        for vertex in color_class:
            vertex.setColornum(key)

    if not is_balanced(coloring, len(g.V())):
        return 0
    if defines_bijection(coloring):
        return 1
    color_class = None
    for key in coloring.keys():
        if len(coloring.get(key)) >= 4:
            color_class = coloring.get(key)
            break
    x = None
    for node in color_class:
        if node.getLabel() < len(g.V()) // 2:
            x = node
    num = 0
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

        for key in coloring.keys():
            color_class = coloring[key]
            for vertex in color_class:
                vertex.setColornum(key)
        num += count_isomorphism(g, D_x, I_y)
    return num


def isIsomorphism(g, D=[], I=[], iso_found=False):
    coloring = alpha_coloring(g, D, I)
    highest_degree = -1
    for key in coloring.keys():
        if key > highest_degree:
            highest_degree = key
    # coloring = beta_coloring(coloring, highest_degree)
    coloring = minimizationpartitioning(coloring, highest_degree)

    for key in coloring.keys():
        color_class = coloring[key]
        for vertex in color_class:
            vertex.setColornum(key)

    if not is_balanced(coloring, len(g.V())):
        return False
    if defines_bijection(coloring):
        iso_found = True
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
        # for key in coloring.keys():
        #     color_class = coloring[key]
        #     for vertex in color_class:
        #         vertex.setColornum(key)
        # iso_found = iso_found or count_isomorphism(g, D_x, I_y)
        iso_found = isIsomorphism(g, D_x, I_y, iso_found) > 0
        if iso_found:
            return True
    return iso_found


# GL, settings = loadgraph("testGraphs\\torus24.grl", FastGraph, True)
# GL, settings = loadgraph("testGraphs\\products72.grl", FastGraph, True)
GL, settings = loadgraph("testGraphs\\bigtrees1.grl", FastGraph, True)
# GL, settings = loadgraph("testGraphs\\cubes5.grl", FastGraph, True)

graph1 = GL[0]
graph2 = GL[2]

# graph1 = loadgraph("testGraphs\\threepaths5.gr", FastGraph)
# graph2 = loadgraph("testGraphs\\threepaths160.gr", FastGraph)

G = disjointunion(graph1, graph2)

# print(count_isomorphism(G, [], []))

print(isIsomorphism(G))


# def isIsomorphism(numberOfVertices, colourmap):
#     if not isBalanced(colourmap, numberOfVertices):
#         return 0
#     if isBijection(colourmap):
#         return 1
#     num = 0
#     highestDeg = -1
#     for key in colourmap.keys():
#         if key > highestDeg:
#             highestDeg = key
#     for key in colourmap.keys():
#         if len(colourmap.get(key)) >= 4:
#             colorclass = colourmap.get(key)
#             for node in colorclass:
#                 if node.getLabel() < numberOfVertices//2:
#                     x = node
#                     dictionary = deepCopyMap(colourmap)
#
#                     dictionary.get(key).remove(x)
#
#                     x.setColornum(highestDeg + 1)
#
#                     newColourClass = [x]
#                     dictionary[highestDeg + 1] = newColourClass
#
#                     for secondNode in colorclass:
#                         if secondNode.getLabel() >= numberOfVertices//2:
#                             dictionary2 = deepCopyMap(dictionary)
#
#                             dictionary2.get(key).remove(secondNode)
#
#                             secondNode.setColornum(highestDeg + 1)
#
#                             newColourClass.append(secondNode)
#                             dictionary2[highestDeg + 1] = newColourClass
#
#                             dictionary2 = minimizationpartitioning(dictionary2, highestDeg + 1)
#                             if isBijection(dictionary2):
#                                 return 1
#                             else:
#                                 oldColourClass = dictionary2[key]
#                                 oldColourClass.append(secondNode)
#                                 dictionary2[key] = oldColourClass
#                                 secondNode.setColornum(key)
#                                 newColourClass.remove(secondNode)
#                     x.setColornum(key)
#                     oldColourClass1 = dictionary[key]
#                     oldColourClass1.append(x)
#                     dictionary[key] = oldColourClass1
#     return num
