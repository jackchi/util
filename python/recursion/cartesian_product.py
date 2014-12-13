""" 
	Cartesian Product of a Tuples gives a list of Tuples
	e.g:
		A = [1,2,3]
		B = [4,5]
		C = [6,7,8]
	A * B * C = 
	[ (1,4,6), (1,4,7), (1,4,8)
	  ...
	  (3,5,6), (3,5,7), (3,5,8)
	]	 
"""
# Product Function gives the Cartesian Product in a List of Tuples
# (y,) is a Tuple with one item
def product (l):
    if not l: 
    	return [()]
    return [x + (y,) for x in product(l[:-1]) for y in l[-1]]

import unittest

class CartesianProductTest(unittest.TestCase):

	def setUp(self):
		self.singleArray = [[1], [2], [3]]
	def test_emptyList(self):
		self.assertEqual([()], product([]))
	def test_singleArray(self):
		self.assertEqual([(1,2,3)], product(self.singleArray))
		
if __name__ == '__main__':
	unittest.main()

