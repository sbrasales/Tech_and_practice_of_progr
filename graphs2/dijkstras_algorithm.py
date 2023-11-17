import math
W = ((math.inf, 3, 1, 3, math.inf, math.inf),
     (3, math.inf, 4, math.inf, math.inf, math.inf),
     (1, 4, math.inf, math.inf, 7, 5),
     (3, math.inf, math.inf, math.inf, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, math.inf, 4),
     (math.inf, math.inf, 5, 2, 4, math.inf))
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

