#!/usr/bin/python
# https://github.com/jackchi/util/python
# Copyright 2014 Jack Chi

# Max Heap Abstract Datastructure
# Building up for Heap Sort

from copy import copy

class Maxheap:
	""" 
	Maxheap is an array of values that is visualized as
	an nearly complete Binary Tree where:
		- parent value is always larger than child value
		
		Given a Node at index i:
		- parent of i is i/2
		- left child of i is 2*i
		- right child of i is 2*i+1
		
		Given a heap of size n: 
		- All leaf nodes are from n/2 ... n
		- # of Levels in the tree is ln(n)
	"""

	def __init__(self, array = None):
		if array:
			self.heap = build_heap(array)
		else:
			self.heap = [0]
	# TODO: Implement priority queue functions
	
	def extract_max():
		pass

	def insert_value(value):
		pass		
	
def heapsort(array):
	"""
		Maximum is always on top
		extract and heapify on the first index 
	"""
	sorted_array = []
	heap = build_heap(array)
	while heap[0] > 0:
		sorted_array.append(heap[1])
		last = heap[0]
		heap[1], heap[last] = heap[last], heap[1]
		# del heap.heap[-1]
		heap[0] -= 1
		max_heapify(heap, 1)
	return sorted_array


def build_heap(array):
	"""
	Build a max heap from an array
	"""
		array = [len(array)] + array
		for i in range(array[0]/2, 0, -1):
			max_heapify(array, i)	
		return copy(array)

def max_heapify(array, index):
		"""
		Subroutine to help with build_heap and heapsort
		Make everything underneath this particular index a heap
		"""
		left = 2*index
		right = 2*index + 1

		if  left <= array[0] and array[left] > array[index]:
			largest = left
		else:
			largest = index
		if right <= array[0] and array[right] > array[largest]:
			largest = right	
		if largest != index:
			array[index], array[largest] = \
			array[largest], array[index]
			max_heapify(array, largest) 	 
			
		return array