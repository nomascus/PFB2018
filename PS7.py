#!/usr/bin/perl
import re

# 1
infile = open("Python_07_nobody.txt", "r")

counter = 1
for line in infile:
	for found in re.finditer("Nobody", line):
		start = found.start() +1
		end = found.end() +1
		print("Nobody: Line", counter,str(start)+"-"+str(end))
	counter += 1
# 2
infile = open("Python_07_nobody.txt", "r")
outfile = open("Pinkerton.txt", "w")

for line in infile:
	line =line.rstrip()
	line = re.sub(r"Nobody", "Pinkerton",line)
	#print(line)
	outfile.write(line+"\n")
# 3

infile = open("Python_07.fasta", "r")

for line in infile:
	header  = re.search(r"^>", line)
	print(header)

# 4

infile = open("Python_07.fasta", "r")

for line in infile:
	if re.search(r"^>", line):
		for found in re.finditer(r"^>(\S*)? (.*)$", line):
			ID = found.group(1)
			desc = found.group(2)
			print("{:s}: {:s}\t{:s}: {:s}".format("id",ID,"desc",desc)) 

# 5

infile = open("Python_07.fasta", "r")

# 6

infile = open("Python_07_ApoI.fasta", "r")

for line in infile:
	if not re.search(r"^>", line):
		for found in re.findall(r"[A|G]AATT[C|T]", line):
			print (found)

# 7

infile = open("Python_07_ApoI.fasta", "r")

header = ''
seq = ''
wordbook = {}

for line in infile:
	line = line.rstrip()
	if not re.search(r"^>", line):
		seq += line
	else:
		header = line
		wordbook[header] = seq
wordbook[header] = seq

for fastahead in wordbook:
	wordbook[fastahead] = re.sub(r"([A|G])(AATT[C|T])", r"\1^\2",wordbook[fastahead])
	print (fastahead)
	print (wordbook[fastahead])

# 8

for head in wordbook:
	fragments = wordbook[head].split("^")
	fragments.sort(key=len)
	fragments.reverse()
	print (fragments)
