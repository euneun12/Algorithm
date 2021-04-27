import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dp = [0 for _ in range(N + 1)]
# N // 3, N // 2, N - 1에 해당하는 수에서 한 번의 연산을 더 하면 N이 만들어진다.
for i in range(2, N + 1):
    # 먼저 1을 뺀 경우 연산 회수 저장
    dp[i] = dp[i - 1] + 1
    # 2로 나누어질 경우 1을 밴 것과 2로 나눈 값의 연산 회수에 1 더한 것 중 최소값
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나누어질 경우 1을 밴 것과 3로 나눈 값의 연산 회수에 1 더한 것 중 최소값
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[N])