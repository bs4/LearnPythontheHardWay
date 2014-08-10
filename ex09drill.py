# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
Line 5
Line 6
Line 7
Line 8
On for infinity, haha
"""

# *NOTE* Using the \ instead of /, changes how the line 7 months print in Shell
# with / they print one one line exactly as written in N++, with \ they print as Z shows Jan, then each successive month on the line below and without the n leading the month name

# \n is for newline

# there was a Study Question about %r in this exercise, lets throw in %r and % into lines 6 and 7
# -line 6 is unchanged, because I didn't use \n there
# -line 7 1st try I added %r and %, but got an error. Then I took out the comma after the second double-quote and it printed, but on one line and with single-quotes around it 
# Interesting, if I put single-quotes around the word months in line 7, it literally uses the word months in the Shell printout, not using the variable and value for it from line 4

# Now time to mess with the """ 3 double-quotes
# I guess you really can just keep adding lines
# Can you add a variable in there? Maybe, but I don't know how