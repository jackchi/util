#!/usr/bin/python
# https://github.com/jackchi/util/python/sorting
# Copyright 2014 Jack Chi (jack@jack-chi.com)

# Max Heap Abstract Datastructure
# Using Nodes and References to model a Binary Tree

import unittest
from maxheap import *

class MaxheapTest(unittest.TestCase):
	
	def test_0(self):
		# constructor tests
		self.assertEquals(
			[0], 
			Maxheap().heap)
		self.assertEquals(list, type(Maxheap().heap))
		
	def test_1(self):
		# max_heapify test
		self.assertEquals(
			[1, 3],
			max_heapify([1,3], 1)
		)
	
	def test_2(self):	
		self.assertEquals(
			[3,6,5,4],
			max_heapify([3,4,5,6], 1)
		)

	def test_3(self):
		self.assertEquals(
			[3,6,4,5],
			max_heapify([3,6,4,5], 1)
		)

	def test_4(self):
		self.assertEquals(
			[5, 14, 8, 7, 2, 4],
			max_heapify([5, 14, 4, 7, 2, 8], 2)
		)

	def test_5(self):
		self.assertEquals(
			[5, 14, 8, 7, 4, 2],
			max_heapify([5, 14, 4, 7, 8, 2], 2)
		)

	def test_6(self):
		self.assertEquals(
			[5, 8, 14, 7, 2, 4],
			max_heapify([5,2,8,7,14,4], 1)
		)

	def test_7(self):
		self.assertEquals(
			[5, 14, 8, 7, 4, 2],
			build_heap([4, 2, 7, 8, 14])
		)
	
	def test_8(self):
		self.assertEquals(
			[9,8,7,6,5,4,3,2,1]
			, heapsort([5,6,7,4,3,8,9,2,1])
		)


if __name__ == '__main__':
	unittest.main()