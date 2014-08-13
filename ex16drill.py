from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write('%s\n%s\n%s\n\n' % (line1, line2, line3))

print "And finally, we close it."
target.close()

txt = open(filename)
print "And here is what's now contained in %r." % filename
print txt.read()

# Interesting both '%s \n %s \n %s \n' and '%s\n%s\n%s\n' behave the same. i didn't need the spaces in the former
# This might lead to how you get things put into a document, etc. User types the info asked of them, then it's written to the doc.
# you might even be able to place the exact location of the raw_input from the user, ex.- a specific spot in a document

# Now to practice with the parameter 'a' for command open
# First I erased the whole truncate thing to see if it still erases the .txt with parameter 'w'
# parameter 'w' erases the contents of the .txt
# parameter 'a' adds onto the .txt...but does it use the first empty line? nope didn't use first empty line, BUT it doesn't skip the empty line at the end of .txt