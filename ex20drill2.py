fo = open("ex20_test.txt", "a+")
print "Name of the file: ", fo.name

fo.seek(8, 0)
line = fo.readline()
print "Read Line: %s" % (line)

fo.seek(28, 1)
line = fo.readline()
print "Read Line: %s" % (line)

fo.close()  

# This seek thing is messing w/me it is using characters in the .txt to place,
# the start, then it does "readline()" from there
# not quite sure how "readline()" is supposed to work