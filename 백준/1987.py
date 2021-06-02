import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

def DFS(r, c, cnt):
    global  max_length
    if max_length < cnt:
        max_length = cnt
    for k in range(4):
        nr = dr[k] + r
        nc = dc[k] + c
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            continue
        if visited[nr][nc] == 0 and board[nr][nc] not in alpha:
            visited[nr][nc] = 1
            alpha.add(board[nr][nc])
            DFS(nr, nc, cnt + 1)
            visited[nr][nc] = 0
            alpha.remove(board[nr][nc])


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
# 알파벳 있는지 없는지 확인할 집합
alpha = set()
alpha.add(board[0][0])
# 방문 표시할거
visited = [[0] * C for _ in range(R)]
# 최대 칸
max_length = 0
DFS(0, 0, 1)
print(max_length)


