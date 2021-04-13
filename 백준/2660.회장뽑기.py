import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def BFS(start):
    # 방문 체크
    visited = [0] * (N + 1)
    Q = deque()
    Q.append(start)
    visited[start] = 1
    while Q:
        s = Q.popleft()
        # s와 친구인 모든 v에 대해서 방문 안했으면 Q에 추가하고 거리 1 더해주기
        for v in friends[s]:
            if visited[v] == 0:
                Q.append(v)
                visited[v] = visited[s] + 1
    # 방문 표시해서 1부터 시작하니까 1 빼서 리턴
    return max(visited) - 1


N = int(input())
friends = [[] for _ in range(N + 1)]
result = []
# -1 -1이 입력될때까지 친구 정보 받아오기
while True:
    u, v = map(int, input().split())
    if u == -1:
        break
    friends[u].append(v)
    friends[v].append(u)

# 각 사람에 대해 점수 계산
for i in range(1, N + 1):
    result.append(BFS(i))

# 점수 제일 낮은 사람이 후보
score = min(result)
cnt = result.count(score)
print(score, cnt)
for i in range(N):
    if score == result[i]:
        print(i + 1, end=' ')