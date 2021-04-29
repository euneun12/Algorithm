import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
find = list(map(int, input().split()))

for num in find:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == num:
            print(1)
            break
        elif numbers[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(0)