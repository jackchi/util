#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Binary Tree Nodes Representation
# Using Nodes and References to model a Binary Tree

import Queue
import unittest

class BinaryTreeTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.tree = BinaryTree('root')

	@classmethod	
	def tearUpClass(self):
		del self.tree

	def test_1(self):
		self.assertIsInstance(
			self.tree,
			BinaryTree
		)

		self.assertIsNone(self.tree.getLeftChild())

		self.assertIsNone(self.tree.getRightChild())

	def test_2(self):
		self.tree.insertLeft('left')
		self.tree.insertRight('right')

		self.assertEqual(
			self.tree.getLeftChild().key, 'left')
		self.assertEqual(
			self.tree.getRightChild().key, 'right')

	def test_3(self):
		self.tree.getLeftChild().insertLeft('leftmost')
		self.tree.getRightChild().insertRight('rightmost')

		self.assertIsNone(self.tree.BFSearch('nothing'))
		self.assertEqual(
			self.tree.BFSearch('leftmost').key, 
			'leftmost')
		self.assertEqual(
			self.tree.BFSearch('rightmost').key, 
			'rightmost')	

	def test_4(self):
		self.tree.setRootVal('newRoot')

		self.assertEqual(
			self.tree.getRootVal(), 'newRoot'
			)	
	
	def test_5(self):
		self.assertIsNone(self.tree.DFSearch('nothing again'))
		self.assertEqual(
			self.tree.DFSearch('newRoot').key, 
			'newRoot')

	def test_6(self):	
		self.assertEqual(BinaryTree.getHeight(None), 0)
		self.assertEqual(BinaryTree.getHeight(self.tree), 3)
		self.assertEqual(BinaryTree.getHeight(BinaryTree('one')), 1)

class BinaryTree:

	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if not self.leftChild:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if not self.rightChild:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getLeftChild(self):
		return self.leftChild		

	def getRightChild(self):
		return self.rightChild		

	def setRootVal(self, val):
		self.key = val

	def getRootVal(self):
		return self.key

	@staticmethod	
	def getHeight(node):
		if node == None:
			return 0
		else: 
			return max(BinaryTree.getHeight(node.getLeftChild()), 
				    BinaryTree.getHeight(node.getRightChild())) + 1	

	def BFSearch(self, target):
		""" Using a Queue to iteratively search adjacent nodes
		before traversing down the tree
		"""

		queue = Queue.Queue()
		queue.put(self)
		
		while not queue.empty():
			r = queue.get()
			if (r.key == target):
				return r
			if r.leftChild != None:
				queue.put(r.leftChild)
			if r.rightChild != None:
				queue.put(r.rightChild)	
		return None

	def DFSearch(self, target):
		""" Using recursion to search leftmost depth nodes
		before traversing across adjacent nodes
		"""
		if self.key == target:
			return self
		else:
			if not self.getLeftChild():
				self.getLeftChild().DFSearch(target)
			if not self.getRightChild():
				self.getRightChild().DFSearch(target)

if __name__ == '__main__':
    unittest.main()
				
