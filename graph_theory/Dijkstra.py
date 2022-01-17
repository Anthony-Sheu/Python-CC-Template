def dijkstra_weighted():  # from heapq import *
    dist = emp(mat, n+1)
    //vis = emp(0, n+1)
    dist[1] = 0  # set 1 as your starting node
    q = [[0, 1]]
    heapify(q)
    while q:
        dis, pos = heappop(q)
        //vis[pos] = 1
        for e, w in g[pos]:  # adj list, weighted graph
            //if not vis[e]:
              if dist[pos]+w < dist[e]:
                  heappush(q, [dist[pos]+w, e])
                  dist[e] = dist[pos]+w
    return dist
