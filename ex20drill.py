# The below line imports the argv module from sys 
from sys import argv
# The below line gives the argument variables to unpack using argv on the command line
script, input_file = argv
# The below line defines function "print_all" with one FuncVar "f"
def print_all(f):
# The below line prints/uses whatever value is entered for FuncVar "f", then reads it
    print f.read()
# The below line defines function "rewind" with one FuncVar "f"    
def rewind(f):
# The below line prints/uses whatever value is entered for FuncVar "f" and
# seeks line number 0 in that doc
    f.seek(0)
# The below line defines function print_a_line with 2 FuncVar "line_count" and "f"
def print_a_line(line_count, f):
# The below line prints/uses whatever value is entered for FuncVar "line_count" and
# prints just the corresponding N++ line number
# then
# prints/uses whatever value is entered for FuncVar "f" and prints a single line
# SO it uses the file entered for f, prints the line number, then the text on that line
    print line_count, f.readline()
# The below line gives variable "current_file" a value of -- opening the input_file
# which was entered by the user as an argument in the command line
current_file = open(input_file)
# The below line prints the words in "" and uses \n to leave a line empty afterwards
print "First let's print the whole file:\n"
# The below line calls function "print_all" with global variable "current_file"
# see above, you'll recall global variable "current_file" = open(input_file)
# SO, global variable "current_file" opens the file input by user
print_all(current_file)
# The below line prints the words in ""
print "Now let's rewind, kind of like a tape."
# The below line calls function "rewind" with global variable "current file"
rewind(current_file)
# The below line prints the words in ""
print "Let's print three lines:"
# The below line sets global variable current_line = to line 1
# probably needs the rewind or a fresh start to be able to do that
current_line = 1
# The below line calls function "print_a_line" with global variables
# "current_line" and "current_file"
print_a_line(current_line, current_file)
# The below line sets global variable "current_line" to the current line + 1
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# I think when we open a file, we move through it consecutively and Shell saves our
# progress. Thats why we need to use the function "rewind" and why we can use
# current_line + 1 and it knows to go from 1 to 2 to 3 etc