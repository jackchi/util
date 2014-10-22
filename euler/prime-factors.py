#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Python Math Practice
# Find the greatest Prime Factor less than a given number

import math
import sys

def primesUpTo(n):
	""" Using Sieve of Eratosthenes to find all primes less than n
		http://www.algorithmist.com/index.php/Prime_Sieve_of_Eratosthenes
	"""
	# [False, False] for 0, 1 which are not primes
	primes = [False, False] + list((True,)*(n-1))
	sqrt = int(math.sqrt(n)) 
	for i in range(2, sqrt+1):
		if(primes[i]):
			for j in range(1, n):
				num = j*i
				if (i**2 <= num <= n):
					primes[num] = False
				
	return [a for a in range(len(primes)) if primes[a]]

def greatestPrimeFactor(n):
	primes = primesUpTo(int(math.sqrt(n)))
	print primes
	for p in reversed(primes):
		if (n % p == 0):
			return p

# print greatestPrimeFactor(600851475143)

def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: integer'

	target = int(args[0])	
	print greatestPrimeFactor(target)	

if __name__ == '__main__':
	main()	