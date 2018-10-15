#!/usr/bin/python3
import re

infile  = open("Python_08.fasta", "r")

wordbook = {}

geneID = ''
seq = ''

for line in infile:
	line = line.rstrip()
	if not  re.search(r"^>", line):
		seq += line
	else:
		geneID = re.search(r"^>(\w+) .*$", line)
		wordbook[geneID] = seq
wordbook[geneID] = seq

for key in wordbook:
	sequence = list(wordbook[key])
	for nuc in sequence:
		if wordbook[geneID][nuc] not in wordbook:
			wordbook[geneID][nuc] = 1
		else:
			wordbook[geneID][nuc] += 1
for gene in sorted(wordbook):
	for nuc in sorted(wordbook[nuc]):
		print (gene,nuc,wordbook[gene][nuc]) 
		
		


