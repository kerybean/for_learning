def factorial(number):
	"""Returns number's factorial"""
	fact = 1

	for value in range(1, number+1):
		fact = fact * value

	return fact


