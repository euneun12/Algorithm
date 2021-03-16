import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(i, j):
    # 방문 표시 대신 배추위치의 값을 -1로 바꿨다.
    farm[i][j] = -1
    # 큐 생성하고 i, j 좌표 넣어주기
    Q = deque()
    Q.append((i, j))
    # Q가 빌 때까지
    while Q:
        # 맨 앞 좌표 꺼내와서
        r, c = Q.popleft()
        # 상하좌우에 배추 있나 보기
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 배열 범위 내에 있으면 배추 위치의 값을 -1로 바꿔주고 큐에 추가
            if 0 <= nr < N and 0 <= nc < M and farm[nr][nc] == 1:
                farm[nr][nc] = -1
                Q.append((nr, nc))


for tc in range(1, int(input()) + 1):
    # M: 가로길이(column), N: 세로길이(row), K: 배추 개수
    M, N, K = map(int, input().split())
    # 일단 0으로 하고
    farm = [[0] * M for _ in range(N)]
    # 입력받은 좌표를 1로 수정
    for k in range(K):
        u, v = map(int, input().split())
        farm[v][u] = 1
    # worm : 필요한 지렁이 개수
    worm = 0
    # 배추가 있으면 (1이면) BFS 하고 지렁이 개수 1 더해주기
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                BFS(i, j)
                worm += 1

    print(worm)