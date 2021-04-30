import sys
sys.stdin = open('input.txt', 'r')


def QuickSort(lo, hi):
    if lo < hi:
        # 피봇보다 작은 수 중 마지막 수를 가리키는 인덱스
        i = lo - 1
        for j in range(lo, hi):
            # 피봇보다 수가 작으면
            if numbers[j] < numbers[hi]:
                # i를 증가시키고 수 교환
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        # 여기까지 하면 인덱스 i까지는 피봇보다 작은 값이고 그 이후는 크거나 같은 값
        # i를 1 증가 시켜서 피봇의 숫자와 교환해주면 피봇 값의 위치는 정해진 것!
        i += 1
        numbers[i], numbers[hi] = numbers[hi], numbers[i]
        # 이제 기존 피봇의 왼쪽과 오른쪽을 또 각각 퀵정렬해주면 된다.
        QuickSort(lo, i - 1)
        QuickSort(i + 1, hi)



for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    QuickSort(0, N - 1)
    print('#{} {}'.format(tc, numbers[N // 2]))
