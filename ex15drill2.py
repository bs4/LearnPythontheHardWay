from sys import argv

script, file_name, file_name2 = argv

txt = open(file_name)
txt2 = open(file_name2)

print "This is the name of your file: %r" % file_name
print txt.read()
print "This is the name of your second file: %r" % file_name2
print txt2.read()

txt2 = open(file_name2)
print "Now I will return  only the first 12 characters of %r." % file_name2
print txt2.read(12)

# Nice! lines 13-15 worked! interesting, they returned 12 characters, but the first 2 lines I didn't write anything in, just left blank, they counted as 1 character for each lines
# You could use this to just write the beginning paragraph of a blog entry...
# Actually probably something similar done when you Google search and only the first ~60 characters on website show up

txt2 = open(file_name2)
print "Now I will return the first 25 characters of %r." % file_name2 
print txt2.read(25)