import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def BFS():
    global result
    temp = 0
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] == 1 or treasure[nr][nc] == 'W':
                continue
            Q.append((nr, nc))
            visited[nr][nc] = 1
            time[nr][nc] = time[r][c] + 1
            temp = max(temp, time[nr][nc])
    return temp


N, M = map(int, input().split())
treasure = [input() for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            time = [[0] * M for _ in range(N)]
            Q = deque()
            Q.append((i, j))
            visited[i][j] = 1
            result = max(result, BFS())
print(result)