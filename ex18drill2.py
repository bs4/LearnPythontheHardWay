# this is me making a function that will print whatever .txt file the user chooses

print
users_choice = raw_input('What file would you like to read? ')

def print_txt(txt):
    print
    print "Here is what is written in %r:" % txt
    print
    file = open(txt).read()
    print file
    
print_txt(users_choice) 