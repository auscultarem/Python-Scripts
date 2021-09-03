import random

random_integer = random.randint(1 , 10)
print(random_integer)

random_float = random.random()
print(random_float)

new_random_number = float(random_integer) + random_float

print(new_random_number)