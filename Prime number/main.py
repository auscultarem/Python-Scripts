#Write your code below this line ๐
def prime_checker(number):
    flag = 0
    
    for num in range(2 , (number + 1)):
      valnum = number % num
            
      if valnum == 0:
        flag += 1        
      
    print(flag)

    if flag == 1:
        print("It is a prime number")
    else:
        print("It is not a prime number") 
         

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



