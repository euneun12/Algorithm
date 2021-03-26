import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def DFS(s):
    global count
    visited[s] = 1
    if s == e:
        return 1
    for w in G[s]:
        if visited[w] == 0:
            if DFS(w) == 1:
                count += 1
                return 1
    return -1


n = int(input())
s, e = map(int, input().split())
m = int(input())
visited = [0] * (n + 1)
G = [[] for _ in range(n + 1)]
count = 0

for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

result = DFS(s)
print(result if result == -1 else count)