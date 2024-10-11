def isPrime(number):
	"""Checks whether the number is prime or not"""
	if number < 2:
		return False
	else:
		for value in range(2, number//2+1):
			if number % value == 0:
				return False
		return True