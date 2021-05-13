import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))
max_num = max(numbers)
zero_count = [1, 0] + [0] * (max_num - 1)
one_count = [0, 1] + [0] * (max_num - 1)
for j in range(2, max_num + 1):
    zero_count[j] = zero_count[j - 1] + zero_count[j - 2]
    one_count[j] = one_count[j - 1] + one_count[j - 2]

for num in numbers:
    print(zero_count[num], one_count[num])