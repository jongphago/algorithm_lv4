# [이론] 다익스트라
# 3. 구현
# n: int (정점의 개수)
# graph: list[list[tuple[int, int]]] (인접 리스트, (v, cost) 형식)
# start: int (시작 정점)
def dijkstra(n, graph, start):
    INF = float('inf')
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[start] = 0

    for _ in range(n):
        min_dist = INF
        u = -1
        # 가장 가까운 미방문 정점 u 찾기
        for i in range(1, n + 1):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:  # 더 이상 방문할 정점이 없음
            break
        visited[u] = True
        # u와 연결된 정점의 거리 업데이트
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
    return dist
