from final.coloringutil import is_balanced, defines_bijection
from final.coloring import alpha_coloring, minimization_partitioning


def count_isomorphism(g, d=[], i=[]):
    coloring = alpha_coloring(g, d, i)
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
    c_intersect_h = []
    for v in color_class:
        if v.getLabel() >= len(g.V()) // 2:
            c_intersect_h.append(v)
    d_x = []
    d_x.extend(d)
    d_x.append(x)
    for y in c_intersect_h:
        i_y = []
        i_y.extend(i)
        i_y.append(y)
        for key in coloring.keys():
            color_class = coloring[key]
            for vertex in color_class:
                vertex.setColornum(key)
        num += count_isomorphism(g, d_x, i_y)
    return num
