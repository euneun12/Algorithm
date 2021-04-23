import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappop, heappush
for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    distance = [[99999999999999] * N for _ in range(N)]
    distance[0][0] = 0
    Q = [[0, 0, 0]]
    visit = [[0] * N for _ in range(N)]
    while Q:
        w, u, v = heappop(Q)
        if visit[u][v] == 1:
            continue
        visit[u][v] = 1
        for r, c in ((0, 1), (0,  -1), (1, 0), (-1, 0)):
            nr, nc = r + u, c + v
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if distance[nr][nc] > distance[u][v] + data[nr][nc]:
                distance[nr][nc] = distance[u][v] + data[nr][nc]
                heappush(Q, (distance[nr][nc], nr, nc))
    print('#{} {}'.format(tc, distance[N - 1][N - 1]))