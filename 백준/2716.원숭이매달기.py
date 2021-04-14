import sys
sys.stdin = open('input.txt', 'r')

# 최대 깊이 구하는 문제
# [가 나오면 +1, ]가 나오면 -1 했을 때 최대값
for tc in range(1, int(input()) + 1):
    tree = input()
    result = 2
    cnt = 0
    max_cnt = 0
    if len(tree) != 0:
        for i in tree:
            if i == '[':
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt -= 1
        print(result ** max_cnt)
    else:
        print(1)
