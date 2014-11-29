#!/usr/bin/python
# https://github.com/jackchi/util/python/sorting
# Copyright 2014 Jack Chi (jack@jack-chi.com)

# Given a rotated sorted array
# Find the index of the target integer in the array

import unittest

def isRotated(array):
	return array[-1] < array[0]

def rotatedSortedSearch(array, target, lower, upper):
	"""perform a Binary Search with adapted rotation"""
	search_range = upper - lower
	mid = search_range / 2 + lower
	if (search_range < 0):
		print 'Not Found'
		raise IndexError('Limits reversed!')
	if target== array[mid]:
		print 'found! %d at index %d' % (target, mid)
		return mid
	if isRotated(array): 
		if target <= array[upper]:
			print 'searching...' + str(array[mid+1:upper])
			return rotatedSortedSearch(array, target, mid+1, upper)
		else:
			print 'searching...' + str(array[lower:mid])
			return rotatedSortedSearch(array, target, lower, mid-1)
	else:
		if target > array[mid]:
			print 'searching...' + str(array[mid+1:upper+1])
			return rotatedSortedSearch(array, target, mid+1, upper)
		else:
			print 'searching...' + str(array[lower:mid])
			return rotatedSortedSearch(array, target, lower, mid-1)

# print rotatedSortedSearch([20,25,1,2,3,4,5,6,7], 25, 0, 8)
# print rotatedSortedSearch([20,25,1,2,3,4,5,6,7], 24, 0, 8)

class RotatedSearchTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.noRotate = [1,2,3,4,5,6,7,9]
		cls.rotate = [10,12,14,0,2,4,6,8]

	def test_noRotation_found(self):
		self.assertEquals(rotatedSortedSearch(self.noRotate, 6, 0, len(self.noRotate)-1),5) # 6 is found at index 5
	
	def test_noRotation_notFound(self):
		self.assertRaises(IndexError, rotatedSortedSearch, self.noRotate, 100, 0, len(self.noRotate)-1)

	def test_rotation_found(self):
		self.assertEquals(rotatedSortedSearch(self.rotate, 8, 0, len(self.rotate)-1), 7)
		self.assertEquals(rotatedSortedSearch(self.rotate, 12, 0, len(self.rotate)-1), 1)

	def test_rotation_notFound(self):
		self.assertRaises(IndexError, rotatedSortedSearch, self.rotate, 44, 0, len(self.rotate)-1)

if __name__ == '__main__':
	unittest.main()