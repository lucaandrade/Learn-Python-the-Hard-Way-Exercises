# - - coding: utf- 8 - -
#Exercise 15 for Learn Python the Hard Way - Reading Files
from sys import argv #importing modules from the system
prompt = "> "
script, filename = argv
txt = open(filename) #It will just open the file we wanted to work with

filename = raw_input("What is the filename? ")
#print "Here's your file %r:" % filename #Print the filename
print txt.read() #It will read the inside data from the opened file and print on screen.
txt.close() #This closes the txt file.

"""
print "Type the filename again:"
file_again = raw_input("> ") #Here we ask the user's the exactly filename again.
txt_again = open(file_again) #Then we store in this variable and open.
print txt_again.read() #We print again the same file.
"""