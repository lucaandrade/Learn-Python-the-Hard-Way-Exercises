# - - coding: utf- 8 - -
#Exercise 21 for Learn Python the Hard Way - Functions Can Return Something

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b #Return the result, but does not print to the console.
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?\n"

#Try 24 + 34 / 100 - 1023

soma = add(24, 34)
subtracao = subtract(100, 1023)

whatis = divide(soma, subtracao)
print "divide(soma, subtracao) = %r" % whatis