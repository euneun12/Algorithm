import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def BFS(height):
    Q = deque()
    # 영역 개수 초기화
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 비 높이보다 큰 수이고 방문 안했을때 Q에 담는다.
            if area[i][j] > height and alert[i][j] == 0:
                alert[i][j] = 1
                Q.append((i, j))
                # 주변 탐색하기
                # 사방으로 비 높이 보다 높고 방문 안했으면 방문표시하고 Q에 담는다
                # Q가 빌 때마다 영역이 1개씩 증가한다.
                while Q:
                    r, c = Q.popleft()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < N and alert[nr][nc] == 0 and area[nr][nc] > height:
                            alert[nr][nc] = 1
                            Q.append((nr, nc))
                cnt += 1
    count.append(cnt)

N = int(input())
# 높이 정보 받아올 곳
area = []
max_height = 0
# 비 내리는 양에 따른 영역 개수
count = []
for i in range(N):
    temp = list(map(int, input().split()))
    area.append(temp)
    max_temp = max(temp)
    max_height = max(max_height, max_temp)

# 비는 0에서 최대 높이일 때까지 내린다하면
for i in range(max_height + 1):
    # 비 내렸을 때 정보 담을 곳
    alert = [[0] * N for _ in range(N)]
    # 영역 개수 구하기
    BFS(i)

print(max(count))