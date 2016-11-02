# - - coding: utf- 8 - -
#Exercise 11 for Learn Python the Hard Way - Asking Questions

print "How old are you?",
age = raw_input() # 'raw_input()' is the command used to take the input from the user.
print "How tall are you?", #6'2" - This outputs: 6\'2" - The backslash escapes the quote so that the interpreter will treat it as a regular character
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)