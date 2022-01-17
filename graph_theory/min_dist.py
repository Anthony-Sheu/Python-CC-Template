def min_dist(a, b):  # returns distance between two points on a non-weighted graph using adj list
    q = collections.deque([a])
    vis = emp(0, n+1)
    dist = emp(0, n+1)
    vis[a] = 1
    while q:
        pos = q.popleft()
        if pos == b: return dist[pos]
        for e in g[pos]:
            if not vis[e]: 
              q.append(e)
              vis[e] = 1
              dist[e] = dist[pos]+1
    return -1
