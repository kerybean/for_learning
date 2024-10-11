def isPrime(number):
	"""Checks whether the number is prime or not"""
	if number < 2:
		return False
	else:
		for value in range(2, number//2+1):
			if number % value == 0:
				return False
		return True


def checkPrime(flag):
	"""Prints if number is prime"""
	if flag:
		print("Number is prime.")
	else:
		print("Number is NOT prime.")