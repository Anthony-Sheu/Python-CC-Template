def bfs():
  q = collections.deque([1])  # change 1 to starting node
  vis = emp(0, n+1)
  while q:
    pos = q.popleft()
    for e in g[pos]:  # adj list
      if not vis[e]:
        q.append(e)
        vis[e] = 1
