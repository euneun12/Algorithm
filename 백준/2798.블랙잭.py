import sys
sys.stdin = open('input.txt', 'r')


def combination(index, start):
    global result
    if index == 3:
        temp = sum(select)
        if temp <= M:
            if result < temp:
                result = temp
    else:
        for i in range(start, N):
            select[index] = card[i]
            combination(index + 1, i + 1)


N, M = map(int, input().split())
card = list(map(int, input().split()))
result = 0
select = [0] * 3
combination(0, 0)
print(result)