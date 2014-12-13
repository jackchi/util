class Tree:
	def __init__(self, x=0):
		self.x = x
		self.l = None
		self.r = None


def solution(T):
	if T:
		return pathAmp(T, T[0], T[0])
	else: 
		return 0

def pathAmp(T, minX, maxX):
	if not T:
		return maxX - minX
	else:
		minN = min(minX, T[0])
		maxN = max(maxX, T[0])
		return max(pathAmp(T[1], minN, maxN), pathAmp(T[2], minN, maxN))

T1 = (5, (8, (12, None, None), (2, None, None)), (9, (7, (1, None, None), None), (4, (3, None, None), None)))
T2 = (None)
T3 = (5, None, None)

print solution(T1)
print solution(T2)
print solution(T3)