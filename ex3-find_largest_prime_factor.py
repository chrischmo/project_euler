import math


def is_prime(n):
        n = abs(n)
        if n <=1: return False
        elif n == 2: return True
        else:
                for x in range(3, int(math.sqrt(n))+1, 2): #step is 2 because we only want odd divisors
                        if n % x == 0: return False
                return True


def get_prime_factors(number):
	prime_numbers = []
	prime_factors = []

        if is_prime(number):
                prime_factors.append(number)

        print "== Beginning search for prime numbers =="

	prime_candidate = number/2    # is there a better way to limit the range?
	if prime_candidate % 2 == 0: prime_candidate += 1    # we only want odd numbers
	while prime_candidate > 1:
		if is_prime(prime_candidate): prime_numbers.append(prime_candidate)
		prime_candidate -= 2 #   we only want to examine odd numbers 

	print "== Now checking if the primes found are divisors of " + str(number) + " =="

	for factor_candidate in prime_numbers:
		if number % factor_candidate == 0: 
			prime_factors.append(factor_candidate)

	return prime_factors

#print max(get_prime_factors(13195))
print max(get_prime_factors(600851475143))


def get_largest_prime_factor(number):
	number = abs(number)
	if is_prime(number): 
		return number
	else:
        	candidate = number/2 
        	while candidate > 1:
                	if (number % candidate == 0 and is_prime(candidate)): return candidate
                	else: candidate -= 1
		return 0

#print is_prime(600851475143)
#print get_largest_prime_factor(13195)
#print get_largest_prime_factor(600851475143)
