import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
prime = [True] * (N + 1)
cnt = 0
flag = False
for i in range(2, N + 1):
    if prime[i]:
        for j in range(1, N // i + 1):
            if prime[i * j]:
                prime[i * j] = False
                cnt += 1
            if cnt == K:
                print(i * j)
                flag = True
                break
        if flag:
            break
