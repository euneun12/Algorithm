import sys
sys.stdin = open('input.txt', 'r')

s = input()
t = input()
s_len = len(s)
t_len = len(t)
result = 0
if s_len == t_len and s == t:
    result = 1
else:
    if s * t_len == t * s_len:
        result = 1

print(result)