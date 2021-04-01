from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS(i, j):
    global count
    # Q 만들고 (i, j) 넣기
    Q = deque()
    Q.append((i, j))
    # 방문표시 할 거 만들고 (i, j) 방문표시하기
    visited = [[0] * W for _ in range(H)]
    visited[i][j] = 1
    while Q:
        r, c = Q.popleft()
        # 네 방향 검사
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 인덱스 검사
            if nr < 0 or nr >= H or nc < 0 or nc >= W or visited[nr][nc] == 1:
                continue
            if cheeze[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append((nr, nc))
            elif cheeze[nr][nc] == 1:
                cheeze[nr][nc] = 0
                count += 1
                visited[nr][nc] = 1
    return count


H, W = map(int, input().split())
# 0은 공기, 1은 치즈
cnt = []
cheeze = [list(map(int, input().split())) for _ in range(H)]
while True:
    count = 0
    if BFS(0, 0):
        cnt.append(count)
    else:
        break

print(len(cnt))
print(cnt[-1])