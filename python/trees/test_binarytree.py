import unittest
from binarytree import *

class BinaryTreeTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.tree = BinaryTree('root')

	@classmethod	
	def tearUpClass(self):
		del self.tree

	def test_instance(self):
		self.assertIsInstance(
			self.tree,
			BinaryTree
		)

	def test_one_level_insert(self):
		self.tree.insertLeft('left')
		self.tree.insertRight('right')

		self.assertEqual(
			self.tree.getLeftChild().key, 'left')
		self.assertEqual(
			self.tree.getRightChild().key, 'right')

	def test_insertion(self):
		b = BinaryTree(10)
		b.insert(8)
		b.insert(20)
		b.insert(22)
		b.insert(12)
		b.insert(1)
		b.DFPrint()
		self.assertEqual(b.getRightChild().key, 20)

	def test_4(self):
		self.tree.setRootVal('newRoot')

		self.assertEqual(
			self.tree.getRootVal(), 'newRoot'
			)	
		
	def test_7(self):
		b= BinaryTree("Root")
		b.insertLeft("leftmost")
		b.insertRight("right")
		b.insertLeft("left")
		self.assertFalse(isLeaf(b))
		self.assertTrue(isLeaf(b.getRightChild()))
		b.DFPrint()

if __name__ == '__main__':
    unittest.main()
