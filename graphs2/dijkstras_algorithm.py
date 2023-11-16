import math
W = ((0, 3, 1, 3, 0, 0),
     (3, 0, 4, 0, 0, 0),
     (1, 4, 0, 0, 7, 5),
     (3, 0, 0, 0, 0, 2),
     (0, 0, 7, 0, 0, 4),
     (0, 0, 5, 2, 4, 0))
start = 0
n = 6
INF = math.inf
visited = [False] * n
dist = [INF] * n
dist[start] = 0
def gofrom():
    index = 0
    distmin = INF
    for i in range(n):
        if dist[i] < distmin and visited[i] == False:
            distmin = dist[i]
            index = i
    return index

while False in visited:
    u = gofrom()
    for v in range(n):
        if W[u][v] != 0 and (not visited[v]):
            dist[v] = min(dist[v], dist[u] + W[u][v])
    visited[u] = True

print(dist)
