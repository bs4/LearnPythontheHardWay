from sys import argv

script, emma, noah, trace = argv
print "The name of the script:", script
print "The name of my first child:", emma
print "The name of my second child:", noah
print "The name of my third child:", trace

# Combine raw_input with argv to make a script that gets more input from a user.

first_child = raw_input("What is the name of your first child? ")
second_child = raw_input("What is the name of your second child? ")
third_child = raw_input("What is the name of your third child? ")

print "Your first child is %r, your second child is %r, and your third child is %r." % (
    first_child, second_child, third_child)