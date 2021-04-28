import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

# V는 노드 개수, E는 간선의 개수
V, E = map(int, input().split())
# 출발점
s = int(input())
G = [[] for _ in range(V + 1)]
# 각각 정보 저장
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

# 거리 정보 저장
D = [9999999] * (V + 1)
# 출발점은 0으로
D[s] = 0
Q = [[0, s]]
# 단방향이라 visited 안 써도 괜찮다...
while Q:
    # 꺼내와서
    w, v = heappop(Q)
    # 만약 그 지점의 값보다 가중치가 더 크면 그냥 건너뛰기
    if w > D[v]:
        continue
    # 다음 노드들에 대해서
    for u, d in G[v]:
        # 다음 노드에 저장된 값보다 지금 노드에서 가중치를 더해서 다음 노드로 가는게 더 작으면
        if D[u] > D[v] + d:
            # 다음 노드에 현재 노드를 거쳐 가는 값 저장
            D[u] = D[v] + d
            # 다음 노드에 넣어주기
            heappush(Q, [D[u], u])

for j in range(1, V + 1):
    print('{}'.format('INF' if D[j] == 9999999 else D[j]))