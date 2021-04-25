import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for tc in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    cost = [[1000000] * N for _ in range(N)]
    cost[0][0] = 0
    cnt = N
    Q = deque()
    Q.append((0, 0))

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr > N - 1 or nc < 0 or nc > N - 1:
                continue
            temp_cost = 1
            if data[nr][nc] - data[r][c] > 0:
                temp_cost += data[nr][nc] - data[r][c]
            if cost[nr][nc] > cost[r][c] + temp_cost:
                cost[nr][nc] = cost[r][c] + temp_cost
                Q.append((nr, nc))

    print('#{} {}'.format(tc, cost[N-1][N-1]))