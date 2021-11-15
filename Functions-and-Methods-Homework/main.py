#Write a function that computes the volume of a sphere given its radius.
def vol(rad):
	volume = (4 *((3.1416)* rad**3))/3

	return volume
print(f"The volume of a sphere is {vol(2)}")


#Write a function that checks whether a number is in a given range (inclusive of high and low)

def rank_check( num,low,high):
	if num >= low and num <=high:
		return f'The {num} is between {low} and {high}'
	else:
		return f'The {num} is not between {low} and {high}'
print("\nCheck if a number in a given range")
print(rank_check(1,2,7))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

print("\nCheck ther lower letter and the upper letters in a sentence")
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(string):
	
	lower_letter = [letter for letter in s if letter.islower()]
	upper_letter = [letter for letter in s if letter.isupper()]
	print(f"There are {len(lower_letter)} lower letters in the sentence")
	print(f"There are {len(upper_letter)} upper letters in the sentence")


up_low(s)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
print("\nReturn a list of unique elements\n")
my_list = [1,1,1,1,2,2,3,3,3,3,4,5]
def unique_list(string):
	return set(string)

print(unique_list(my_list))

# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24
print("\nMultiply all elements inside a list")

def multiply(list_numbers):
	result = 1
	for num in list_numbers:
		result *= num
	print(result)

my_list2 = [1, 2, 3, -4, 5, 9, 6]

print(f"The result of multiply my list is : {multiply(my_list2)}")

# Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

def palindrome(string):
	string_validation = True
	reverse_string = string[::-1]

	for char in range(0 , len(string)):
		character1 = string[char]
		character2 = reverse_string[char]
		print(character1, character2)
		if character1 == character2:
			string_validation = True
		else:
			string_validation = False		
	return string_validation	

string1 = 'helleh'
print(palindrome(string1))

# Hard:
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Hint: You may want to use .replace() method to get rid of spaces.

print("\nPangram Exercise\n")

import string

sentence = "The quick brown fox jumps over the lazy dog"
sentence.lower()


def ispangram(sentence):

	ascii_list = list(string.ascii_lowercase)
	validation_list = []

	sentence = sentence.lower()
	sentence = sentence.replace(" ","")
	
	sentence_list = [char for char in sentence]
	
	for num in range(0, len(sentence_list)):
		for char in ascii_list:				
			if char in sentence_list:
				sentence_list.remove(char)
				validation_list.append(char)
	
	validation_list = set(validation_list)
	if len(validation_list) == len(ascii_list):
		print('True')
	else:
		print('False')

ispangram(sentence)