# 문제 2 간결 예시: 우선순위 큐 다익스트라 + parent 경로 복원
import heapq

INF = int(1e9)


def dijkstra(n, graph, start):
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
s, e = map(int, input().split())
dist, parent = dijkstra(n, graph, s)
print(dist[e])
path = []
x = e
while x != -1:
    path.append(x)
    x = parent[x]
path.reverse()
print(len(path))
print(*path)
