from sys import argv

script, filename = argv

txt = open(filename)

print "The name of your file is %r." % filename
print "Were the changes made? Let's see:"
print txt.read()


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")