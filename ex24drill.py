print "Let's practice everything."
# The below line uses \ (escapes) to use ' (single quotes) inside
## a string with ' surrounding it
print 'You\'d need to know \'bout escapes with \\ that do \n n',
# I couldn't get Zeds way to work without adding print below
## print below and a , (comma) to end the previous line, after '      
print 'ewlines and \t tabs.'
# the below lines print everything between the """
## notice the \t (escape tab) and \n (escape newline)
## also from """ to """ there are 10 lines, """ included plus \n
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# The below lines use hyphens to make a visual break in the script
## "poem" is a variable that has a value of the above text within """ 
print "--------------"
print poem
print "--------------"

# The below line is a variable "five" with value 10 - 2 + 3 - 6 (=5)
five = 10 - 2 + 3 - 6
# The below line is a string using a modifier to insert the variable
## "five"
print "This should be five: %s" % five
# The below line defines a function named secret_formula
def secret_formula(started):
# The below line sets the temporary variable jelly_beans = to the 
## temporary argument  "started", then multiplies it by 500
    jelly_beans = started * 500
# The below line sets variable "jars" = to "jelly_beans" divided by 1000
    jars = jelly_beans / 1000
# The below line sets variable "crates" = to "jars" divided by 100
    crates = jars / 100
# The below line returns the three values for the 3 temp. variables
## jelly_beans, jars and crates, from the function secret_formula
    return jelly_beans, jars, crates 
    
# The below line sets variable "start_point" = to 10000    
start_point = 10000
# The below line sets the value of global variables "beans" "jars" and
## "crates" = to the returned values from function secret_formula
beans, jars, crates = secret_formula(start_point)
# The below lines are strings with %d modifier to handle numbers from
## variables "start_point" and then "beans" "jars" "crates"
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans,
jars, crates)
# The below line re-values the variable "start_point" = to the original
## start_point value divided by 10
## MATH, essentially taking one zero off each number :), see output
## from below strings
start_point = start_point / 10 
# I added ', new start point: %d" % start_point' to show new start
## point is only 1000, not 10000
print "We can also do that this way, new start point: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)




