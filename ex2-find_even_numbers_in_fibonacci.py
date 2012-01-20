def fibonacci(max_number):
	sequence = []
	while True:
		if sequence == []: 
			sequence.append(1)
			sequence.append(2)
		else:
			candidate = sequence[-1] + sequence[-2]
			if candidate <= max_number: sequence.append(candidate)
			else: return sequence


even_fibonacci = filter(lambda x: x%2 == 0,  fibonacci(4000000))
sum = 0
for number in even_fibonacci: sum += number
print "Even Fibonacci numbers: " + str(even_fibonacci)
print "Sum: " + str(sum)
