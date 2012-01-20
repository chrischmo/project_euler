import math

def is_prime(n):
	n = abs(n)
	if n <=1: return False
	elif n == 2: return True
	else:
		for x in range(3, int(math.sqrt(n))+1, 2): #step is 2 because we only want odd divisors
			if n % x == 0: return False
		return True

def find_prime(n):
	"""Find the nth prime number"""
	counter = 1
	candidate = 3
	latest_prime = 2
	while counter < n:
		if is_prime(candidate): 
			latest_prime = candidate
			counter += 1
                        #print "prime no. " + str(counter) + ": " + str(latest_prime)
		candidate += 2 # all primes except 2 (already registered) are odd 
	return latest_prime

print find_prime(100010000)
