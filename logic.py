import game

def check_win(my_money):
    if my_money>game.money:
        print(f'you won {my_money-game.money}$!')
    else:
        print(f'you lost{game.money-my_money}$!')