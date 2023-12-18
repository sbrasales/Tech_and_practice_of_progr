# prim_algorithm.py

def prim_algorithm(graph):
    N = len(graph)
    selected_node = [False] * N
    selected_node[0] = True
    INF = 9999
    no_edge = 0
    result_edges = []

    while no_edge < N - 1:
        minimum = INF
        a = 0
        b = 0

        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if not selected_node[n] and graph[m][n]:
                        if minimum > graph[m][n]:
                            minimum = graph[m][n]
                            a = m
                            b = n

        result_edges.append((a, b))
        selected_node[b] = True
        no_edge += 1

    return result_edges
