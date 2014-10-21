#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Python Recursion Factorial Practice
# Recursion is made up of two cases
# - base case where it doesn't recurse
# - recursive case where it calls itself with different parameter

import sys

def factorial(number):
	""" n! = n*(n-1)! 
		0! = 0
		-1! = ValueError
	"""
	if(number > 1):
		return number * factorial(number-1)
	elif(number < 0):
		raise ValueError("factorial() not defined for negative values")
	else:
		return 1

def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: number1 [number2]'
	for number in args:
		print '%s! = %d' % (number, factorial(int(number)))		

if __name__ == '__main__':
	main()