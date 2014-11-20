def multTable(x,y):
	line = range(x+1)
	print line
	for m in range(1,y+1):
		t= map(lambda s: s*m, line)
		t[0] = m
		print t


