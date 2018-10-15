#!/usr/bin/perl
import sys

#name = 'joe'
#color = 'brown'
#activity = 'sloth'
#animal = 'pinkerton'

#print('my name is ',name,color,activity,animal)

#The script should print out, your name, favorite color, favorite activity, and your favorite animal.
#Make it executable using chmod (only have to do this one time per script).
#Run it from the command line.


name = sys.argv[1]
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]

print('my name is ',name,color,activity,animal)

