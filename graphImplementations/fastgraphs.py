from graphImplementations.basicgraphs import vertex, graph, GraphError, edge


class FastVertex(vertex):
    def __init__(self, graph, label=0):
        self._graph = graph
        self._label = label
        self._inclist = []

        self._colornum = 1

    def getLabel(self):
        return self._label

    def setLabel(self, n):
        self._label = n

    def setGraph(self, G):
        self._graph = G

    def inclist(self):
        return self._inclist

    def addToInclist(self, edge):
        self._inclist.append(edge)

    def getDegree(self):
        return len(self.inclist())

    def setColornum(self, num):
        self._colornum = num

    def updateColornumByOne(self):
        self._colornum += 1

    def getColornum(self):
        return self._colornum

class FastGraph(graph):

    def addObjVertex(self, node):
        self._V.append(node)

    def addvertex(self, label=-1):
        """
        Add a vertex to the graph.
        Optional argument: a vertex label (arbitrary)
        """
        if label == -1:
            label = self._nextlabel
            self._nextlabel += 1
        u = FastVertex(self, label)
        self._V.append(u)
        return u

    def addedge(self, tail, head):
        """
		Add an edge to the graph between <tail> and <head>.
		Includes some checks in case the graph should stay simple.
		"""
        if self._simple:
            if tail == head:
                raise GraphError('No loops allowed in simple graphs')
            for e in self._E:
                if (e._tail == tail and e._head == head):
                    raise GraphError(
                        'No multiedges allowed in simple graphs')
                if not self._directed:
                    if (e._tail == head and e._head == tail):
                        raise GraphError(
                            'No multiedges allowed in simple graphs')
        if not (tail._graph == self and head._graph == self):
            raise GraphError(
                'Edges of a graph G must be between vertices of G')
        e = edge(tail, head)
        # ////
        tail.addToInclist(e)
        head.addToInclist(e)
        # \\\\
        tail.updateColornumByOne()
        head.updateColornumByOne()
        # ////
        self._E.append(e)
        return e

    def adj(self, u, v):
        """
        Returns True iff vertices <u> and <v> are adjacent.
        """
        for tupel in v.inclist():
            if tupel.head() == u or tupel.tail() == u:
                return True
        return False