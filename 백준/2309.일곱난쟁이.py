import sys
sys.stdin = open('input.txt', 'r')


def perm(i, total):
    global result
    # 100이 넘으면 더 할 필요 없음
    if total > 100:
        return
    # 순열이 완성되었을 때
    if i == 7:
        # 합이 100이면 result 바꿔주기
        if total == 100:
            result = sorted(temp)
        return
    # 순열 생성
    for j in range(i, 9):
        if visit[j]:
            continue
        visit[j] = 1
        temp[i] = h[j]
        perm(i + 1, total + temp[i])
        visit[j] = 0


h = []
for i in range(9):
    h.append(int(input()))
# 순열 만들곳
temp = [0] * 7
# 방문체크
visit = [0] * 9
# 출력할 정렬된 결과
result = []
perm(0, 0)
print('\n'.join(map(str, result)))

