from sys import argv

script, first, second, third = argv

# I'm using 'python ex13drill3.py " the beautiful" " the handsome" super' as my command line entry to initiate this script in Shell

number = raw_input("How many kids do you have? ")
emma = raw_input("What is your first child named? ")
noah = raw_input("What is your second child named? ")



print "Your first child is: %s" % (emma + first)
print "Your second child is: %s" % (noah + second)
print "You have %s %s kids." % (number, third)
print "The third argument is: ", third

# WOOT! Finally combined argv and raw_input, see above: whatever I put on the cmd line in position "first" will be added to the %s in the first print line where it is "(emma + first)"
# I don't know yet how this can be useful, but I'm sure I'll find out
# Difference of argv and raw_input from Z: The different has to do with where the user is required to give input. If they give your script inputs on the command line, then you use argv. If you want them to input using the keyboard while the script is running, then use raw_input().
