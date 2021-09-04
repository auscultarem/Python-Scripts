#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
from replit import clear
should_continue = True

while should_continue:
	clear()
	print(logo)
	guess_number = random.randint(0, 100)
	print("Guess the number from 0 to 100.")
	dificulty = input(("Choose a dificulty. Type 'easy' or 'hard' "))
	variable = 0

	if dificulty == 'easy':
		counter_easy = 10
		while counter_easy > 0:
			variable = int(input(f"You have{counter_easy} lifes ,Guess the number: "))
			if variable == guess_number:
				counter_easy = 0
				should_continue = False
				print("You win!!")
			elif variable < guess_number:
				counter_easy -= 1
				print("Too Low")	
			elif variable > guess_number:
				print("Too High")
				counter_easy -=1
			elif counter_easy == 0:
				should_continue = False 	

	elif dificulty == 'hard':
		counter_hard = 5
		should_continue = False
	else:
		print("type a correct dificulty")		