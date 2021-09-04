programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.",
	 "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary
print(programming_dictionary["Function"])
#adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

#create an empty dictionary
empty_dictionary = {}

#Wipe an empty dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in a empty_dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
print("*-*-*-*-*-*-*-*-*-*-*-")
#Loop through a dictionary
for key in programming_dictionary:
	print(key)
	print(programming_dictionary[key])