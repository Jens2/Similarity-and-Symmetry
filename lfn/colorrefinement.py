from graphImplementations.fastgraphs import graph

def colorref(G):
    listofcolourlists = []
    #
    # Create a list which contains the colour number as the index with a list of vertices which all have the specified colour.
    # Also keep track of the highest known number
    highestDeg = - 1
    for v in G.V():
        if highestDeg < v.getColornum:
            highestDeg = v.getColornum
        if listofcolourlists[v.getColornum] is not None:
            listofcolourlists.insert(v.getColornum, listofcolourlists[v.getColornum].append(v))
        else:
            listofcolourlists.insert(v.getColornum, list().append(v))
    i = 0
    # while not done.
    # for de lijst
    for colourlist in listofcolourlists:
        if len(colourlist) > 0:
            u = colourlist[0]
            for v in colourlist:
                if u is not v:
                    if not checkNeighbourhood(u,v):
    #                     verander shit
                        print()
    return -1

def checkNeighbourhood(u, v):
    for node in u.nbs():
        pass
    # TODO