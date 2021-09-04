#Write your code below this row 👇
total = 0

for num in range(1, 101, 2): 
  total += num

total2 = 0

for num in range(2, 101 , 2):
  total2 += num

print(f"The sum of odd numbers from 1 yo 100 is: {total}")
print(f"The sum of even numbers from 1 yo 100 is: {total2}")
