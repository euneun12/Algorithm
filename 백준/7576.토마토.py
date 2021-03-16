import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def BFS():
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M  and tomato[nr][nc] == 0:
                tomato[nr][nc] = -1
                Q.append((nr, nc))
                distance[nr][nc] = distance[r][c] + 1
# M : 상자 가로의 칸 수(column), N: 상자 세로의 칸 수(row)
M, N = map(int, input().split())
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1: 토마토 없음
tomato = [list(map(int, input().split())) for _ in range(N)]

distance = [[0] * M for _ in range(N)]

Q = deque()
# 익은 토마토가 여러 개니까 일단 큐에 쌓는다.
# 지난 번에 많이 풀었던 것처럼 1이 있으면 BFS 하는 걸로 하면 최소 일수를 구할 수 없다...
# BFS 이제 잘 풀 수 있다! 했더니 이 문제에서 시간이 오래 걸렸다...그래도 풀고 나니 뿌듯

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append((i, j))
            tomato[i][j] = -1

BFS()

# 안 익은 토마토가 있으면 -1
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            break
    if tomato[i][j] == 0:
        break
# 위에서 브레이크 안 걸렸을 때
else:
    result = max(map(max, distance))
    # 처음부터 다 익었을 때
    if result == 1:
        print(0)
    else:
        print(result)
