import turingarena as ta
import networkx as nx


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

# run the solution
for N, M in testcases:
    graph = nx.random_tree(N)

    with ta.run_algorithm(submitted_solution) as p:
        p.functions.shortest_path(
            3,
            5,
            [1, 2, 3, 0, 2],
            [2, 3, 0, 2, 1],
            [0, 0, 1, 1, 0])

