import unittest, sys, random, math

def exp(x, y):
	if y == 0:
		if x == 0:
			return 0
		elif x > 0:
			return 1
		elif x < 0: 
			return -1
	else: 
		root = exp(x, y/2)
		return root * root * x if y % 2 else root * root

class ExpTest(unittest.TestCase):
	def test_power_of_zero_0_base(self):
		self.assertEqual(0, exp(0,0))

	def test_power_of_zero_pos_base(self):
		# random integer between 0 and maximum integer
		self.assertEqual(1, exp(random.randint (0, sys.maxint), 0)) 

	def test_power_of_zero_neg_base(self):
		# random negative integer between min and -1
		self.assertEqual(-1, exp(random.randint (-sys.maxint, -1), 0))	

	def test_power_of_zero_any_base(self):
		self.assertEqual(0, exp(0, random.randint(-sys.maxint, sys.maxint)))

	def test_power_of_one(self):
		itself = random.randint (-sys.maxint, sys.maxint)
		self.assertEqual(itself, exp(itself, 1))

	def test_power_any(self):
		base = random.randint (0, 25)
		ex = random.randint (0, 10)
		self.assertEqual(base**ex, exp(base, ex))

if __name__ == '__main__':
	unittest.main()