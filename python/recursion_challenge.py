""" a factorial is the result of multiplying a sequence of descending numbers down to 0. Factorials are only defined for non-negative integer numbers. This definition includes zero. Though 0! is equal to 1, so treat it as an edge case."""
def factorial(x):
	if x == 0:
		return 1
	total = x * factorial(x-1)
	return total





def palindrome(string):
	pass

def bottles(num):
	pass

def roman_num(num):
	pass