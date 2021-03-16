from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


# def DFS(i, j):
#     # 일단 방문 표시를 하고
#     visit[i][j] = 1
#     for k in range(4):
#         # 오른쪽, 아래 두 방향에 대해서
#         nr = dr[k] + i
#         nc = dc[k] + j
#         # 인덱스가 벗어나지 않고 방문하지 않은 경우
#         if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
#             # 같은 색상이면 다시 DFS 해주기
#             if draw[i][j] == draw[nr][nc]:
#                 DFS(nr, nc)
#
# # N x N
# N = int(input())
# # 입력받은 그림
# draw = [list(input()) for _ in range(N)]
# # 방문 표시
# visit = [[0] * N for _ in range(N)]
# dr = [0, 0, 1, -1]
# dc = [-1, 1, 0, 0]
# # p1은 적록색약 아닌 사람
# p1 = 0
# for i in range(N):
#     for j in range(N):
#         if visit[i][j] == 0:
#             DFS(i, j)
#             p1 += 1
# # p2는 적록색약인사람, 방문 초기화
# p2 = 0
# visit = [[0] * N for _ in range(N)]
# # R과 G 하나로 통일 ( R이면 G로 바꾸어줌)
# for i in range(N):
#     for j in range(N):
#         if draw[i][j] == 'R':
#             draw[i][j] = 'G'
#
# for i in range(N):
#     for j in range(N):
#         if visit[i][j] == 0:
#             DFS(i, j)
#             p2 += 1
#
# print(p1, p2)

def BFS(i, j):
    Q.append((i, j))
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = dr[k] + r
            nc = dc[k] + c
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and draw[r][c] == draw[nr][nc]:
                visit[nr][nc] = 1
                Q.append((nr, nc))


N = int(input())
draw = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
Q = deque()
# p1은 적록색약 아닌 사람
p1 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            Q = deque()
            visit[i][j] == 1
            BFS(i, j)
            p1 += 1


# p2는 적록색약인사람, 방문 초기화
p2 = 0
visit = [[0] * N for _ in range(N)]
# R과 G 하나로 통일 ( R이면 G로 바꾸어줌)
for i in range(N):
    for j in range(N):
        if draw[i][j] == 'R':
            draw[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            Q = deque()
            visit[i][j] == 1
            BFS(i, j)
            p2 += 1

print(p1, p2)
