# The below line prints the words in quotes
print "Mary had a little lamb."
# The below line prints the words in quotes and then has a formatter "%s" for the string 'snow'. 'snow' is a string because it has quotes (single or double), a variable wouldn't have the single quotes around it
print "Its fleece was white as %s." % 'snow'
# The below line prints the words in quotes
print "And everywhere that Mary went."
# The below line prints the "." in quotes 10 times, then the pound character stops the printing for a comment
print "." * 10 # what'd that do?
# The below lines are variables that correspond to values, any other word or number could be used to replace "end + number"
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# *NOTE* The below line is actually different on Zed's study guide, it has the "ppens" in happens on line 24, I couldn't figure out how that works, so I moved it up till later I might learn it
# watch that comma at the end. try removing it to see what happens
# The below line adds all the listed variables together and spells "Cheese", *NOTE* the "," comma at the end makes python print lines 20 & 21 as one line in Powershell
# *NOTE* from Z: Q:Couldn't you just not use the comma , and turn the last two lines into one single-line print? Yes, you could, but then it'd be longer than 80 characters, which in Python is bad style.
print end1 + end2 + end3 + end4 + end5 + end6,
# The below line adds all the listed variables together and spells "Burger"
print end7 + end8 + end9 + end10 + end11 + end12