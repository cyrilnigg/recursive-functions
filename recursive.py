#Various recursive functions

def factorial(n):
	'''
	Takes an integer greater than 0
	Returns factorial value recursively
	'''
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
		
		
def fib(n):
	'''
	Takes an integer greater than 0
	Returns Fibonacci value
	'''
	assert type(n) == int and n >= 0
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
		
		
def Q(n):
	'''
	Erratic recursive function defined in Gobel, Escher, Bach
	'''
	assert type(n) == int and n > 0
	if n == 1 or n == 2:
		return 1
	else:
		return Q(n - Q(n - 1)) + Q(n - Q(n - 2))
		
		
def sum(num_list):
	'''
	Takes a list of numbers and sums them recursively
	'''
	if len(num_list) == 1:
		return num_list[0]
	else:
		return num_list[0] + sum(num_list[1:])

def factorInRange(k, n):
	'''
	Helper function for primeTest
	Checks numbers between 2 and n
	'''
	if k >= n:
		return False
	elif n % k == 0:
		return True
	else:
		return factorInRange(k+1, n)
	
def primeTest(n):
	'''
	Returns True if number is prime using recursion
	Uses the factorInRange
	'''
	assert type(n) == int and n >= 0
	return n > 1 and not factorInRange(2, n)
	