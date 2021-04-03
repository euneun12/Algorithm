import sys
sys.stdin = open('input.txt', 'r')

def perm(idx):
    if idx == M:
        print(*result)
    else:
        for i in range(N):
            result[idx] = number[i]
            perm(idx + 1)

N, M = map(int, input().split())
result = [0] * M
number = [i for i in range(1, N + 1)]
perm(0)
