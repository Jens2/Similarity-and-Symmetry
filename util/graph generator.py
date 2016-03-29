from graphIO import *
from graphutil import *

def createcomplete(n):
    g = graph(n)
    V = g.V()
    for i in range(0,n):
        for j in range(i+1,n):
            g.addedge(V[i], V[j])
    return g

def createbipart(n,m):
    g = graph(n+m)
    V = g.V()
    for i in range(n):
        for j in range(n,n+m):
            g.addedge(V[i],V[j])
    return g

def createtripart(n,m,p):
    g = graph(n+m+p)
    V = g.V()
    for i in range(n):
        for j in range(n,n+m+p):
            g.addedge(V[i],V[j])
    for i in range(n,n+m):
        for j in range(n) and range(n+m,n+m+p):
            g.addedge(V[i],V[j])
    return g

def createplanar():
    g = graph(n)

print(createtripart(2,3,2))


print(createbipart(4,4))
print(createcomplete(4))
