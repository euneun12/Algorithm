import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range((V + 1))]
    for i in range(E):
        # 유항
        u, v, w = map(int, input().split())
        G[u].append((v, w))

    distance = [1000000000000] * (V + 1)
    distance[0] = 0
    visited = [0] * (V + 1)
    cnt = V
    # 모든 노드에 대해서
    while cnt:
        # 최소 가중치 가진 것 찾기
        u, mini = 0, 1000000000000
        for k in range(V + 1):
            if not visited[k] and distance[k] < mini:
                u, mini = k, distance[k]
        # 선택해주고
        visited[u] = 1
        # 인접 노드에 대해서
        for v, w in G[u]:
            # 아직 방문 안하고 그 노드에 현재 저장되어 있는 거리보다 지금 노드에서 그 노드로 이동할 때 거리가 더 작으면
            if not visited[v] and distance[v] > distance[u] + w:
                # 인접 노드의 거리 갱신
                distance[v] = distance[u] + w
        cnt -= 1

    print('#{} {}'.format(tc, distance[V]))