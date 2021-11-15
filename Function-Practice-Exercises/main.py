#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or #both numbers are odd

def my_func(a,b):
	print("Lesser of two events")
	if a % 2 == 0 and b % 2 == 0:
		if a < b:
			return  a
		else:
			return b
	else:
		if a < b:
			return b
		else:
			return a

print(my_func(11,9))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def string_crakers(string):
	print("\nAnimal Crackers")
	new_string = string.split()

	string1 = new_string[0]
	string2 = new_string[1]

	if string1[0] == string2[0]:
		return True
	else:
		return False	

print(string_crakers("Levelheaded Llama"))
print(string_crakers("Crazy Kangaroo"))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True

def makes_twenty(a,b):
	print("\nMakes Twenty")
	if a == 20 or b == 20:
		return True
	elif (a + b) ==	20:
		return True
	else:
		return False

print(makes_twenty(20,10))
print(makes_twenty(12,8) )
print(makes_twenty(2,3))

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def capitalize_name(string):
	print("\nCapitalize first letter")
	name = string.capitalize()
	return name

print(capitalize_name("macdonald"))

#MASTER YODA: Given a sentence, return a sentence with the words reversed

def reverse_sentence(string):
	
	reverse_string = string.split()
	reverse_string = reverse_string[::-1]
	return " ".join(reverse_string)


print(reverse_sentence('I am home'))

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
print("\n")
def almost_there(number):
	
	base_number = [100,200]	

	for num in base_number:
		base_plus = num + 10
		base_minus = num - 10
		if number <= base_plus:
			if number >= base_minus:
				return True
			else:
				return False

print(almost_there(110))
print(almost_there(150))
print(almost_there(210))
#print(almost_there(211))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print('\nGiven a list of ints, return True if the array contains a 3 next to a 3 somewhere.\n')
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(enteros):

	variable = False

	for num in range(0, len(enteros) - 1):
		number1 = enteros[num]
		number2 = enteros[num + 1]
		print(number1, number2)
		if number1 == number2:
			variable = True


	return variable

new_list = [1,2,3,3,4,3,5]
new_list2 = [1,2,3,4,3,5]
print(new_list)
print(has_33(new_list))
print(new_list2)
print(has_33(new_list2))

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
print("\nPaper Doll")
def paper_doll(string):
	new_string = [char*3 for char in string]
	return print("".join(new_string))

paper_doll('hello')
paper_doll('Mississippi')

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

def blackjack(a,b,c):

	if a == 11:
		 a = 1
	elif b == 11:
		b = 1
	elif c == 11:
		c = 1

	black_jack = a + b + c

	if black_jack <= 21:
		return print(black_jack)
	else:
		return print('BUST')

blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14
print("\nSUMMER OF '69'\n")
def summer_69(numbers):
	index_s = numbers.index(6)
	index_f = numbers.index(9) + 1
	remove = numbers[index_s:index_f]
	add = 0
	for num in numbers:
		if num in remove:
			pass
		else:
			add+= num
	
	print(add)


variable = [4, 5, 6, 7, 8, 9]
variable2 = [2, 1, 6, 9, 11]
summer_69(variable)
summer_69(variable2)

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 #spy_game([1,2,4,0,0,7,5]) --> True
 #spy_game([1,0,2,4,0,5,7]) --> True
 #spy_game([1,7,2,0,4,5,0]) --> False

print("\nSpy game")
def spy_game(number_list):

	bond_list = [0,0,7]
	result_list = []
	count = 0

	for number in number_list:
		if number == 0:		
			result_list.append(number)			
		elif number == 7:
		 	result_list.append(number)		

	for num in range(0 , len(bond_list)):
		var1 = bond_list[num]
		var2 = result_list[num]	
		if var1 == var2:
			count +=1
	if count == 3:
		return True
	else:
		return False		

number_list1 = [1,0,2,4,0,5,7]
number_list2 = [1,2,4,0,0,7,5]
number_list3 = [1,7,2,0,4,5,0]
print(spy_game(number_list1))
print(spy_game(number_list2))
print(spy_game(number_list3))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25

#By convention, 0 and 1 are not prime.
print("\nCount Primes\n")

def count_primes(number):
	
	primes_list = []

	for numb in range(1, number):
		var = numb
		was_divisible = 0
		
		for num in range(1 , var):
			if var % num  == 0:
				was_divisible += 1
		
		if was_divisible == 1:
			primes_list.append(var)
		else:
			pass
	print(f"The number {number} has {len(primes_list)} primes numbers\n{primes_list}")
	
		
count_primes(1000)

#Just for fun:
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".
# #
def print_big(letter):
	my_letters ={
		'a':'''   #  \n  
  # #   \n
 #   #  \n
#     # \n
####### \n
#     # \n
#     # \n''',
		'b':
'''#####  
 #    # 
 #####  
 #    # 
 #    # 
 ##### ''',

	}

	print(my_letters['a'],'\n', my_letters['b'])

print_big('a')

#case os use map
print("\nCase of use of Maps")
def square(num):
	return num**2

my_nums = [1,2,3,4,5,6]
my_nums2 = list(map(square, my_nums))

print(my_nums2)

#Case of use of filter
print("\nCase of use of filter")
def check_even(num):
	return num % 2 == 0
my_list = [1,2,3,4,5,6]	

my_list2 = list(filter(check_even, my_list))
print(my_list2)

# Case of use of lambda
print("\nCase of use of Lamba")
square = lambda num: num **2
print(square(3))

#Case of use lambda + map
print("\nCase of use lambda and map")
my_list3 = list(map(lambda num: num**2, my_list))
print(my_list3)

#Case of use filter and lambda 
print("\nCase of use filter an lambda")
my_list4 = list(filter(lambda num: num % 2 == 0, my_nums))
print(my_list4)

#another example
print("\nAnother example")
my_names = ['Andy', 'Eve', 'Sally']
my_list5 = list(map(lambda num:num[0], my_names))
print(my_list5)
