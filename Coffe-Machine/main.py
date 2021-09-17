from Menu import MENU
from Menu import resources
QUARTER = 0.25
DIMES = 0.10
PENY = 0.01
NICKEL = 0.05

def report():
	for item in resources:
		print(item, resources[item])

def sum_of_money(a_quarters, a_dimes, a_nickels, a_pennies):
	money_of_quarters = a_quarters * QUARTER
	money_of_dimes = a_dimes * DIMES
	money_of_nickels = a_nickels * NICKEL
	money_of_pennies = a_pennies * PENY

	sum_of_money = money_of_quarters + money_of_dimes + money_of_nickels + money_of_pennies

	return float(sum_of_money)

def calculus_espresso():
	""" rest the amount of resources """
	water_in_machine = resources['water']
	coffee_in_machine = resources['coffee']
		
	water_espresso = MENU['espresso']['ingredients']['water']
	coffee_espresso  = MENU['espresso']['ingredients']['coffee']
	rest_of_water = water_in_machine - water_espresso
	rest_of_coffee = coffee_in_machine - coffee_espresso
	
	resources['water'] = rest_of_water
	resources['coffee'] = rest_of_coffee
	


def calculus_latte():
	water_in_machine = resources['water']
	coffee_in_machine = resources['coffee']
	milk_in_machine = resources['milk']

	water_latte = MENU['latte']['ingredients']['water']
	milk_latte = MENU['latte']['ingredients']['milk']
	coffee_latte = MENU['latte']['ingredients']['coffee']
	rest_of_water = water_in_machine - water_latte
	rest_of_milk = milk_in_machine - milk_latte
	rest_of_coffee = coffee_in_machine - coffee_latte
	resources['water'] = rest_of_water
	resources['coffee'] = rest_of_coffee
	resources['milk'] = rest_of_milk
	


def calculus_cappuccino():
	water_in_machine = resources['water']
	coffee_in_machine = resources['coffee']
	milk_in_machine = resources['milk']

	water_cappuccino = MENU['cappuccino']['ingredients']['water']
	milk_cappuccino = MENU['cappuccino']['ingredients']['milk']
	coffee_cappuccino = MENU['cappuccino']['ingredients']['coffee']
	rest_of_water = water_in_machine - water_cappuccino
	rest_of_milk = milk_in_machine - milk_cappuccino
	rest_of_coffee = coffee_in_machine - coffee_cappuccino
	resources['water'] = rest_of_water
	resources['coffee'] = rest_of_coffee
	resources['milk'] = rest_of_milk
	


def user_selection(selection_of_coffe, money_of_user):
		
	if money_of_user >= 1.5:
    #User selection
		if selection_of_coffe == 'espresso':
			cost = MENU['espresso']['cost']
			water_in_machine = resources['water']
			coffee_in_machine = resources['coffee']
			#Verify if there are resources
			if water_in_machine >= 50 and coffee_in_machine >= 18:				
				calculus_espresso()
				change_money = round(money_of_user - cost, 2)
				print(f"Here your money in change $ {change_money}")
				print("Here you are your coffe.Thank you!!")
			else:
				print("Sorry there are not enough resources ....")	
			
			
    #User selection
		elif selection_of_coffe == 'latte':
			cost = MENU['latte']['cost']
			water_in_machine = resources['water']
			coffee_in_machine = resources['coffee']
			milk_in_machine = resources['milk']
			#Verify if there are resources
			if water_in_machine >= 200 and coffee_in_machine >= 24 and milk_in_machine >= 150:
				calculus_latte()
				change_money = round(money_of_user - cost, 2)
				print(f"Here your money in change $ {change_money}")
				print("Here you are your coffe.Thank you!!")
			else:
				print("Sorry there are not enough resources ....")
			
    #User selection
		elif selection_of_coffe == 'cappuccino':
			cost = MENU['cappuccino']['cost']
			water_in_machine = resources['water']
			coffee_in_machine = resources['coffee']
			milk_in_machine = resources['milk']
			
			#Verify if there are resources
			if water_in_machine >= 250 and coffee_in_machine >= 24 and milk_in_machine >= 100:
				calculus_cappuccino()
				change_money = round(money_of_user - cost, 2)
				print(f"Here your money in change $ {change_money}")
				print("Here you are your coffe.Thank you!!")
			else:
				print("Sorry there are not enough resources ....")

	else:
		print("Sorry that's no enough money")


def coffe_machine():
	should_continue = True
	
	while should_continue:
					
		selection_of_coffee = input("What would you like? (espresso/late/capuccino : ").lower()
		if selection_of_coffee == 'exit':
			should_continue = False
		elif selection_of_coffee == 'report':
			report()			
		else:	
			amount_quarters = int(input("How many quarters?: "))
			amount_dimes = int(input("How many dimes?: "))
			amount_nickels = int(input("How many nickels?: "))
			amount_pennies = int(input("How many pennies?: "))
			money_of_user = sum_of_money(amount_quarters, amount_dimes, amount_nickels, amount_pennies)
			user_selection(selection_of_coffee, money_of_user)
		


coffe_machine()