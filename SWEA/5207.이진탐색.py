import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A_lst = list(map(int, input().split()))
    A_lst.sort()
    B_lst = list(map(int, input().split()))
    cnt = 0
    for num in B_lst:
        flag = 0
        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2
            if A_lst[m] == num:
                cnt += 1
                break
            if num < A_lst[m]:
                if flag == 1:
                    break
                r = m - 1
                flag = 1
            else:
                if flag == -1:
                    break
                l = m + 1
                flag = -1


    print('#{} {}'.format(tc, cnt))