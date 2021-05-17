import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')


while True:
    numbers = list(map(int, input().split()))
    k = numbers[0]
    S = numbers[1:]
    if k == 0:
        break
    results= list(combinations(S, 6))
    for result in results:
        print(*result)
    print()

# def combi(start, index):
#     if index == 6:
#         print(*result)
#     else:
#         for i in range(start, len(S)):
#             result[index] = S[i]
#             combi(i + 1, index + 1)
# while True:
#     numbers = list(map(int, input().split()))
#     k = numbers[0]
#     S = numbers[1:]
#     S.sort()
#     result = [0] * 6
#     if k == 0:
#         break
#     combi(0, 0)
#     print()

