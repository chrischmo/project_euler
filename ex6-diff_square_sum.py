def sum_of_squares(range):
	sum = 0
	for n in range: sum += n**2
	return sum

def square_of_sum(range):
	sum = 0
	for n in range: sum += n
	return sum**2

#print square_of_sum(range(1, 11)) - sum_of_squares(range(1, 11))

my_range= range(1, 101)
print my_range
print square_of_sum(my_range) - sum_of_squares(my_range)
