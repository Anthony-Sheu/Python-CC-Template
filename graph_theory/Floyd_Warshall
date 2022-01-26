    # Thanks to Tommy Shan
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[k][j] and j != i and dist[i][k] and i != k:
                    if not dist[i][j]: dist[i][j] = max(dist[i][k], dist[k][j])
                    else: dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))
