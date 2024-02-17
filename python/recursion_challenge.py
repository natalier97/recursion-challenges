""" a factorial is the result of multiplying a sequence of descending numbers down to 0. Factorials are only defined for non-negative integer numbers. This definition includes zero. Though 0! is equal to 1, so treat it as an edge case."""
def factorial(x):
	if x == 0:
		return 1
	total = x * factorial(x-1)
	return total



'''A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward, such as madam or kayak. --> returns True or False if string is a palindrome'''

def palindrome(string):
	# last_index = len(string) - 1
	# i = last_index
	# reverse_string = ''
	# while i > - 1:
	# 	reverse_string += string[i] 
	# 	i -= 1
	# if reverse_string == string:
	# 	return True
	# else:
	# 	return False

	length = len(string)
	if length == 1:
		return True
	if string[0] != string[-1]:
		return False
	return palindrome(string[1:-1])


	# length = len(string)
	# i = length
	# reverse_string = ''
	# if len(string) <= 1: #base case bc if len of string = 1 (aka last leter in str) --> 1-1 = 0 so -1 means we dont have any other letters to add to reversed string
	# 	return reverse_string
	# reverse_string = string[-1] + palindrome(string[:(i -1)])
	# print(reverse_string)




'''92 bottles of beer on the wall, 92 bottles of beer.
Take one down and pass it around, 91 bottles of beer on the wall.
91 bottles of beer on the wall, 91 bottles of beer.
Take one down and pass it around, 90 bottles of beer on the wall.
...
...
...
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.'''

def bottles(num):
	bottle_plural = 'bottles' if num > 1 else "bottle"
	str = f"""{num} {bottle_plural} of beer on the wall, {num} {bottle_plural} of beer. 
				Take one down, pass it around, {num-1} bottles of beer on the wall."""
	if num == 1:
		return str
	return str, bottles(num-1)
	





"""A function that takes in a number and returns roman numerals equiv."""
def roman_num(num, priority_order_list = ["M", "D", "C", "L", "X", "V", "I"], output = ''):
	roman_numeral_to_number = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  };

	if len(priority_order_list) == 0:
		return ''
	if num < roman_numeral_to_number[priority_order_list[0]]:
		return roman_num(num, priority_order_list[1:], output)
	output += priority_order_list[0]
	num = num - roman_numeral_to_number[priority_order_list[0]]
	output = output + roman_num(num, priority_order_list)
	output= output.replace('DCCCC', 'CM')
	output = output.replace("CCCC", "CD")
	output = output.replace("XXXX", "XL")
	output = output.replace("VIIII", "IX")
	output = output.replace("IIII", "IV")
	return output

