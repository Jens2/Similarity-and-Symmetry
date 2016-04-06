from util.graph_generator import *

graph_amount = 40
graph_size = 150

GL_complete = []
GL_bipartite = []
GL_tripartite = []
GL_tree = []
GL_planar = []

complete_path = "complete" + str(graph_size) + ".grl"
bipartite_path = "bipartite" + str(graph_size) + ".grl"
tripartite_path = "tripartite" + str(graph_size) + ".grl"
tree_path = "tree" + str(graph_size) + ".grl"
planar_path = "planar" + str(graph_size) + ".grl"

for i in range(graph_amount):
    GL_complete.append(create_complete(graph_size))
print("Complete done")
for i in range(graph_amount):
    GL_bipartite.append(create_bipartite_random(graph_size//2, graph_size - graph_size//2))
print("Bipartite done")
for i in range(graph_amount):
    GL_tripartite.append(create_tripartite_random(graph_size//3, graph_size//3, graph_size - 2 * (graph_size//3)))
print("Tripartite done")
for i in range(graph_amount):
    GL_tree.append(make_tree(graph_size))
print("Tree done")
for i in range(graph_amount):
    GL_planar.append(create_planar(graph_size))
print("Planar done")


savegraph(GL_complete, complete_path)
savegraph(GL_bipartite, bipartite_path)
savegraph(GL_tripartite, tripartite_path)
savegraph(GL_tree, tree_path)
savegraph(GL_planar, planar_path)



