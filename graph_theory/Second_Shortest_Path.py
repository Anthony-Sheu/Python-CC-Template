def dijkstra(x, ind):
    q = [[0, x]]  # distance, node
    heapify(q)
    dist[ind][x] = 0
    while q:
        dis, pos = heappop(q)
        for e, w in g[ind][pos]:
            if dis+w < dist[ind][e]:
                dist[ind][e] = dis+w
                heappush(q, [dis+w, e])

n, m = gi()
g = [[[] for i in range(n+1)] for i in range(2)]
dist = [emp(mat, n+1) for i in range(2)]
for i in range(m):
    a, b, c = gi()
    g[0][a].append([b, c])
    g[1][b].append([a, c])
dijkstra(1, 0)
dijkstra(n, 1)
ans = mat
for i in range(1, n+1):
    for a, b in g[0][i]:
        total = dist[0][i]+b+dist[1][a]
        if total > dist[0][n]:
            ans = min(ans, total)
printf(ans if ans != mat else -1)

# https://dmoj.ca/problem/cco12p2
