from art import logo, game_over
from replit import clear
table = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
tic_tac = ['X','O']

def select_market():

	user_selection = input("Hello which market would you like to be: 'X' or 'O': ")
	user_selection = user_selection.upper()
	if user_selection in tic_tac:
		return True, user_selection
	else:
		return False, True


def display_board(market, box):
	clear()
	print(logo)

	table[box] = tic_tac[market]
	print('\t\t\t\t\t'+'1'+'|'+'2'+'|'+'3')
	print('\t\t\t\t\t'+'4'+'|'+'5'+'|'+'6')
	print('\t\t\t\t\t'+'7'+'|'+'8'+'|'+'9')
	print("\n")
	print('\t\t\t\t\t'+table[1]+'|'+table[2]+'|'+table[3])
	print("\t\t\t\t\t-----")
	print('\t\t\t\t\t'+table[4]+'|'+table[5]+'|'+table[6])
	print("\t\t\t\t\t-----")
	print('\t\t\t\t\t'+table[7]+'|'+table[8]+'|'+table[9])

def box_selection(market):	
	
	is_not_number = True
	
	while is_not_number:		
		try:
			user_box = int(input(f"Player '{market}' Please select a box (1-9): "))
			if user_box in range(1,10):
				if table[user_box] == ' ':
					is_not_number = False
					return user_box
				else:
					print("It is not empty try another box")
		except ValueError:
			print("Oops!  That was no valid number.  Try again...")
			

	

def switch_user(first_user):	
	if first_user == 0:
		second_user = 1
	else:
		second_user = 0		
	return second_user

def check_winer(market):
		 
	if table[1] == table[2] and table[2] == table[3] and table[3] == market:
		return True
	elif table[4] == table[5] and table[5] == table[6] and  table[6] == market:
		return True
	elif table[7] == table[8] and table[8] == table[9] and table[9] == market:
		return True
	elif table[1] == table[4] and table[4] == table[7] and table[7] == market:
		return True
	elif table[2] == table[5] and table[5] == table[8] and table[8] == market:
		return True
	elif table[3] == table[6] and table[6] == table[9] and table[9] == market:
		return True
	elif table[1] == table[5] and table[5] == table[9] and table[9] == market:
		return True
	elif table[3] == table[5] and table[5] == table[7] and table[7] == market:
		return True	
	else:
		return False	

def should_continue():

	reset = input("Would you like another game?: (Y/N) -> ")
	reset = reset.upper()	
	if reset == 'Y':
		return True
	else:
		return False

def reset_game():
	global table 

	table = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


		
is_game_on = False
is_game_off = True

while is_game_off:
	print(logo)

	is_game_on , user_selection = select_market()

	if is_game_on:
		is_game_off = False

		while is_game_on:

			first_user = tic_tac.index(user_selection)
			second_user = switch_user(first_user)
			winer = False	

			display_board(first_user, box_selection(tic_tac[first_user]) )
			winer = check_winer(tic_tac[first_user])
			if winer:
				print(f"Player {tic_tac[first_user]} is the winer")
				continue_game = should_continue()
				if continue_game:
					reset_game()
				else:
					clear()
					print(game_over)
					is_game_on = False	
					break
				
			display_board(second_user, box_selection(tic_tac[second_user]) )
			winer = check_winer(tic_tac[second_user])
			if winer:
				print(f"Player {tic_tac[second_user]} is the winer")
				continue_game = should_continue()
				if continue_game:
					reset_game()
				else:
					clear()
					print(game_over)
					is_game_on = False	
					break
	
	else:
		clear()
		print("\t Wrong election please enter a valid election...\n")
			