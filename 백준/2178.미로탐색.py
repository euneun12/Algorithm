import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def BFS():
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0 and maze[nr][nc] == '1':
                visit[nr][nc] = 1
                length[nr][nc] = length[r][c] + 1
                Q.append((nr, nc))
            if nr == N - 1 and nc == M - 1:
                return length[nr][nc]


N, M = map(int, input().split())
maze = [input() for _ in range(N)]
visit = [[0] * M for _ in range(N)]
length = [[1] * M for _ in range(N)]
Q = deque()
Q.append((0, 0))
visit[0][0] = 1
print(BFS())