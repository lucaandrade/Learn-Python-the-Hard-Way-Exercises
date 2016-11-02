# - - coding: utf- 8 - -
#Exercise 14 for Learn Python the Hard Way - Prompting and Passing
from sys import argv #'import' add features to your script from the Python feature set. Rather than give you all the features at once.

script, user_name = argv
prompt = "> " #Will prompt a '> ' in the user input, like a game.

print "Hi %s, i'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt) #Now, the raw_input takes an argument which is Prompt '>' to the user.

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "How much you earn per month?"
salary = raw_input(prompt)

#Print multiple lines
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer. Nice.
And you earn %r per month! Damn!
""" % (likes, lives, computer, salary)