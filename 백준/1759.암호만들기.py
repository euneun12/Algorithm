import sys
sys.stdin = open('input.txt', 'r')


def comb(start, idx, vow_cnt):
    # 자음이 최소 두개 포함되어야 하기 때문에 넣은 조건
    if (L - 2) < vow_cnt:
        return
    # 암호가 완성되었을 때
    if idx == L:
        # 모음이 1개 이상 포함되어야한다.
        if vow_cnt != 0:
            print(''.join(result))
        return
    # 조합 생성
    for i in range(start, C):
        result[idx] = alpha[i]
        comb(i + 1, idx + 1, vow_cnt + 1 if alpha[i] in vowel else vow_cnt)


L, C = map(int, input().split())
# 알파벳 오름차순이니까 아스키코드로 변환해서 했는데 그냥 해도 오름차순 된다..! 호엥
alpha = list(input().split())
# alpha = list(map(ord, input().split()))
alpha.sort()
# 모음들
vowel = {'a', 'e', 'i', 'o', 'u'}
# 완성된 암호 저장할 곳
result = [0] * L
# 조합!!
comb(0, 0, 0)
