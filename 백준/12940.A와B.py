import sys
sys.stdin = open('input.txt', 'r')

# def check(S):
#     global result
#     if S == T:
#         result = 1
#         return
#     if len(S) > len(T):
#         return
#     S1 = S + 'A'
#     check(S1)
#     S2 = ('B' + S)[::-1]
#     check(S2)
#
#
# S = input()
# T = input()
# result = 0
# check(S)
# print(result)

S = list(input())
T = list(input())
result = 0
while len(S) < len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]

    if S == T:
        result = 1
        break

print(result)