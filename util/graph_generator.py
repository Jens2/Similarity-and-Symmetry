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
