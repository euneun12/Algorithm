import sys
sys.stdin = open('input.txt', 'r')


def DFS(v):
    visit[v] = 1  # v를 방문 체크 해주고
    for w in G[v]:  # v와 인접한 노드 중 방문하지 않은 노드에 대해서 DFS 실시
        if not visit[w]:
            DFS(w)

# V: 노드의 개수, E: 간선의 개수
V = int(input())
E = int(input())
# G: 간선 정보
G = [[] for _ in range(V + 1)]
for e in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# visit: 방문 체크
visit = [0] * (V + 1)

DFS(1)
print(visit.count(1) - 1)

# 다른 방법
# V = int(input())
# E = int(input())
# G = [[] for _ in range(V + 1)]
# S = []
# for e in range(E):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)
# # visit: 방문 체크
# visit = [0] * (V + 1)
# v = 1
# S.append(v)
# visit[v] = 1
# while S:
#     for w in G[v]:
#         if not visit[w]:
#             S.append(v)
#             visit[w] = 1
#             v = w
#             break
#     else:
#         v = S.pop()
#
# print(visit.count(1) - 1)
