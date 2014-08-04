# The below line gives a value for variable x, the value is a string that has a formatter in it
x = "There are %d types of people." % 10
# The below line gives a value for the variable "binary", I think doing this is a joke of sorts
binary = "binary"
# The below line gives a value for the variable "do_not", the value is a contraction of the variable
do_not = "don't"
# The below line gives variable "y" a value of a string with formatters, there are variables in the string for variable "y"
y = "Those who know %s and those who %s." % (binary, do_not)
# The below line says to print variable "x"
print x
# The below line says to print variable "y"
print y 

#The below line inserts variable "x" using %r formatter. %r formatter prints exactly as it is written. ie-(') single quotes are included.
#Zed does this to quote the above string, basically "I said "variable x"
print "I said: %r." % x
# The below line inserts variable y using %s formatter. In this instance, Zed puts (') singles quotes around %s so that the value put into the string looks quoted.
# Zed had to use single quote for the below line since he used %s instead of %r. It could read -   print "I also said: %r." % y
# *Note* using %r in the line above, *POSSIBLY* since there are already (") double quotes, when it pulls "y" using %r, it changes the (") double quotes in "y" to single quotes
print "I also said: %r." % y
# The below line gives variable "hilarious" a value of "False"
hilarious = False
# The below line gives variable joke_evaluation a value of a string with a formatter
joke_evaluation = "Isn't that joke so funny?! %r"
# The below line uses variable "joke_evaluation" as short hand for the string which is it's value...SO instead of writing out the string everytime, you could just use "joke_evaluation", aha!
# Notice the % after joke evaluation is just as if you typed --  print "Isn't that joke so fully?! %r" % then added variable "hilarious", aha!
print joke_evaluation % hilarious
# The below lines are just a play on words or a joke...I think :) 
w = "This is the left side of..."
e = "a string with a right side."

print w + e 