import math

def is_prime(n):
        n = abs(n)
        if n <=1: return False
        elif n == 2: return True
        else:
                for x in range(3, int(math.sqrt(n))+1, 2): #step is 2 because we only want odd divisors
                        if n % x == 0: return False
                return True

def get_primes(limit):
	"""Returns all prime numbers below limit."""
	primes = []
	if limit >3:
		primes = [2, 3]
		candidate = 5
		while candidate < limit:
			#if candidate % 100001 == 0: print "Evaluating " + str(candidate)
			if is_prime(candidate): primes.append(candidate)
			candidate += 2
	else: 
		primes = []
		for candidate in range(1, limit):
			if is_prime(candidate): primes.append(candidate)

	return primes

def sum_up(numbers):
	"""Expects an iterable object with numbers in it and sums them up."""
	sum = 0
	for number in numbers: sum += number
	return sum

print sum_up(get_primes(2000000))
