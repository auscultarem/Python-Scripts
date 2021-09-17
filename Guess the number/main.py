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

def game(lives, guess_number):
	counter = lives	
	while counter > 0:
			variable = int(input(f"You have {counter} lifes ,Guess the number: "))
			if variable == guess_number:
						print("You win!!")
						return False
			elif variable < guess_number:
						counter -= 1
						print("Too Low")	
			elif variable > guess_number:
						print("Too High")
						counter -= 1
	if counter == 0:
		print("You loose")
	
	 
while should_continue:
	clear()
	print(logo)
	guess_number = random.randint(0, 100)
	print("Guess the number from 0 to 100.")
	dificulty = input(("Choose a dificulty. Type 'easy' or 'hard' "))
	lives_easy = 10
	lives_hard = 5
	
	if dificulty == 'easy':
		counter = lives_easy
		should_continue = game(counter, guess_number) 	

	elif dificulty == 'hard':
		counter = lives_hard
		should_continue = game(counter, guess_number)
	else:
		print('Elige una opcion correcta')

			