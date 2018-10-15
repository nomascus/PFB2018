#!/usr/bin/python3
import sys
import math
#taco = sys.argv[1]


#if bool(taco) == 1:
#	print('True')
#else:
#	print('Not True')

number = int(sys.argv[1])

if number >= 0:
	print ('this number is positive')
	if number > 50:
		print("it's also bigger than 50")
		if math.modf(number/3)[0] ==0:
			print ('the number is divisible by 3')
		else:
			print ('the number is not divisible by 3')
	elif number == 50:
		print("the number is 50")
	else:
		print("it's less than 50")
		if number%2 !=0:
			print ("the number is odd")
		else:
			print("the number is even")
else:
	print('this number is negative')


