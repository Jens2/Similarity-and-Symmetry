

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


def deep_copy_coloring(coloring):
    result = dict()
    for key in coloring.keys():
        result[key] = coloring[key]
    return result

