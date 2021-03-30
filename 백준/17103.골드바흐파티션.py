import sys
sys.stdin = open('input.txt', 'r')



tc = int(input())
numbers = [int(input()) for _ in range(tc)]
N = max(numbers)
# 테스트케이스 중에서 가장 큰 수 골라서 그 수 중에 소수인 것은 True로 하고 아니면 False
prime = [False, False] + [True] * (N - 1)
for i in range(2, N // 2):
    if prime[i]:
        for j in range(i * 2, N + 1, i):
            if prime[j]:
                prime[j] = False

# 테스트케이스에 대해서
for number in numbers:
    cnt = 0
    for j in range(2, number // 2 + 1):
        # 두 수 모두 소수이면 카운트
        if prime[j] and prime[number - j]:
            cnt += 1
    print(cnt)

# def prime(num):
#     for k in range(2, num):
#         if num % k == 0:
#             break
#     else:
#         return 1
#
# for i in range(1, int(input()) + 1):
#     number = int(input())
#     cnt = 0
#     for j in range(2, number // 2 + 1):
#         if prime(j):
#             if number - j == 1 or prime(number - j):
#                 cnt += 1
#     print(cnt)