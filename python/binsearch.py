import sys

def binarySearch(array, target):
	array = sorted(array)
	print 'searching...' + str(array) 
	return binarySearchLimits(sorted(array), target, 0, len(array)-1, 0)

def binarySearchLimits(array, target, lower, upper, level):	
	# target not in array
	search_range = upper - lower
	mid = (search_range / 2) + lower
	if (search_range < 0):
		raise IndexError('Limits reversed!')
	print 'Level %d mid is %d' %(level, array[mid])
	if (array[mid] == target):
		print 'found! %d at index %d' % (target, mid)
		return mid
	elif (array[mid] > target):
		print 'searching...' + str(array[lower:mid]) 
		return binarySearchLimits(array, target, lower, mid-1, level+1)
	elif (array[mid] < target):
		print 'searching...' + str(array[mid+1:upper+1])
		return binarySearchLimits(array, target, mid+1, upper, level+1)
			 

def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: python binsarch.py array integer'
		sys.exit(1)
	array = [int(a) for a in args[0].strip('[]').split(',')] # string to array
	target = int(args[1])	
	binarySearch(array, target)
			
if __name__ == '__main__':
	main()