from lfn.colorrefinement import checkNeighbourhood


class coloring:

    def __init__(self):
        self.__colors = dict()

    def put(self, color, v):
        v.setColornum(color)
        if self.__colors.get(color) is not None:
            self.__colors[color].append(v)
        else:
            self.__colors[color] = []
            self.__colors[color].append(v)

    def remove(self, v):
        self.__colors[v.getColornum()].remove(v)

    def move(self, v, to):
        self.__colors[v.getColornum()].remove(v)
        self.put(to, v)

    def moveAll(self, vs, to):
        if len(vs) > 0:
            color = vs[0].getColornum()
            for v in vs:
                self.__colors[color].remove(v)
                self.put(to, v)

    def get(self, color):
        return self.__colors[color]

    def getColorClasses(self):
        return [self.__colors.get(key) for key in self.__colors.keys()]

    def colors(self):
        return [c for c in self.__colors.keys() if self.__colors.get(c) is not None and len(self.__colors.get(c)) > 0]

    def deepcopy(self):
        deepcopy = coloring()
        for c in self.colors():
            deepcopy.__colors[c] = self.__colors.get(c)
        return deepcopy

    def k(self):
        k = 0
        for color_class in self.__colors.keys():
            if len(self.__colors.get(color_class)) > 0:
                k += 1
        return k

    def isStable(self):
        for color_class in self.colors():
            v = self.__colors[color_class][0]
            for u in self.__colors[color_class][1:]:
                if not checkNeighbourhood(u, v):
                    return False
        return True

    def isUniform(self):
        return self.k() == 1

    def isDiscrete(self):
        for color_class in self.__colors.keys():
            if len(self.__colors[color_class]) > 1:
                return False
        return True

    def print(self):
        print(self.__colors)

def getColoringByDegree(G):
    alpha = coloring()
    for v in G.V():
        alpha.put(v.getDegree(), v)
    return alpha

def getColoring2(G):
    alpha = coloring()
    highestDegree = -1
    for v in G.V():
        alpha.put(v.getDegree(), v)
        if highestDegree < v.getColornum():
            highestDegree = v.getColornum()
    changed = True
    # De colour refinement:
    while changed:
        changed = False
        for colour_list in alpha.getColorClasses():
            change_list = []
            u = colour_list[0]
            for v in colour_list[1:]:
                if not checkNeighbourhood(u, v):
                    changed = True
                    change_list.append(v)
            alpha.moveAll(change_list, highestDegree + 1)
            if changed:
                highestDegree += 1
    return alpha

def getColoring(G):
    alpha = coloring()
    highestDegree = -1
    for v in G.V():
        alpha.put(v.getDegree(), v)
        if highestDegree < v.getColornum():
            highestDegree = v.getColornum()
    changed = True
    buffer = alpha
    # De colour refinement:
    while changed:
        changed = False
        alpha = buffer.deepcopy()
        for color in alpha.colors():
            colour_list = buffer.get(color)
            if len(colour_list) > 1:
                changelist = []
                u = colour_list[0]
                for v in colour_list[1:]:
                    if not checkNeighbourhood(u, v):
                        changed = True
                        changelist.append(v)
                for v in changelist:
                    buffer.move(v, highestDegree + 1)
                if changed:
                    highestDegree += 1
    return buffer