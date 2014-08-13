the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number
    
# same as above
for fruit in fruits:
    print "A fruit of type %s" % fruit
    
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in items
for i in change:
    print "I got %r" % i
    
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range (0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print "Element was: %d" % i
    
    
    
# RANGE PRACTICE

# range(start, stop[, step])

# below line is just the stop part of above range()
# leaves out the stop integer
# oh, also starts at zero, that must be default
# below line prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(10)

# below line prints: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print range(1, 11)

# below line prints: [0, 5, 10, 15, 20, 25]
# counts up to 30 by fives, 5 is step
print range (0, 30, 5)
# below line prints:[0, 6, 12, 18, 24]
print range (0, 30, 6)

# below line prints: [0, 5, 10, 15, 20, 25, 30]
# even tho not a step of 5, still counts all steps of 5 up to stop point 31
print range (0, 31, 5)

# below line prints: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print range (0, -10, -1)

# below line prints: TypeError expected integer step, got float
#print range (0, 10, .5)
# lol, i had to put a # in front of above line or python won't print
# after it, haha


# STUDY DRILL 2

elementP = [range(0, 6)]

for x in elementP:
    print "This is practice number: %s" % x
    
#...hmm, i think i did this wrong, i think i should be using .append

elementG = 

#...hmm, i don't quite get Study Drill 2, gonna have to come back...

# COMMON QUESTION 3
# This took me a sec typing into Python. good practive tho, i created a list
# test = []
# then created 2 different variables that were equal to lists of words
# then i separately appended (added) each variables list to test
# cool






