# - - coding: utf- 8 - -
#Exercise 16 for Learn Python the Hard Way - Reading and Writing Files
"""
• close — Closes the file. Like File- >Save.. in your editor.
• read — Reads the contents of the fi le. You can assign the result to a variable.
• readline — Reads just one line of a text file.
• truncate — Empties the file. Watch out if you care about the file.
• write(stuff)—Writes stuff to the file.
"""
from sys import argv #From system import modules :)
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL+C" #CTRL + C will make then program stop * This is a windows command
print "If you do want that, hit ENTER."
raw_input("?")

print "Opening the file..."
target = open(filename, 'w') #The 'w' will write a new file in case it not exists.

print "Trucating the file. Goodbye!"
target.truncate() #Empties the file

print "Now i'm going to ask you for three lines." #Asking for user's inputs.

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file." #Will now write from user's input to the file.
target.write(line1) #Will write into the line 1.
target.write("\n") #Will make the cursor move to a new line.

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close() #Command to close it.



