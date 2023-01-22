import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
moves = {0: rock, 1: paper, 2: scissors}
player_1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
player_2 = random.randint(0,2)
print(moves[player_1])
print(moves[player_2])

if player_1 == player_2:
  print('Nobody wins.')
else:
  if player_1 == 0:
    if player_2 == 1:
      print('Player 2 wins')
    else:
      print('Player 1 wins')
  elif player_1 == 1:
    if player_2 == 0:
      print('Player 1 wins')
    else:
      print('Player 2 wins')
  else:
    if player_2 == 0:
      print('Player 2 wins')
    else:
      print('Player 1 wins')