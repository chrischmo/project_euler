def get_multiples_of_3and5(x): return x % 3 == 0 or x % 5 == 0
num_list = filter(get_multiples_of_3and5, range(1, 1000))

sum = 0
for number in num_list: sum += number
print sum
