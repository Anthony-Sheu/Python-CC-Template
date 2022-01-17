def cyclic():  # call this function to check for a cycle within a directed graph (returns 1 for cycle found)
    vis = emp(0, n+1)
    res = emp(0, n+1)
    for i in range(n):
        if not vis[i] and dfscycle(i, vis, res):
            return 1
    return 0

def dfscycle(x, vis, res):
    vis[x] = 1
    res[x] = 1
    for e in g[x]:
        if not vis[e] and dfscycle(e, vis, res):
            return 1
        elif res[e]: return 1
    res[x] = 0
    return 0
