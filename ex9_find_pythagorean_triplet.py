import math

def find_py_triplet(abc_sum):
	"""Finds a Pythagorean triplet for which a + b + c = sum(a, b, c).
	   According to wikipedia, any triplet can be formed
	   with the following formulas:
	   a = u**2 - v**2
	   b = 2*u*v
	   c = u**2 + v**2
	   where u and v are natural numbers and u > v
	   => 2*(u**2) + 2*u*v = sum(a, b, c)"""

	u = int(math.sqrt(abc_sum)) + 1

	while u > 2:
		v = 1
		while v < u:
			if 2*(u**2) + 2*u*v == abc_sum:
				a = u**2 - v**2
				b = 2*u*v
				c = u**2 + v**2
				return (a, b, c)
			v += 1
		u -= 1
	return (0, 0, 0)

def checkpy(abc_tuple):
	"""Checks if a given triplet (a, b, c) fulfills a² + b² = c²"""
	return abc_tuple[0]**2 + abc_tuple[1]**2 == abc_tuple[2]**2

def multiply_triplet(triplet):
	"""Looks inside a tuple or list and multiplies its numbers"""
	product = 1
	for n in triplet: product *= n
	return product

triplet = find_py_triplet(1000)
print checkpy(triplet)
print multiply_triplet(triplet)
