from util.graphutil import *
import random

def create_complete(n):
    g = graph(n)
    V = g.V()
    for i in range(0,n):
        for j in range(i+1,n):
            g.addedge(V[i], V[j])
    return g


def create_bipartite_complete(n, m):
    g = graph(n+m)
    V = g.V()
    for i in range(n):
        for j in range(n, n+m):
            g.addedge(V[i], V[j])
    return g


def create_bipartite_random(n, m):
    g = graph(n+m)
    V = g.V()
    for i in range(n):
        for j in range(n, n+m):
            if random.choice:
               g.addedge(V[i], V[j])
    return g


def create_tripartite_complete(n, m, p):
    g = graph(n+m+p)
    V = g.V()
    for i in range(n):
        for j in range(n, n+m+p):
            g.addedge(V[i], V[j])
    for i in range(n, n+m):
        for j in range(n) and range(n+m, n+m+p):
            g.addedge(V[i], V[j])
    return g


def create_tripartite_random(n, m, p):
    g = graph(n+m+p)
    V = g.V()
    for i in range(n):
        for j in range(n, n+m+p):
            if random.choice:
                g.addedge(V[i], V[j])
    for i in range(n, n+m):
        for j in range(n) and range(n+m, n+m+p):
            if random.choice:
                g.addedge(V[i], V[j])
    return g


def create_planar(n):
    g = graph(n)
#
#
# print(create_tripartite_random(2, 3, 2))
#
#
# print(create_bipartite_complete(4, 4))
# print(create_complete(4))

def create_tree(n):
    g = graph(n)
    V = g.V()
    E = g.E()
    G1 = []
    G2 = []
    G3 = []
    root = random.choice(list(V))
    print(root)
    split1 = random.choice(list(range(1,n-1)))
    split2 = random.choice(list(range(split1+1,n)))
    if V[split1] == root:
        split1 = split1 + 1
    if V[split2] == root or V[split2] == V[split1]:
        split2 = split2 - 1
    print(split1)
    print(split2)
    for i in range(0,split1):
        if V[i] != root:
            G1.append(V[i])
    for i in range(split1,split2):
        if V[i] != root:
            G2.append(V[i])
    for i in range(split2,n):
        if V[i] != root:
            G3.append(V[i])
    g.addedge(root,random.choice(G1))
    g.addedge(root,random.choice(G2))
    g.addedge(root,random.choice(G3))
    print(G1)
    print(G2)
    print(G3)
    return g

print(create_tree(9))