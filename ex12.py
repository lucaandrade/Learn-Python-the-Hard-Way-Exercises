# - - coding: utf- 8 - -
#Exercise 12 for Learn Python the Hard Way - Prompting People
#To get help on python when in the PowerShell window, type: python -m pydoc raw_input
age = raw_input("How old are you? ") #'raw_input' takes the user's input value and store in the variable 'age'
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)