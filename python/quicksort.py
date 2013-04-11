#! /usr/bin/python
# AUTHOR: Jack Chi
# QuickSort

import pprint

# Sort a list of ints


def quicksort(arr):
	if not arr:
		return []
	pivot = arr[0]
	lesser = quicksort([x for x in arr[1:] if x < pivot])
	greater = quicksort([x for x in arr[1:] if x >= pivot])
	return lesser + [pivot] + greater

while True:
	b = True
	while b:
		try:
			s = raw_input("Enter Some Numbers Separated by spaces:")
			numbers = map(int, s.split())
			b = False
			break 
		except:
			print ("Wrong Input!")

		sn= quicksort(numbers)
		pprint.pprint(sn)

		quit = str(raw_input("Continue(y/n)?"))
		if quit =='y' :
			print ("ok!")
		elif quit == 'n' :
			break
