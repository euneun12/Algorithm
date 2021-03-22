import sys
sys.stdin = open('input.txt', 'r')

def perm(idx):
    if idx == M:
        print(*result)
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                result[idx] = number[i]
                perm(idx + 1)
                visited[i] = 0

N, M = map(int, input().split())
result = [0] * M
number = [i for i in range(1, N + 1)]
visited = [0] * N
perm(0)
