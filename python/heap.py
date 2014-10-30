#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Max Heap Abstract Datastructure
# Using Nodes and References to model a Binary Tree

import unittest
from copy import deepcopy

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
			Maxheap([3]).max_heapify(1)
		)
	
	def test_2(self):	
		self.assertEquals(
			[3,6,5,4],
			Maxheap([4,5,6]).max_heapify(1)
		)

	def test_3(self):
		self.assertEquals(
			[3, 6,4,5],
			Maxheap([6,4,5]).max_heapify(1)
		)

	def test_4(self):
		self.assertEquals(
			[5, 14, 8, 7, 2, 4],
			Maxheap([14, 4, 7, 2, 8]).max_heapify(2)
		)

	def test_5(self):
		self.assertEquals(
			[5, 14, 8, 7, 4, 2],
			Maxheap([14, 4, 7, 8, 2]).max_heapify(2)
		)

	def test_6(self):
		self.assertEquals(
			[5, 8, 14, 7, 2, 4],
			Maxheap([2,8,7,14,4]).max_heapify(1)
		)
	def test_7(self):
		self.assertEquals(
			[5, 14, 8, 7, 4, 2],
			Maxheap([4, 2, 7, 8, 14]).build_heap()
		)
	
	def test_8(self):
		maxheap = Maxheap([5,6,7,4,3,8,9,2,1])
		maxheap.build_heap()
		self.assertEquals(
			[9,8,7,6,5,4,3,2,1]
			, heapsort(maxheap)
		)


class Maxheap:
	
	def __init__(self, array = None):
		if array:
			self.array = [len(array)] + array
			self.heap = deepcopy(self.array)
		else:
			self.array = [0]
			self.heap = [0]
	

	def max_heapify(self, index):
		left = 2*index
		right = 2*index + 1

		if  left <= self.heap[0] and self.heap[left] > self.heap[index]:
			largest = left
		else:
			largest = index
		if right <= self.heap[0] and self.heap[right] > self.heap[largest]:
			largest = right	
		if largest != index:
			self.heap[index], self.heap[largest] = \
			self.heap[largest], self.heap[index]
			self.max_heapify(largest) 	 
	
		return self.heap

	def build_heap(self):
		for i in range(self.heap[0]/2, 0, -1):
			self.max_heapify(i)	
		return self.heap

def heapsort(heap):
	sorted_array = []
	while heap.heap[0] > 0:
		sorted_array.append(heap.heap[1])
		last = heap.heap[0]
		heap.heap[1], heap.heap[last] = heap.heap[last], heap.heap[1]
		# del heap.heap[-1]
		heap.heap[0] -= 1
		heap.max_heapify(1)
	return sorted_array


if __name__ == '__main__':
	unittest.main()