import sys
sys.stdin = open('input.txt', 'r')

def DFS(s):
    for v in G[s]:
        if visited[v] == 0:
            visited[v] = 1
            dfs.append(v)
            DFS(v)


def BFS(s):
    while Q:
        v = Q.pop(0)
        for u in G[v]:
            if visited[u] == 0:
                visited[u] = 1
                Q.append(u)
                bfs.append(u)

N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
# 간선 정보 저장
for i in range(M):
    u, v = map(int, input().split())
    G[u].append((v))
    G[v].append((u))
# 정점 여러개면 작은 번호부터 방문하니까 정렬해주기
for j in G:
    j.sort()

# 먼저 DFS
dfs = []
visited = [0] * (N + 1)
visited[V] = 1
dfs.append(V)
DFS(V)
print(*dfs)

# BFS
bfs = []
visited = [0] * (N + 1)
visited[V] = 1
bfs.append(V)
Q = [V]
BFS(V)
print(*bfs)