#!/usr/bin/python

import sys
from collections import Counter

class Doc:
  # word count in Doc
	wordCount = 0
	
	# word position in Doc
	# key : value
	# key is the word
	# value stores the position at which the word occurs
	# frequent is the length of the value
	wordPos = {}
	
	def tokenizeDoc(self, filename):
		fileDoc = open(filename, 'r')
		print "Name of the file: ", fileDoc.name
		
		for w in fileDoc.read().split():
			self.wordCount += 1
			if w in self.wordPos:
				self.wordPos[w].append(self.wordCount)
			else:
				self.wordPos[w] = [self.wordCount]
		fileDoc.close()
		
	def printDoc(self):
		print "# of words" , self.wordCount
		for word, times in self.wordPos.items():
		    print (word + " appears ", len(times), " times at positions ", times)
	def wordFreq(self, word):
		return len(self.wordPos[str(word)])
	
	def wordPosition(self, word):
		return self.wordPos[str(word)]

while True:
	filename = str(raw_input("Enter name of your file (or 'q' to quit): "));
	if filename == "q" :
		break
	else:
		doc1 = Doc()
		doc1.tokenizeDoc(filename)
		doc1.printDoc()
