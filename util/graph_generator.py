from util.graphutil import *
import random

def create_complete(n):
    g = graph(n)
    V = g.V()
    for i in range(0, n):
        for j in range(i+1, n):
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
    vertices = g.V()
    if n > 1:
        # Make first edge
        remaining_vertices = []
        remaining_vertices.extend(vertices)
        outer_edges = [g.addedge(vertices[0], vertices[1])]
        remaining_vertices.remove(vertices[0])
        remaining_vertices.remove(vertices[1])
        # Add shapes
        while len(remaining_vertices) > 0:
            # Pick shape to add
            choice = random.choice(range(4))
            if choice == 0:
                # Add line
                v = random.choice(remaining_vertices)
                remaining_vertices.remove(v)
                e = random.choice(outer_edges)
                outer_edges.append(g.addedge(e.tail(), v))
            if choice == 1:
                # Add triangle
                v = random.choice(remaining_vertices)
                remaining_vertices.remove(v)
                e = random.choice(outer_edges)
                new_edge_one = g.addedge(e.tail(), v)
                new_edge_two = g.addedge(e.head(), v)
                outer_edges.remove(e)
                outer_edges.append(new_edge_one)
                outer_edges.append(new_edge_two)
            if choice == 2 and len(remaining_vertices) > 1:
                # Add square
                v1 = random.choice(remaining_vertices)
                remaining_vertices.remove(v1)
                v2 = random.choice(remaining_vertices)
                remaining_vertices.remove(v2)
                e = random.choice(outer_edges)
                new_edge_one = g.addedge(e.tail(), v1)
                new_edge_two = g.addedge(e.head(), v2)
                new_edge_three = g.addedge(v1, v2)
                outer_edges.remove(e)
                outer_edges.append(new_edge_one)
                outer_edges.append(new_edge_two)
                outer_edges.append(new_edge_three)
            if choice == 3 and len(remaining_vertices) > 2:
                # Add pentagon
                v1 = random.choice(remaining_vertices)
                remaining_vertices.remove(v1)
                v2 = random.choice(remaining_vertices)
                remaining_vertices.remove(v2)
                v3 = random.choice(remaining_vertices)
                remaining_vertices.remove(v3)
                e = random.choice(outer_edges)
                new_edge_one = g.addedge(e.tail(), v1)
                new_edge_two = g.addedge(e.head(), v3)
                new_edge_three = g.addedge(v1, v2)
                new_edge_four = g.addedge(v2, v3)
                outer_edges.remove(e)
                outer_edges.append(new_edge_one)
                outer_edges.append(new_edge_two)
                outer_edges.append(new_edge_three)
                outer_edges.append(new_edge_four)
    return g



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
