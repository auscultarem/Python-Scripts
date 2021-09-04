from replit import clear
people_list = []
#HINT: You can call clear() to clear the output in the console.
def add_blind_auction(name, amount):
	blind_dictionary = {}

	blind_dictionary["Name_of_person"] = name
	blind_dictionary["Start_amount"]   = amount
	people_list.append(blind_dictionary)
	

def winer():
	amount = 0
	amount_per_person = []
	
	
	for person in range(0, len(people_list)):
		amount = people_list[person]["Start_amount"]
		amount_per_person.append(int(amount))
	
	maximo = max(amount_per_person)

	for person in range(0, len(people_list)):
		amount = people_list[person]["Start_amount"]
		if maximo == int(amount):
			clear()
			print(logo)
			print("The winer is: ", people_list[person]["Name_of_person"])
		

from art import logo
print(logo)
finish_entry = True


	
while finish_entry:
	
	name_input= input("Please enter a name: ")
	amount_input = input("Please enter an amount:$ ")
	add_blind_auction(name_input, amount_input)
	decition = input("Would you like enter anoter user: 'Yes' , 'No'-> ")
	if decition == "No":
		finish_entry = False
		winer()
	else:
		clear()