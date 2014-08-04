name = 'B'
age = 32 # not a lie
height = 72 # inches
weight = 155 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name 
print "He's %s inches tall." % height
print "He's %s pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %s, %s, and %s I get %s." % (
    age, height, weight, age + height + weight)
    
# %r prints exactly what the variable is equal to, ex.- line 1, name = 'Brandon J. Smith', using %r prints the "'" also
# %r also used for debugging since it displays raw data of the variable

# s% does both words and numbers

# %d and %i are for numbers, won't work with words

# Floating Point format E%, e% for exponential format, F%, f% for decimal format

# %c does single character or integer, needs ' (single quote) around it in variable value. ex.- line 1, name = 'B'