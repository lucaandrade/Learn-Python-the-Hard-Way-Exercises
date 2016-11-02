# - - coding: utf- 8 - -
#Exercise 8 for Learn Python the Hard Way - Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", #It's gonna print with double quotes because there's a word that uses a quote didn't. So Python will make it doule quote so its more readable.
	"So i said goodnight."
)