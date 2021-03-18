import sys
sys.stdin = open('input.txt', 'r')

def BFS(r, c):
    global cnt
    Q.append((r, c))
    apart[r][c] = 0
    while Q:
        x, y = Q.pop(0)
        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0 <= nr < N and 0 <= nc < N and apart[nr][nc] == 1:
                apart[nr][nc] = 0
                cnt += 1
                Q.append((nr, nc))
    return cnt


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
apart = [list(map(int, input())) for _ in range(N)]
Q = []
count = []
for i in range(N):
    for j in range(N):
        if apart[i][j] == 1:
            cnt = 1
            count.append(BFS(i, j))
count.sort()
print(len(count))
for m in range(len(count)):
    print(count[m])