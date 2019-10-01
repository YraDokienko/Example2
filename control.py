import random


def inp_ut(value):
    """ Метод проверяет правильность выбора Игроком предлагаемых вариантов действий (1,2,3)"""
    while True:
        try:
            template = [1, 2, 3]
            data = int(input('{} {}'.format(value, '>>>')))
            if data in template:
                return data
            print("Please retype")
        except ValueError:
            print("Please retype")


class Control():

    def __init__(self):
        print('SUPER FIGHT GAME!')
        self.flag_game = True  # Флаг для управления ИГРОЙ

    def control_battle(self, warrior, opponent):
        """Метод контроля БОЯ"""
        while self.flag_game:
            print('Opponent  HP: ', opponent.get_health())
            print('Your warrior HP: ', warrior.get_health())
            print()

            kick = inp_ut('Please select kick: 1 - to head, 2 - to body, 3 - to foot = ')
            block = inp_ut('Please select block: 1 - to head, 2 - to body, 3 - to foot = ')

            print()

            opponent_kick = random.randint(1, 3)
            opponent_block = random.randint(1, 3)

            if kick != opponent_block:
                print('You hit an opponent!')
                opponent.set_health(opponent.get_health() - (warrior.get_power() * warrior.get_skill()))

            if block != opponent_kick:
                print('Opponent hit you :( ')
                warrior.set_health(warrior.get_health() - (opponent.get_power() * opponent.get_skill()))

            if opponent.get_health() <= 0:
                break

            if warrior.get_health() <= 0:
                self.flag_game = False
                break

        if self.flag_game:
            print('YOU WINNER!!!')
        else:
            print('GAME OVER!!!.')
