#!/usr/bin/python

import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''

	try:
		# getopt.getopt(args, options[, long_options])
		opts, args = getopt.getopt(argv, "hio:", ["ifile=", "ofile"])
	except getopt.getoptError:
		print 'cet.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'cet.py -i <inputfile> -o <outputfile>'
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "-ofile"):
			outputfile = arg

if __name__ == "__main__":
	main(sys.argv[1:])

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
