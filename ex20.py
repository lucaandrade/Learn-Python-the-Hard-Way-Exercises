# - - coding: utf- 8 - -
#Exercise 20 for Learn Python the Hard Way - Functions and Files

from sys import argv #From system import argv

script, input_file = argv

def print_all(f): #Function to print out the whole file
	print f.read()
	
def rewind(f): # resets pointer to beginning of file
	f.seek(0)
	
def print_a_line(line_count, f): #Function to print out a line.
	print line_count, f.readline() #f.readline() will make it prints only the current line. The readline() function returns the \n that’s in the file at the end of that line.

current_file = open(input_file) #We have always to open the file before we starting calling.

print "First let's print the whole file:/n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)# resets pointer to beginning of file

print "Let's print three lines:" #We are counting the line and printing.
current_line = 1
print_a_line(current_line, current_file) #We call the function print_a_line

current_line += 1 #The shorthand notation '+=' means current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)