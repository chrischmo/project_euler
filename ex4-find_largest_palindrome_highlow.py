def reverse_number(number):
	return int("".join(reversed(str(number))))

def find_palindromes(max_digits):
	"""Improves on first version in that it goes from high to low numbers"""
        palindromes = []
        numbers = range(1, 1*10**max_digits)
	numbers.reverse()

        for num1 in numbers:
                for num2 in numbers:
                        if num1*num2 == reverse_number(num1*num2):
                                palindromes.append(num1*num2)
        
	return palindromes

print max(find_palindromes(3))
