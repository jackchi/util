import unittest

# Board is a n x n matrix that is represented as a list of list
# [[1,2,3], [4,5,6], [7,8,9]]


def isFutoArray(array):
	n = len(array)
	r = range(1, n+1)
	for a in array:
		if a not in r:
			return False
		else:	
			r.remove(a)
	return True

def isFutoBoard(matrix):
	isFuto = True
	# check both rows & coluns
	for i, row in enumerate(matrix):
		if not isFuto:
			return False
		isFuto = isFuto and isFutoArray(row) and isFutoArray(column(matrix, i))
	return True	

def column(matrix, i):
    return [row[i] for row in matrix]		

def isFutoCond(matrix, conditions):
	""" conditions: [(rule)...]
	    rule: ((x1,y1), (x2,y2), lambda)
	    Checks all conditions on the board by applying lambda
    """
	result = True
	for cond in conditions:
		if not result:
			return False
		x1, y1 = cond[0][0], cond[0][1]
		x2, y2 = cond[1][0], cond[1][1]
		rule = cond[2]
		result = result and rule(matrix[x1][y1], matrix[x2][y2]) # applies 'rule' lambda
	return True

def isOrigFuto(origMatrix,testMatrix):
	"""
		origMatrx: nxn matrix list of list [[1,2,..,n],...]
				   None values for non-filled	
		Returns: True if non-empty values are in the correct coordinate in testMatrix
	"""
	result = True
	for x, row in enumerate(origMatrix):
		for y, column in enumerate(row):
			if not result:
				return False
			if origMatrix[x][y]:
				result = (testMatrix[x][y] == origMatrix[x][y])
	return result

def isFutoComplete(origMatrix, testMatrix):
	return isFutoBoard(testMatrix) and isOrigFuto(origMatrix, testMatrix)

class FutoTest(unittest.TestCase):

	def test_futoArray(self):
		self.assertTrue(isFutoArray([1,2,3,4])) 
		self.assertTrue(isFutoArray([1,2,3,4,5]))
		self.assertFalse(isFutoArray([2,3,4,5])) 
		self.assertFalse(isFutoArray([1,2,3,3,5])) 

	def test_column(self):
		self.assertEqual([2,4], column([[1,2], [3,4]], 1))
		self.assertEqual([1,4,7], column([[1,2,3], [4,5,6], [7,8,9]], 0))

	def test_isFutoBoard(self):
		board1 = [[3,4,1,2], [1,3,2,4], [4,2,3,1], [2,1,4,3]]
		board2 = [[3,4,2,1], [1,3,2,4], [4,2,3,1], [2,1,4,3]]
		self.assertTrue(isFutoBoard(board1))	# correct board
		self.assertFalse(isFutoBoard(board2))   # column 3,4 repeats

	def test_isFutoCond(self):
		gt = lambda x,y: x>y
		lt = lambda x,y: x<y
		board1 = [[3,4,1,2], [1,3,2,4], [4,2,3,1], [2,1,4,3]]
		conditions = [((0,0),(0,1),lt),
					  ((1,1),(1, 2),gt),
					  ((0,2),(1,2),lt),
					  ((1,3),(2,3),gt)]
		self.assertTrue(isFutoCond(board1, conditions))			  		

	def test_isOrigFuto(self):
		board = [[1,2],[3,4]]
		orig1 = [[1,None],[None,None]]
		orig2 = [[1,None],[None,4]]
		orig3 = [[1,None],[None,2]]
		self.assertTrue(isOrigFuto(orig1, board))
		self.assertTrue(isOrigFuto(orig2, board))
		self.assertFalse(isOrigFuto(orig3, board))

	def test_isFutoComplete(self):
		board1 = [[3,4,1,2], 
				  [1,3,2,4], 
				  [4,2,3,1], 
				  [2,1,4,3]]		
		orig = [[None,None,None,None],
				[None,None,None,None],
				[None,None,None,None],
				[2,None,None,None]]
		self.assertTrue(isFutoComplete(orig,board1))
		
if __name__ == '__main__':
    unittest.main()