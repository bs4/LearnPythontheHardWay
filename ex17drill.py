from sys import argv ; script, from_file, to_file = argv ; print "Copying %s to %s" % (from_file, to_file) ; indata = open(from_file).read() ; print "The length of this file is %d characters." % len(indata) ; open(to_file, 'w').write(indata)