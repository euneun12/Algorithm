import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def BFS(i, j):
    rec[i][j] = 1
    Q = deque()
    Q.append((i, j))
    count = 1
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and rec[nr][nc] == 0:
                rec[nr][nc] = 1
                Q.append((nr, nc))
                count += 1
    area.append(count)


dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
# M : row, N : column, K : 영역
M, N, K = map(int, input().split())
rec = [[0] * N for _ in range(M)]
# 문제에는 왼쪽 아래가 (0, 0)으로 나와있는데 편의상 상하반전된 형태로 했다. 어차피 영역의 넓이만 알면 되니까
# 직사각형이 그려지는 부분은 1로 저장
for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            rec[i][j] = 1

# 영역의 넓이 저장할 공간
area = []
# 0이면 BFS 실행
for i in range(M):
    for j in range(N):
        if rec[i][j] == 0:
            BFS(i, j)

print(len(area))
area.sort()
print(*area)
