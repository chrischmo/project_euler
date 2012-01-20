def reverse_number(number):
	return int("".join(reversed(str(number))))

def find_palindromes(max_digits):
	palindromes = []
	numbers = range(1, 1*10**max_digits)
	
	for number in numbers:
		i  = 0
		while i < len(numbers):
			product = number * numbers[i]
			if product == reverse_number(product):
				palindromes.append(product)
			i += 1
	return palindromes

print max(find_palindromes(3))
