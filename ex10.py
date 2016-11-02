# - - coding: utf- 8 - -
#Exercise 10 for Learn Python the Hard Way - What Was That?

"""
Escape Sequences
This is the list of all the escape sequences Python supports.
Escape What it does.
\\ Backslash (\)
\' Single- quote (')
\" Double- quote (")
\a ASCII bell (BEL)
\b ASCII backspace (BS)
\f ASCII formfeed (FF)
\n ASCII linefeed (LF)
\N{name} Character named name in the Unicode database (Unicode only)
\r ASCII carriage return (CR)
\t ASCII horizontal tab (TAB)
\uxxxx Character with 16- bit hex value xxxx (Unicode only)
\Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
\v ASCII vertical tab (VT)
\ooo Character with octal value oo
\xhh Character with hex value hh
"""

tabby_cat = "\tI'm tabbed in." # '\t' will make a tab in the start of this line 
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\ cat." # '\\' These two characters will print just one backslash

#\t is used for Tab (spacing)
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

