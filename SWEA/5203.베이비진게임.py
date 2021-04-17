import sys
sys.stdin = open('input.txt', 'r')


def babygin(player):
    if player == 1:
        card = player1
    else:
        card = player2
    for i in range(10):
        if card[i] > 0 and card[i + 1] > 0 and card[i + 2] > 0:
            return True
        if card[i] >= 3:
            return True


for tc in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    player1 = [0] * 11
    player2 = [0] * 11
    for i in range(12):
        if i % 2:
            player2[cards[i]] += 1
            if babygin(2):
                print('#{} {}'.format(tc, 2))
                break
        else:
            player1[cards[i]] += 1
            if babygin(1):
                print('#{} {}'.format(tc, 1))
                break
    else:
        print('#{} {}'.format(tc, 0))
