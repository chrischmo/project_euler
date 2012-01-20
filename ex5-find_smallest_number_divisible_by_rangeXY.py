def is_evenly_divisible(number, range):
	"""Takes a number and checks if it is evenly divisble by all numbers in a given range"""
	for divisor in range:
		if number % divisor != 0: 
			return False
	return True

#print is_evenly_divisible(2520, range(1, 11))

def find_smallest(range):
	"""Finds the smallest number evenly divisible by all numbers in a given range"""
	number = max(range)**2 # is there a better way to optimize this?
	while True:
		if is_evenly_divisible(number, range): 
			return number
		number += 1
		

print find_smallest(range(1, 21))
