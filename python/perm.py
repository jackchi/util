#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Python Recursion: String Permutation
# Recursion is made up of two cases
# - base case where it doesn't recurse
# - recursive case where it calls itself with different parameter
import sys

def perm(s):
	if len(s) <= 1:
		return s
	perms = []
	for sub_perm in perm(s[1:]):
		for i in range(len(s)):
			perms.append(sub_perm[:i] + s[0] + sub_perm[i:])
	return perms
	

def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: string [string2]'
		sys.exit(1)
	for word in args:	
		print '%s has these permutations:\n' % word + str(perm(word)).strip('[]')

if __name__ == '__main__':
	main()			