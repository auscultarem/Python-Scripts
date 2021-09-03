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
import random
game_images = [ rock, paper, scissors]
list_of_play =["rock", "paper", "scissors"]
machine = random.randint(0, 2)
user_selection = input(" Please select 'rock', 'paper' or 'scissors' to start the game. ->")
#user      Machine
#          r    p    s  r=rock, p=paper, s=scisors
rock1   =["T", "L", "W"] 
paper1  =["W", "T", "L"]
scissors1=["L", "W", "T"]

#print(machine)
#print(list_of_play[machine])

if user_selection == "rock":
  print(user_selection)
  print(rock)
  if rock1[machine] == "T":
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("TIE!")
  elif rock1[machine] == "L":
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("You LOSE!!!")
  else:
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("You WIN!!!")

elif user_selection == "paper":
  print(user_selection)
  print(paper)
  if paper1[machine] == "T":
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("TIE!")
  elif paper1[machine] == "L":
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("You LOSE!!!")
  else:
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("You WIN!!!")

else:
  print(user_selection)
  print(scissors)
  if scissors1[machine] == "T":
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("TIE!")
  elif scissors1[machine] == "L":
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("You LOSE!!!")
  else:
    print("*-*-*- VS *-*-*-")
    print(list_of_play[machine])
    print(game_images[machine])
    print("You WIN!!!")

