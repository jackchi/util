nums = set(['0', '1', '2', '3', '4', '5','6', '7', '8', '9']) 
def solution(S):
	stack = []
	for s in S: 
		if s in nums:
			stack.append(int(s))
		elif s == '+':
			try:
				r1 = stack.pop()
				r2 = stack.pop()
				stack.append(r1 + r2)
			except :
				return -1
		elif s == '*':
			try:
				r1 = stack.pop()
				r2 = stack.pop()
				stack.append(r1 * r2)
			except :
				return -1
	try:
		return stack.pop()
	except:
		return -1
				
print solution('13+62*7+*')