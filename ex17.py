# - - coding: utf- 8 - -
#Exercise 17 for Learn Python the Hard Way - More Files
"""
• close — Closes the file. Like File- >Save.. in your editor.
• read — Reads the contents of the fi le. You can assign the result to a variable.
• readline — Reads just one line of a text file.
• truncate — Empties the file. Watch out if you care about the file.
• write(stuff)—Writes stuff to the file.
"""
from sys import argv #From system import the Argv module
from os.path import exists #The exist module will return if the if already exists or not.

script, from_file, to_file = argv #We have two arguments here.

print "Copying from %s to %s" % (from_file, to_file) #From the first to the second file.

in_file = open(from_file) #Variable to open the first file(from_file)
indata = in_file.read() #Make it readable.

print "The input file is %d bytes long" % len(indata) #len command to check the size of the file.

print "Does the output file exist? %r" % exists(to_file) #Calling the exists method to check if the file really exists.
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w') #out_file is the new file we are copying from the first one. 'w' will make the file writable.
out_file.write(indata) #write in out_file the content of indata.

print "Alright, all done."

out_file.close() #Close file.
in_file.close() #Close file.