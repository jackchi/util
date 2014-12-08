#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Binary Tree Nodes Representation
# Using Nodes and References to model a Binary Tree

import Queue


def isLeaf(node):
	return not node.getLeftChild() and not node.getRightChild()

def insert(key, leftLine, rightLine, line):
	print "%d %s %d %d" % (line, key, leftLine, rightLine)
	return line

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

	def insert (self, newNode):
		prev = None
		curr = self
		while curr:
			prev = curr
			if newNode < curr.key:
				curr = curr.leftChild
			else:
				curr = curr.rightChild	
		if newNode < prev.key:
			prev.leftChild = BinaryTree(newNode)
		else:
			prev.rightChild = BinaryTree(newNode)


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

	def DFPrint(self, line=0):
		if isLeaf(self):
			line+=1
			return insert(self.key, -1, -1, line)		
		else: 
			line+=1
			return insert(self.key, self.getLeftChild().DFPrint(line) if self.getLeftChild() else -1, 
				self.getRightChild().DFPrint(line) if self.getRightChild() else -1, line) 


