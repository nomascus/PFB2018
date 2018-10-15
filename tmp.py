#!/usr/bin/python3


#infile = open("seq.nt.fa", "r")
#outfile = open("nt_counts.txt", "w")

#total_nucs = 0
#counter = 1

#for line in infile:
#	line = line.rstrip()
#	nucs = len(line)
#	total_nucs += nucs
#	outfile.write("line "+ str(counter) + ": " + str(nucs) + "\n")
#	counter += 1

#outfile.write("total_nucs: " + str(total_nucs) + "\n")
#outfile.write('total_nucs: str(total_nucs)\n')
#print("{:s}{:d}".format("total_nucs: " , total_nucs ,"\n"))

#outfile.write("{:s}{:d}\n".format("total nucs: ",total_nucs))

wordbook = {}
with open("sequence_data.txt", "r") as infile:
	for line in infile:
		line = line.rstrip()
#		split_line = line.split("\t")
#		wordbook[split_line[0]] = split_line[1]
		(key, value) = line.split("\t")
		wordbook[key] = value
#print("{:s}\t{:s}".format(wordbook)

for gene,seq in wordbook.items():
#	seq = wordbook[gene]
	print ("{:s}\t{:s}".format(gene,seq))
