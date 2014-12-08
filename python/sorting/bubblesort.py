#! usr/bin/python 
# sort from smallest to largest
import random
from random import choice
import timeit

def srand(start, stop):
	try:
		l = range(start, stop)
		random.shuffle(l)
		return l
	except StandardError:
		print "Standard Error"

def bubblesort(array):
	nums= list(array)
	print "Original List" + str(array)
	for i in range(len(nums)):
		for j in range(i+1,len(nums)):
			if array[j] < array[i]:
				array[j], array[i] = array[i], array[j]

	print "Altered List:" + str(array)

a = srand(2,40)
