# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
from euler import Euler

euler = Euler()
print( euler.multiple3_or_5(1000) )
#Next problem
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
print(euler.fibonacci( 50 ))
print(euler.sum_even_fibonacci())

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
primes_list = euler.the_prime_numbers(10000)
# euler.the_largest_prime_factor(13195, primes_list)
euler.the_largest_prime_factor(600851475143, primes_list) #the answer is [71,839,1471,6857]