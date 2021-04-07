import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def BFS(B):
    while Q:
        temp, cnt = Q.popleft()
        if temp == B:
            return cnt
        temp1 = temp * 2
        if temp1 <= B:
            Q.append((temp1, cnt + 1))
        temp2 = temp * 10 + 1
        if temp2 <= B:
            Q.append((temp2, cnt + 1))

    return -1
A, B = map(int, input().split())
Q = deque()
Q.append((A, 1))

print(BFS(B))

