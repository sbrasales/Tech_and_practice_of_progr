def kruskal_algorithm(edges, n):
    edges.sort(key=lambda x: x[0])  # Ordena las aristas por peso

    D = list(range(n))
    result = []

    for edge in edges:
        a, b = edge[1], edge[2]
        temp = D[a]
        if D[a] != D[b]:
            result.append((edge[0], a, b))
            for i in range(n):
                if D[i] == temp:
                    D[i] = D[b]

    return result
