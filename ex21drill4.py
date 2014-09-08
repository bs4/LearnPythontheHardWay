# trying to grab some text from a file inside a function

def print_a_line(line_count, f):
    print "The file we are reading is %r" % f
    print line_count, open(f).readline(),
    
    
    
file_name = raw_input("What file would you like pulled up? ")
current_line = int(raw_input("And what line would you like to view:? "))

print_a_line(current_line, file_name)


