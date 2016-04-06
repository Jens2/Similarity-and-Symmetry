from final.coloringutil import is_balanced, defines_bijection
from final.coloring import alpha_coloring, minimization_partitioning


def isIsomorphism(g, D=[], I=[], iso_found=False):
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
        iso_found = isIsomorphism(g, D_x, I_y, iso_found) > 0
        if iso_found:
            return True
    return iso_found

