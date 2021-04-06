
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
tree = [[] for _ in range (N + 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parent = [0] * (N + 1)
Q = deque()
Q.append(1)

while Q:
    node = Q.popleft()
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            Q.append(i)

for i in range(2, N + 1):
    print(parent[i])
