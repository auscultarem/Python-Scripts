
class Euler:

	def __init__(self):
		self.fibonacci_list = []

	def multiple3_or_5(self, number):
		total = 0
		for num in range(0, number):
			if num % 3 == 0 or num % 5 == 0:
				total += num
						
		return total
	
	def fibonacci(self, number):
		previous_number = 0
		next_number = 0
		new_number = 0
		fibonacci_numbers = [1 , 2]
		
		for num in range(0 , number):
			new_number = 0
			previous_number = fibonacci_numbers[num]
			next_number = fibonacci_numbers[num + 1]
			new_number += previous_number + next_number
			fibonacci_numbers.append(new_number)

			self.fibonacci_list = fibonacci_numbers
		return fibonacci_numbers

	def sum_even_fibonacci(self):
		evenfibonacci_list = []
		oddfibonacci_list = []		
		sum_even = 0
		sum_odd = 0
		for num in self.fibonacci_list:
			if num % 2 == 0:
				evenfibonacci_list.append(num)
				if num > 4000000:
					pass
				else:
					print(num)
					sum_even += num
			else:
				oddfibonacci_list.append(num)
				if num > 4000000:
					pass
				else:
						sum_odd += num
				
		
		print(f"Even fibonacci list: \n{evenfibonacci_list} \n Odd finonacci list {oddfibonacci_list} \n The sum of even fibonacci number < 4000000 is: {sum_even} \n the sum of odd fibonacci numbers < 4000000 is: {sum_odd} \n")

	def the_prime_numbers(self, number):

		prime_numbers = []
		divisible_by_number = 0
		
		for new_number in range (2, number):
			divisible_by_number = 0
						
			for count in range (2, number+1):
				
				if (new_number % count) == 0:
					divisible_by_number+=1									
				else:
					pass
			
			if divisible_by_number == 1:
				prime_numbers.append(new_number)

		return prime_numbers

	def the_largest_prime_factor(self, number, prime_numbers):
		prime_factor = []
		# print(prime_numbers)

		for x in prime_numbers:
			if (number % x) == 0:
				prime_factor.append(x)

		print(prime_factor)