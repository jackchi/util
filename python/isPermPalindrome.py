import unittest
from collections import Counter

def isPermutePalindrome(string):
	isEven = not len(string) % 2
	cnt = Counter(string)
	if isEven:
		return reduce(lambda x, y: x and y % 2 == 0 , cnt.values(), True)
	else:
		# only one count can be odd
		odds = filter(lambda x: x % 2 != 0, cnt.values()) 
		return len(odds) == 1

class PermutePalindromeTest(unittest.TestCase):
	def test_even(self):
		self.assertTrue(isPermutePalindrome('wasrawwarsaw'))
		self.assertTrue(isPermutePalindrome('potsstop'))
		self.assertFalse(isPermutePalindrome('restroom'))
	def test_odd(self):
		self.assertTrue(isPermutePalindrome('viicc'))
		self.assertTrue(isPermutePalindrome('fewwe'))
		self.assertTrue(isPermutePalindrome('yakay'))
		self.assertFalse(isPermutePalindrome('ghost'))


if __name__ == '__main__':
	unittest.main()