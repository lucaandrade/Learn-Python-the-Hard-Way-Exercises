# - - coding: utf- 8 - -
#Exercise 5 for Learn Python the Hard Way - More Variables and Printing
'''
Conversion	Meaning	Notes
d	Signed integer decimal.	
i	Signed integer decimal.	
o	Unsigned octal.	(1)
u	Unsigned decimal.	
x	Unsigned hexadecimal (lowercase).	(2)
X	Unsigned hexadecimal (uppercase).	(2)
e	Floating point exponential format (lowercase).	
E	Floating point exponential format (uppercase).	
f	Floating point decimal format.	
F	Floating point decimal format.	
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.	
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.	
c	Single character (accepts integer or single character string).	
r	String (converts any python object using repr()).	(3)
s	String (converts any python object using str()).	(4)
%	No argument is converted, results in a "%" character in the result.	
'''

name = 'LUCAS'
age = 25 # i'm not a lie
height = 69 #inches
weight = 159.3 #lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'
centimeters = height * 2.54
kilograms = weight * 0.453592
shit = 'old'
print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "He's %3.2f pounds heavy." %weight #Floating number. 3.2 means: I want 3 first numbers and 2 after point.
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofee." % teeth

#Some tricky
#'r' stands for Raw representation. Automatically converts anything
print "If i add %d, %d, and %3.2f I get %r." % (age, height, weight, age + height + weight)


print
#inches to centimeters
print "So if you have %d inches then you got %1.2f in Centimeters" % (height, centimeters)
print "And, if you have %d Pounds then you got %2.2f in Kilograms" % (weight, kilograms)
print "How %s are you?" %shit
