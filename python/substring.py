#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Python String manipulation practice
# A Substring is a segment of the original word broken down to len(word)...len(1)

import sys

def toUniqueOrderList(seq):
	"""Given a sequence of strings return the unique sequence whilst preserving order"""
	seen = set()
	seen_add = seen.add
	return [ x for x in seq if not (x in seen or seen_add(x))]

def toSubString(word):
	"""Given a word returns a list of unique sub strings"""
	# Retruns an array of unique substrings
	WORD_LENGTH = len(word)
	unique_substr = []
	
	# find all sub length strings
	for sub_length in range(WORD_LENGTH,0,-1):
		# word starting index
		sl = [word[i:i+sub_length] for i in range(0, WORD_LENGTH) if (i + sub_length) <= WORD_LENGTH]
		unique_substr+= sl

	return toUniqueOrderList(unique_substr)		

def longestsubstr(word1, word2):
	"""Given 2 words, return the longest substring"""
	short_word = word1 if len(word1) < len(word2) else word2 
	long_word = word1 if len(word1) >= len(word2) else word2
	short_word_substring = toSubString(short_word)
	
	for w in short_word_substring:
		if (~long_word.find(w)):
 			return w

def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: [--substr] [--longest] string1 [string2]'
		sys.exit(1)

	substr = False
	if(args[0] == '--substr'):
		substr = True
		del args[0]

	longest = False
	if(args[0] == '--longest'):
		longest = True
		del args[0]


	if substr:	
		for word in args:	
			print 'Word: %s has substring:\n' % (word) + str(toSubString(word))

	if longest:		
		tempLongest = longestsubstr(args[0], args[1])
		for w in args[2:]:
			tempLongest = longestsubstr(w, tempLongest)
		print "The longest substring is %s" % tempLongest	
			
if __name__ == '__main__':
	main()