import sys
sys.stdin = open('input.txt', 'r')


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def dfs(r, c, cnt, tmp):
    if cnt == 6:
        result.add(tmp)
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, cnt + 1, tmp + matrix[nr][nc])


for tc in range(1, int(input()) + 1):
    matrix = [input().split() for tc in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, matrix[i][j])

    print('#{} {}'.format(tc, len(result)))