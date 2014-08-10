formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
    

    
    
# So to summarize:
# -the word "formatter" is used here as a variable that equals the formatter %r 4 times in a row within doubles quotes on each side
# -in line 3 for example, there is the variable and a % then a left parenthesis, then 4 values each separated by a comma, 1 value for each of the %r formatters that are the variable's value
# --SO, in line 3, the 4 values in parenthesis are 1, 2, 3, 4 and the %r prints them in Shell exactly as written
# -this can also be seen in line 7, the 4 short sentences within parenthesis and separated by commas print in Shell exactly as written in N++