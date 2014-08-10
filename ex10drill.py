tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
butt_in = "\b\b\bBOOTY BOOTY BOOTY"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

string_cat = "\a\tBACKSPACE\bI Spray on other cats' food %s." % fat_cat

print tabby_cat + butt_in
print persian_cat
print backslash_cat
print fat_cat

print string_cat 

# Escape sequences that python supports
# \\ backslash()
# \' single-quote (')
# \" double-quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N {name} Character named name in the Unicode database (Unicode only)
# \r ASCII Carriage Return (CR)
# /t ASCII horizontal Tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx (Unicode Only)
# Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v ASCII vertical tab (VT)
# \ooo Character with octal value ooo
# \xhh Character with hex value hh