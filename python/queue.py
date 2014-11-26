#!/usr/bin/python

# Udacity's Python Engineering Interview Question
# Implement the push/pop operation of a queue only using
# stack operations

import unittest 

class Q:
	def __init__(self, elements = []):
		self.stack1 = elements
		self.stack2 = []

	def push(self, element):
		self.stack1.append(element)

	def pop(self):
		if not self.stack2: 
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()

class QTest(unittest.TestCase):

	def test_empty_constructor(self):
		q = Q()
		self.assertRaises(IndexError, q.pop)

	def test_constructor(self):
		q = Q(['a','b','c','d'])
		self.assertEqual('a', q.pop())
		self.assertEqual('b', q.pop())
		self.assertEqual('c', q.pop())
		self.assertEqual('d', q.pop())

	def test_multiple_push_pop(self):
		q= Q()
		q.push(1)
		q.push(2)
		q.push(3)
		self.assertEqual(1, q.pop())
		self.assertEqual(2, q.pop())
		q.push(4)
		self.assertEqual(3, q.pop())
		self.assertEqual(4, q.pop())
		q.push(5)
		self.assertEqual(5, q.pop())
		self.assertRaises(IndexError, q.pop)


if __name__ == '__main__':
    unittest.main()