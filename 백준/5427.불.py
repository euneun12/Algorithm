import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS():
    # 불 먼저 번지게하기
    while p:
        for i in range(len(f)):
            fr, fc = f.popleft()
            for j in range(4):
                nfr = fr + dr[j]
                nfc = fc + dc[j]
                if -1 < nfr < h and -1 < nfc < w:
                    if fire[nfr][nfc] == '.' or fire[nfr][nfc] == '@':
                        fire[nfr][nfc] = '*'
                        f.append((nfr, nfc))
        # 상근이 이동
        for k in range(len(p)):
            pr, pc = p.popleft()
            for i in range(4):
                npr = pr + dr[i]
                npc = pc + dc[i]
                if npr < 0 or npr >= h or npc < 0 or npc >= w:
                    return distance[pr][pc]
                elif fire[npr][npc] == '.' and 0 <= npr < h and 0 <= npc < w and distance[npr][npc] == 0:
                    distance[npr][npc] = distance[pr][pc] + 1
                    p.append((npr, npc))
    return 'IMPOSSIBLE'


for tc in range(1, int(input()) + 1):
    w, h = map(int, input().split())
    fire = [list(input()) for _ in range(h)]
    p = deque()
    f = deque()
    distance = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if fire[i][j] == '@':
                p.append((i, j))
                distance[i][j] = 1
            elif fire[i][j] == '*':
                f.append((i, j))

    print(BFS())