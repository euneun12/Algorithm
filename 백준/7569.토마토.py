import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

def BFS():
    global result
    while Q:
        h, r, c = Q.popleft()
        for k in range(6):
            nr = r + dr[k]
            nc = c + dc[k]
            nh = h + dh[k]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M  and tomato[nh][nr][nc] == 0:
                tomato[nh][nr][nc] = -1
                Q.append((nh, nr, nc))
                distance[nh][nr][nc] = distance[h][r][c] + 1
                if distance[nh][nr][nc] > result:
                    result = distance[nh][nr][nc]

# M : 상자 가로의 칸 수(column), N: 상자 세로의 칸 수(row), H: 상자의 높이
M, N, H = map(int, input().split())
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1: 토마토 없음
tomato = [[list(map(int, input().split())) for _ in range(N)] for h in range(H)]
distance = [[[0] * M for _ in range(N)] for h in range(H)]
Q = deque()
result = 0

for m in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[m][i][j] == 1:
                Q.append((m, i, j))
                tomato[m][i][j] = -1

BFS()

# 안 익은 토마토가 있으면 -1
def miss():
    for m in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[m][i][j] == 0:
                    print(-1)
                    return 1


check = miss()
if not check:
    print(result)
