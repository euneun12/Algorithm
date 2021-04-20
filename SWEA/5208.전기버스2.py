import sys
sys.stdin = open('input.txt', 'r')

def BatteryChange(bus, charge, cnt):
    global min_change
    if cnt > min_change:
        return
    for i in range(charge, 0, -1):
        if bus + i >= N:
            if cnt < min_change:
                min_change = cnt
        else:
            BatteryChange(bus + i, battery[bus + i], cnt + 1)


for tc in range(1, int(input()) + 1):
    battery= list(map(int, input().split()))
    N = battery[0]
    min_change = 1000
    BatteryChange(1, battery[1], 0)
    print('#{} {}'.format(tc, min_change))
