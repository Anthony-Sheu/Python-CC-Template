def min_path(x, y):  # returns a list of the minimum path from one node to another, otherwise 0
    q = collections.deque([[x, [x]]])
    vis = emp(0, n+1)
    vis[x] = 1
    while q:
        pos, past = q.popleft()
        if pos == y: return past
        for i in range(len(g[pos])):  # adj matrix
            if not vis[g[pos][i]]: 
              vis[g[pos][i]] = 1
              q.append([g[pos][i], past + [g[pos][i]]])
    return []
