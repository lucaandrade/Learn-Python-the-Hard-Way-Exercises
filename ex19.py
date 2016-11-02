# - - coding: utf- 8 - -
#Exercise 19 for Learn Python the Hard Way - Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers): #Define the function Cheese and Crackers
	print "You have %d cheeses!" % cheese_count #You have 20 cheeses!
	print "You have %d boxes of crackers!" % boxes_of_crackers #You have 30 boxes of crackers!
	print "Man that's enought for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) #1 - Here i'm calling the function by giving it values.

print "Or, we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #2 - Here i'm calling the function again.

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #3 - Again!

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)#4 - And again