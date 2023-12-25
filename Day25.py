import networkx as nx

G = nx.Graph()

with open("day_25_input.txt") as input_file:
    for line in input_file:
        source, right = line.split(": ")
        for edge in right.strip().split(" "):
            G.add_edge(source, edge)

a = nx.minimum_edge_cut(G)
print(f"Minimum number of edges to cut is {len(a)} edges: {a} ")

G.remove_edges_from(nx.minimum_edge_cut(G))

c = [i for i in nx.connected_components(G)]
answer = len(c[0]) * len(c[1])
print(f"After removing edges, number of separated groups: {len(c)}")
print(f"Length of group 1: {len(c[0])}\nLength of group 2: {len(c[1])}")
print(f"Multiplying both: {answer}")