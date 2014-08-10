# The below line is the variable formatter with 4 places
formatter = "%r %r %r %r"
# The below line we call formatter to print 4 numbers
print formatter % (1, 2, 3, 4)
# The below line we call formatter to print 4 words
print formatter % ("one", "two", "three", "four")
# The below line we call formatter to print 4 values
print formatter % (True, False, False, True)
# The below line we call formatter to print itself 4 times
print formatter % (formatter, formatter, formatter, formatter)
# The below lines we call formatter to print 4 strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it did not sing.",
    "So I said goodnight."
    )
# *NOTE* The ' single quote in line 10 of ex8, python adds double quotes around this string when printed to make it unambiguous. this way ' can't be misinterpreted as a beginning or ends
# from internet "Python is clever; it'll use double quotes for strings that contain single quotes when generating the representation, to minimize escapes