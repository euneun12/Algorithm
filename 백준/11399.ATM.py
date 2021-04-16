N = int(input())
people = list(map(int, input().split()))
people.sort()
for i in range(1, N):
    people[i] += people[i - 1]

print(sum(people))


# def permutation(idx):
#     global minute
#     if idx == N:
#         # 여기서 총 몇 분 걸리나 확인하기
#         count = list(new)
#         for j in range(1, N):
#             count[j] += count[j - 1]
#         temp = sum(count)
#         if temp < minute:
#             minute = temp
#     # 가능한 순서 만드는 곳
#     else:
#         for i in range(N):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 new[idx] = people[i]
#                 permutation(idx + 1)
#                 visited[i] = 0
#
# # tc = int(input())
# N = int(input())
# people = list(map(int, input().split()))
# visited = [0] * N
# new = [0] * N
# minute = 1000000000
# permutation(0)
# print(minute)
