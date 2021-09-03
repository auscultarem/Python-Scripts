# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

true = 0
love = 0

#True
#firt name
true += name1_lower.count("t")
true += name1_lower.count("r")
true += name1_lower.count("u")
true += name1_lower.count("e")
#second name
true += name2_lower.count("t")
true += name2_lower.count("r")
true += name2_lower.count("u")
true += name2_lower.count("e")

#false
#firt name
love += name1_lower.count("l")
love += name1_lower.count("o")
love += name1_lower.count("v")
love += name1_lower.count("e")
#second name
love += name2_lower.count("l")
love += name2_lower.count("o")
love += name2_lower.count("v")
love += name2_lower.count("e")


percentage = str(true) + str(love)
print(f"\nTimes true {true}, times False {love}")
print(f"The porcentage is {percentage}")

if int(percentage) <= 10 or int(percentage) >= 90:
  print(f"Your score is {percentage}, you go togeter like a coke and mentos")
elif int(percentage) <= 40 and int(percentage) <= 50:
  print(f"Your score is {percentage}, you alright togeter")
else:
  print(f"Your score is {percentage}.\n")