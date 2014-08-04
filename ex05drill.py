name = 'B'
age = 32 # not a lie
height = 72 # inches
weight = 155 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

euro_height = height * 2.54
euro_weight = weight / 2.20462

print "Let's talk about %s." % name 
print "He's %s inches tall." % height
print "He's %s pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If he lived in Europe, %s's height and weight would be in centimeters and kilos." % name
print "%s would be %d cm tall and %i kilos heavy." % (name, euro_height, euro_weight)

# this line is tricky, try to get it exactly right
print "If I add %s, %s, and %s I get %s in America." % (
    age, height, weight, age + height + weight)
print "However, if I add %f, %f and %f I get %f in Europe." % (
    age, euro_height, euro_weight, age + euro_height + euro_weight)
    
# %r prints exactly what the variable is equal to, ex.- line 1, name = 'Brandon J. Smith', using %r prints the "'" also

# s% does both words and numbers

# %d and %i are for numbers, won't work with words

# Floating Point format E%, e% for exponential format, F%, f% for decimal format

# %c does single character or integer, needs ' (single quote) around it in variable value. ex.- line 1, name = 'B' **I changed the name a couple times, just think if I only called myself B**