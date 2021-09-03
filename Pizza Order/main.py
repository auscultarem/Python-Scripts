# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L -> ")
add_pepperoni = input("Do you want pepperoni? Y or N ->")
extra_cheese = input("Do you want extra cheese? Y or N ->")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_amount = 0

if size == 'S':
  total_amount = 15
  if add_pepperoni == 'Y':
    total_amount += 2
    if extra_cheese == 'Y':
      total_amount += 3
      print(f"The toyal amount is: ${total_amount}")
    else:
      print(f"The toyal amount is: ${total_amount}") 
  else:
    if extra_cheese == 'Y':
      total_amount += 3
      print(f"The total amount is: ${total_amount}")
    else:
      print(f"The total amount is: ${total_amount}") 
#*-*-*-*-*-* size M
elif size == 'M':
  total_amount = 20
  if add_pepperoni == 'Y':
    total_amount += 2
    if extra_cheese == 'Y':
      total_amount += 3
      print(f"The total amount is: ${total_amount}")
    else:
      print(f"The total amount is: ${total_amount}") 
  else:
    if extra_cheese == 'Y':
      total_amount += 3
      print(f"The total amount is: ${total_amount}")
    else:
      print(f"The total amount is: ${total_amount}")
 #*-*-*-*-*-*-*-* Size L
elif size == 'L':
  total_amount = 25
  if add_pepperoni == 'Y':
    total_amount += 2
    if extra_cheese == 'Y':
      total_amount += 3
      print(f"The toal amount is: ${total_amount}")
    else:
      print(f"The toal amount is: ${total_amount}") 
  else:
    if extra_cheese == 'Y':
      total_amount += 3
      print(f"The total amount is: ${total_amount}")
    else:
      print(f"The total amount is: ${total_amount}") 

else:
  print("Please enter a valid size")

