import random
from decouple import config
from logic import check_win
remain_money=0

money = config('MY_MONEY', default=10000, cast=int)
def play():
    my_money=money
    slots=range(1, 30)
    while True:
        try:
            chosen_slot = int(input('choose slot 1-30: '))
            bet = int(input('your bet amount: '))
        except ValueError:
            print('only numbers')

        if chosen_slot<0 or chosen_slot>30:
            print('you can choose slot only 1-30, try again.')
            continue
        if bet > my_money:
            print(f'not enough money, max bet is {my_money}')
            continue

        else:
            print(f'bet {bet}$ accepted!')

        slot = random.choice(slots)
        print(f'LUCKY SLOT IS {slot}')
        if slot == chosen_slot:
            print(f'your bet won! bonus {bet * 2}$ ')
            my_money += bet * 2
        else:
            print(f'your bet lost! minus {bet}$')
            my_money -= bet
        if my_money<=0:
            print('you lost all money, come back later')
            break

        choice=input(f'{my_money}$ remain, do you want to continue game?\n''print y/n')
        if choice=='y':
            continue
        else:
            check_win(my_money)
        break



