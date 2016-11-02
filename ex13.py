# - - coding: utf- 8 - -
#Exercise 13 for Learn Python the Hard Way - Parameters, Unpacking, Variables

from sys import argv #'import' add features to your script from the Python feature set. Rather than give you all the features at once.

script, first, second, third = argv #This variable holds the arguments you pass to your Python script when you run it.

#*We need to declare 3 arguments for this program run, if less then it, then it says Error: need more than 3 values to unpack

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third