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