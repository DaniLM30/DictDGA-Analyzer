#!/usr/bin/env python
#Copyright (c) 2021 Daniel Lopez
#All rights reserved.

from wordsegment import load, segment

def dga_analyzer():
	#Open file
	with open("dga_testing.txt") as f:
		domains = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
    # also remove TLDs and annoying hyphens in AGDs
	domains = [x.strip().split(".")[0].replace('-','') for x in domains]
    
	#For loop to analyze domains
	load()

	wordlist = []
	for domain in domains:
		segmentation = segment(domain)

		for word in segmentation:
			if word not in wordlist:
				wordlist.append(word)
	
	print(sorted(wordlist))
	print(len(wordlist))

dga_analyzer()