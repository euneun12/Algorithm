import sys
sys.stdin = open('input.txt', 'r')

# dp = [0, 1, 2, 4]
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     dp = dp + [0] * N
#     for i in range(4, N + 1):
#         dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#     print(dp[N])

dp = [0, 1, 2, 4] + [0] * 7
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for tc in range(1, int(input()) + 1):
    N = int(input())
    print(dp[N])