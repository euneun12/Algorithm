import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS():
    while Q:
        r, c, k = Q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][k]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1 < nr < N and -1 < nc < M:
                if wall[nr][nc] == 0 and visited[nr][nc][k] == 0:
                    visited[nr][nc][k] = visited[r][c][k] + 1
                    Q.append((nr, nc, k))
                # 벽 부술 수 있는 경우!
                elif wall[nr][nc] == 1 and k == 0:
                    visited[nr][nc][1] = visited[r][c][k] + 1
                    Q.append((nr, nc, 1))
    return -1


N, M = map(int, input().split())
wall = [list(map(int, input())) for _ in range(N)]
# 벽 부수고 이동할 때와 아닐 때 나눠야해서 3차원 리스트 사용!
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
Q = deque()
Q.append((0, 0, 0))
visited[0][0][0] = 1
print(BFS())
