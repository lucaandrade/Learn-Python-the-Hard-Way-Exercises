# - - coding: utf- 8 - -
#Exercise 5 for Learn Python the Hard Way - Strings and Text
#4. Explain why adding the two strings w and e with + makes a longer string.
#Answer: Basically, the '+' will concatenate the values. As it has no space after the '+' then it will e together.

x = "There are %d types of people." % 10 #I can declare the decimal value like this
binary = "binary" #string variable
do_not = "don't" #string variable
y =  "Those who know %s and those who %s." % (binary, do_not) #I set two variable aove then calling them now, %s as it's a Strings

print x #print the whole x variable
print y #print the whole y variable

print "I said: %r." %x #This is tricky again, will print the whole x, using %r, means it will automatically detect what type of data it is.
print "I also said: '%s.'" %y #This is tricky again, will print the whole y

hilarious = False #Boolean
joke_evaluation = "Isn't that joke so funny?! %r" #Will print the whole variable + the boolen
print joke_evaluation % hilarious #Isn't that joke so funny?! False

w = "This is a the left side of..." #easy string
e = "a string with a right side." #easy string

print w + e #This is a the left side of...a string with a right side.