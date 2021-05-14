import sys
sys.stdin = open('input.txt', 'r')


# def tile(i):
#     if i == 1:
#         return 1
#     elif i == 2:
#         return 2
#     else:
#         result = tile(i - 1) + tile(i - 2)
#         return result
#
# N = int(input())
# print(tile(N) % 10007)


N = int(input())
if N == 1:
    print(1)
else:
    count = [0, 1, 2] + [0] * (N - 2)
    for i in range(3, N + 1):
        count[i] = count[i - 1] + count[i - 2]
    print(count[N] % 10007)
