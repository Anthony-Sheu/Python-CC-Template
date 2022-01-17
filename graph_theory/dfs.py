dist = emp(0, n+1)
def dfs(x, y):  # x is position and y is distance, start with y = 1
    dist[x] += y
    for e in g[x]:
        if not dist[e]: dfs(e, y+1)
