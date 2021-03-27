import sys
sys.stdin = open('input.txt', 'r')

# 이렇게 하면 시간 초과ㅜㅠㅠㅠ
# N = int(input())
# result = 1
# for i in range(2, N//2):
#     cnt = 0
#     while N % (i * i) == 0:
#         N = N // (i * i)
#         result *= i
# print(result)

# 이진 탐색 풀이
N = int(input())
s = 1
e = N
while True:
    mid = (s + e) // 2
    if mid * mid == N:
        break
    elif mid * mid < N:
        s = mid
    else:
        e = mid

print(mid)