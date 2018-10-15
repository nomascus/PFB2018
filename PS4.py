#!/usr/bin/python3

# 1

# num =1
# while num < 101:
#	print(num)
#	num +=1

# 2

#num = 1
#factorial = 1
#while num < 1000:
#	factorial = factorial * (num+1) 
#	num +=1
#print(factorial)


# 3 

#numbers =  [101,2,15,22,95,33,2,27,72,15,52]
#for number in numbers:
#	if number % 2 == 0: 
#		print(number)

# 4

numbers = [101,2,15,22,95,33,2,27,72,15,52]

evens = 0
odds = 0

for number in sorted(numbers):
	print (number)
	if number % 2 == 0:
		evens += number
	else:
		odds += number
print ("sum of evens: ",evens, "\n" "sum of odds: ",odds)

# 5

#for num in range(99):
#	if num != 0:
#		print (num)


print(list(range(100)))


# 6

import sys

print ("\n\n #6 \n\n")

start = int(sys.argv[1])
end = int(sys.argv[2])

print ("start = ",start, "end = ", end)
while start <= end:
	if start % 2 != 0:
		print(start)
	start += 1

# 7 

print ("\n\n #7 \n\n")

DNA = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for dna in DNA:
	print(len(dna), "\t", dna)

# 8 

print ("\n\n #8 \n\n")

#for dna in DNA:
#	DNAtup = (len(dna), dna)
#	print (DNAtup[0],"\t", DNAtup[1])

DNAlist = [(len(dna), dna) for dna in DNA]

#print(DNAlist)
for dna_tuple in DNAlist:
	print ("{0:d}\t{1:s}".format(*dna_tuple))

# 9

print ("\n\n #9 \n\n")

DNAlist = [(len(dna), dna) for dna in DNA]
counter = 1
for dna_tuple in DNAlist:
	print ("counter\t", "{0:d}\t{1:s}".format(*dna_tuple))
	counter +=1


