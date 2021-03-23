import sys
sys.stdin = open('input.txt', 'r')

def com(idx, start):
    if idx == M:
        print(*result)

    else:
        for i in range(start, N):
            result[idx] = number[i]
            com(idx + 1, i + 1)



N, M = map(int, input().split())
result = [0] * M
number = [i for i in range(1, N + 1)]
com(0, 0)
