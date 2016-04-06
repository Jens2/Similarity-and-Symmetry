

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


def minimization_partitioning(coloring, highest_degree):
    w = [pick_smallest_splitter(coloring)]
    if None in w:
        w = []
    while len(w) > 0:
        a = w.pop()
        classes_to_split = count_and_sort_neighbours(coloring, a)
        for colour_class in classes_to_split.keys():
            w_contains = False
            first = True
            new_minimal_entry = []
            node_count = classes_to_split[colour_class]
            if coloring[colour_class] in w:
                w.remove(coloring[colour_class])
                w_contains = True
            for key in node_count.keys():
                if len(new_minimal_entry) == 0 or (
                        len(new_minimal_entry) != 0 and len(node_count[key]) < len(new_minimal_entry)):
                    new_minimal_entry = node_count[key]
                if not first:
                    highest_degree += 1
                    coloring[highest_degree] = node_count[key]
                    if w_contains:
                        w.append(node_count[key])
                    for node in node_count[key]:
                        coloring[colour_class].remove(node)
                else:
                    if w_contains:
                        w.append(node_count[key])
                    first = False
            if not w_contains:
                w.append(new_minimal_entry)
    return coloring


def pick_smallest_splitter(colouring_map):
    list_of_p = []
    for colour_class in colouring_map.values():
        list_of_p.append(colour_class)
    merge_sort(list_of_p)
    for i in range(len(list_of_p) - 1):
        if len(count_and_sort_neighbours(colouring_map, list_of_p[i])) > 0:
            return list_of_p[i]


def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if len(left_half[i]) < len(right_half[j]):
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1


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
        class_with_node_count = dict()
        for node in colouring[colour]:
            if no_of_neighbours.get(node) is not None:
                count = no_of_neighbours[node]
            else:
                count = 0
            if class_with_node_count.get(count) is not None:
                class_with_node_count[count].append(node)
            else:
                class_with_node_count[count] = [node]
        if len(class_with_node_count) > 1:
            classes_to_split[colour] = class_with_node_count
    return classes_to_split

