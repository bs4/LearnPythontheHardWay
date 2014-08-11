# The below line tells the script to import the argv module from sys
from sys import argv
# The below line tells how many arguments for argv to use
script, filename = argv
# The below line gives variable (txt) a value (open(filename). open is a command. filename is an argument from the user as to which file the user would like opened
txt = open(filename)
# The below line prints the string located in quotes, using formatter %r for whatever file the user put as their argument for "filename"
print "Here's your file %r:" % filename
# The below line returns a string containing all characters in the file. txt = opened file that was input by user in argument line, read() 
print txt.read()
# The below line asks the user to tell the name of the file again, this time at the > prompt. Also, what user enters at > will equal variable "file_again"
print "Type the filename again:"
file_again = raw_input("> ")
# The below line makes variable "txt_again" equal to command open the variable file_again
txt_again = open(file_again)
# The below line returns a string containing all characters in the file. txt_again = opened name of file input by user at prompt, read() is command that returns everything in the file
print txt_again.read()