#!/usr/bin/python3

# 1,2

infile = open("TomPetty.txt", "r")
outfile = open("TomPettyUpper.txt", "w")
for line in infile:
	line = line.rstrip()
	line = line.upper()
	#print(line)
	outfile.write(line+"\n")


# 3

infile = open("Python_06.seq.txt", "r")
wordbook = {}

for line in infile:
	line = line.rstrip()
	gene,seq = line.split("\t")
	seq_rev = ''.join(reversed(seq)).lower()
	seq_rev = seq_rev.replace('a','T')
	seq_rev = seq_rev.replace('t', 'A')
	seq_rev = seq_rev.replace('c','G')
	seq_rev = seq_rev.replace('g','C')
	wordbook[gene]=seq_rev

#for gene,seq in wordbook.items():
#	print("{:s}\n{:s}".format(">"+gene,seq))


# 4

infile = open("Python_06.fastq", "r")

line_count = 0
characters = 0
for line in infile:
	line_count += 1
	line_length = len(line)
	characters += line_length

mean_length = characters/line_count

#print("total lines:", line_count, "\ntotal characters:", characters, "\naverage line length:", mean_length) 

# 5
CPset = set()
TPset = set()

TFfile= open("alpaca_all_genes.tsv", "r")
CPfile = open("alpaca_stemcellproliferation_genes.tsv","r")

for line in TFfile:
	line = line.rstrip()
	if line.startswith("Gene"):
		continue
	else:
		TPset.add(line)
for line in CPfile:
	line = line.rstrip()
	if line.startswith("Gene"):
		continue
	else:
		CPset.add(line)
shared_set = TPset & CPset

for genes in shared_set:
	print(genes)


# Extra 1

infile = open("Python_06.seq.txt", "r")

wordbook = {}
for line in infile:
	line = line.rstrip()
	header,seq = line.split("\t")
	seq_dict = {}
	for position in range(0, len(seq)):
		if seq[position] not in seq_dict:
			seq_dict[seq[position]] = 1
		else:
			seq_dict[seq[position]] +=1
	GC = (seq_dict['G'] + seq_dict['C']) /len(line)
	print("{:s}\t{:s}{:.2f}".format(header,"GC content: ",GC),end = '')
	for nuc in sorted(seq_dict):
		nuc = nuc.rstrip()
		print("\t"+nuc+":"+str(seq_dict[nuc]), end = '')
	print('')
