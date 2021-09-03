# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
print(names)

people = len(names)
#print(people)
person = random.randint(0, people - 1)
#print(person)
pay_the_account = names[person]
print(f"{pay_the_account} is going to pay the account")



