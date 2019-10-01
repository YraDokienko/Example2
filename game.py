import random
from player import Player
from control import Control

control = Control()
player1 = Player('Power man', 15, 1.0, 100)
player2 = Player('Healthy man', 10, 1.0, 150)
player3 = Player('Skill man', 10, 2.0, 100)

warrior = int(input('Please select warrior: 1 - strong, 2 - healthy, 3 - skill \n'))
if warrior == 1:
    warrior = player1
elif warrior == 2:
    warrior = player2
elif warrior == 3:
    warrior = player3
print('Your warrior : ')
warrior.show_player()

opponent_random = random.randint(1, 3)
if opponent_random == 1:
    opponent = player1
elif opponent_random == 2:
    opponent = player2
elif opponent_random == 3:
    opponent = player3
print('Opponent : ')
opponent.show_player()
control.control_battle(warrior, opponent)
