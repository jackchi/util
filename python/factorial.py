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

def allFactorials(number):
	""" Using a wrapper to initialized the Array """
	results = [1] if number == 0 else list((0,)*(number+1))
	doAllFactorials(number, 0, results)
	return results

def doAllFactorials(number, level, results):
	"""n!! = [n!, (n-1)!, (n-2)!, ..., 0!] """
	if(number >= 1):
		results[level] = number * doAllFactorials(number-1, level+1, results)
		return results[level]
	else:
		results[level] = 1
		return 1

def main():
	args = sys.argv[1:]

	AllFacts = False
	if (args[0] == '--all'):
		AllFacts = True
		del args[0]
	
	if not args:
		print 'usage: --all number1 [number2]'
		sys.exit(1)
			
	if AllFacts:
		for number in args:
			print '%s! has these levels:\n' + str(allFactorials(int(number)))
	else:
		for number in args:
			print '%s! = %d' % (number, factorial(int(number)))		

if __name__ == '__main__':
	main()