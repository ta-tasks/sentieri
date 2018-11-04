import turingarena as ta

import networkx as nx
import random

# the solution submitted by the user, source is the default name
submitted_solution = ta.submission.source

testcases = [
    (16, 15),
    (80, 162),
    (11, 10),
    (20, 19),
    (20, 37),
    (50, 49),
    (50, 99),
    (99, 218),
    (100, 99),
    (100, 203),
]

MAXN = 100
MAXM = 1000

# run the solution
for N, M in testcases:
    graph = nx.random_tree(N)
    while len(graph.edges()) < M:
        graph.add_edges_from(nx.gnm_random_graph(N, M - len(graph.edges())).edges())

    weights = [random.randint(0, 1) for i in range(len(graph.edges()))]

    assert len(graph.nodes()) <= MAXN
    assert len(graph.edges()) <= MAXM
    assert nx.is_connected(graph)

    with ta.run_algorithm("solutions/correct.cpp") as p:
        correct_output = p.functions.shortest_path(
            len(graph.nodes()),
            len(graph.edges()),
            *zip(*graph.edges()),
            weights)

    with ta.run_algorithm(submitted_solution) as p:
        output = p.functions.shortest_path(
            len(graph.nodes()),
            len(graph.edges()),
            *zip(*graph.edges()),
            weights)

    if output == correct_output:
        print("correct! (%d == %d)" % (output, correct_output))
    else:
        print("wrong (%d != %d)" % (output, correct_output))