
print("**** Welcome to the tip calculator ****")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What porcentaje bill would you like to give? 10, 12, 15? : "))
split_bill = int(input("How many people to split the bill? "))
pay_per_person =  ((((total_bill/100) * percentage_tip) + total_bill )/ split_bill )
print("Each person sould pay: ", round(pay_per_person, 2))