from util.graphutil import *
import random


def create_complete(n):
    g = graph(n)
    V = g.V()
    for i in range(0, n):
        for j in range(i + 1, n):
            g.addedge(V[i], V[j])
    return g


def create_bipartite_complete(n, m):
    g = graph(n + m)
    V = g.V()
    for i in range(n):
        for j in range(n, n + m):
            g.addedge(V[i], V[j])
    return g


def create_bipartite_random(n, m):
    g = graph(n + m)
    V = g.V()
    for i in range(n):
        for j in range(n, n + m):
            if bool(random.getrandbits(1)):
                g.addedge(V[i], V[j])
    return g


def create_tripartite_complete(n, m, p):
    g = graph(n + m + p)
    V = g.V()
    for i in range(n):
        for j in range(n, n + m + p):
            g.addedge(V[i], V[j])
    for i in range(n, n + m):
        for j in range(n) and range(n + m, n + m + p):
            g.addedge(V[i], V[j])
    return g


def create_tripartite_random(n, m, p):
    g = graph(n + m + p)
    V = g.V()
    for i in range(n):
        for j in range(n, n + m + p):
            if bool(random.getrandbits(1)):
                g.addedge(V[i], V[j])
    for i in range(n, n + m):
        for j in range(n) and range(n + m, n + m + p):
            if bool(random.getrandbits(1)):
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


def make_tree(n):
    g = graph(n)
    if n > 2:
        connect_recursive(g, g.V()[0], g.V()[1:])
    elif n is 2:
        g.addedge(g.V()[0], g.V()[1])
    return g


def connect_recursive(g, root, nodes):
    if len(nodes) > 0:
        index = random.choice(range(len(nodes)))
        left = [v for v in nodes[index:]]
        right = [v for v in nodes[:index]]
        if len(left) is not 0:
            left_root = random.choice(left)
            g.addedge(root, left_root)
            new_left = [v for v in left if v is not left_root]
            connect_recursive(g, left_root, new_left)
        if len(right) is not 0:
            right_root = random.choice(right)
            g.addedge(root, right_root)
            new_right = [v for v in right if v is not right_root]
            connect_recursive(g, right_root, new_right)


# def make_non_binary_tree(n):
#     g = graph(n)
#     if n > 2:
#         new_roots = pick_roots(g.V()[1:])
#         connect_recursive_not_binary(g, g.V()[0], g.V()[1:])
#     elif n is 2:
#         g.addedge(g.V()[0], g.V()[1])
#     return g


# def connect_recursive_not_binary(g, root, new_roots, free_nodes):
#     for v in new_roots:
#         g.addedge(root, v)
#     new_new_roots = pick_roots(free_nodes)
#     for v in new_new_roots:
#         free_nodes.remove(v)
#     for v in new_roots:
#         connect_recursive_not_binary(g, v, new_new_roots, [u for u in free_nodes[]])

# def connect_recursive_not_binary(g, root, nodes):
#     new_roots = pick_roots(nodes)
#     for v in new_roots:
#         g.addedge(v, root)
#         nodes.remove(v)
#     partitions = chunkIt(nodes, len(new_roots))
#     for i in range(len(new_roots)):
#         connect_recursive_not_binary(g, new_roots[i], partitions[i])
#
#
# def pick_roots(nodes):
#     roots = []
#     if len(nodes) > 0:
#         split = 0
#         if len(nodes) > 1:
#             split = random.choice(range(1, len(nodes)))
#         picked = 0
#         while picked < split:
#             root = random.choice(nodes)
#             if root not in roots:
#                 picked += 1
#                 roots.append(root)
#     return roots
#
# def chunkIt(seq, num):
#     if num == 0:
#         return seq
#     avg = len(seq) / float(num)
#     out = []
#     last = 0.0
#
#     while last < len(seq):
#         out.append(seq[int(last):int(last + avg)])
#         last += avg
#     return out


def create_tree(n):
    g = graph(n)
    V = g.V()
    E = g.E()
    G1 = []
    G2 = []
    G3 = []
    root = random.choice(list(V))
    print(root)
    split1 = random.choice(list(range(1, n - 1)))
    split2 = random.choice(list(range(split1 + 1, n)))
    if V[split1] == root:
        split1 = split1 + 1
    if V[split2] == root or V[split2] == V[split1]:
        split2 = split2 - 1
    print(split1)
    print(split2)
    for i in range(0, split1):
        if V[i] != root:
            G1.append(V[i])
    for i in range(split1, split2):
        if V[i] != root:
            G2.append(V[i])
    for i in range(split2, n):
        if V[i] != root:
            G3.append(V[i])
    g.addedge(root, random.choice(G1))
    g.addedge(root, random.choice(G2))
    g.addedge(root, random.choice(G3))
    print(G1)
    print(G2)
    print(G3)
    return g


# print(create_tree(9))

G = make_tree(30)

print(G)
writeDOT(G, "TestingPlease.dot", False)
