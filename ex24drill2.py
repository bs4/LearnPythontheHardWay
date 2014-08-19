def chant(x):
    per_day = x
    per_year = x * 365
    per_life = per_year * 75
    return per_day, per_year, per_life

subject = raw_input("What would you like to discuss? ")

print "Ok then, we will talk about %r." % subject
print "I like talking about %r.\n%r is my fav subject." % (subject, subject)
print "There is nothing better than discussing %r.\n%r, %r, %r." % (subject, subject,subject, subject)

daily = int(raw_input("Say %s how many times today? " % subject))
day, year, life = chant(daily)

print "We will chant %d times today, %d this year, %d in your life." % (
    day, year, life)
    
# Output

# What would you like to discuss? babies
# Ok then, we will talk about 'babies'.
# I like talking about 'babies'.
# 'babies' is my fav subject.
# There is nothing better than discussing 'babies'.
# 'babies', 'babies', 'babies'.
# Say babies how many times today? 2
# We will chant 2 times today, 730 this year, 54750 in your life.