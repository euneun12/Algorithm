import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = [False, False] + [True] * 1003001
prime = []
# 에라토스테네스 체로 소수...
# 1003001이 1000000 이상인소수이면서 팰린드롬 수 중 가장 작은 수
for i in range(2, 1003003):
    if numbers[i]:
        # 소수인 것만 넣기
        prime.append(i)
        for j in range(i * 2, 1003003, i):
            numbers[j] = False
# 소수로 된 것들 중에서
for num in prime:
    # N보다 작은건 그냥 넘기기
    if num < N:
        continue
    # 팰린드롬 수이면 출력하고 끝내기
    if str(num) == str(num)[::-1]:
        print(num)
        break