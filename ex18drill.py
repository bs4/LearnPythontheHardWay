# this one is like  your scripts with argv. The below line has a *, it tells python to take all arguments to the function and put them in args as a list
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."
    
# this one is putting a lot of words in a row, just for function
def in_a_row(a, b, c, d, e, f, g, h, i, j, k):
    print "a: %r, b: %r, c: %r, d: %r, e: %r, f: %r, g: %r, h: %r, i: %r, j: %r, k: %r" % (a, b, c, d, e, f, g, h, i, j, k)
    
# this one is...going to attempt raw_input...lol, don't know if this will work. it did, that took some maneuvering tho LOL!
def user_def(var1):
    print "Now we attempt the old raw_input."
    girl = raw_input("What is your daughters name?")
    print "Your girl is %r and your son is %r." % (girl, var1)
    
# this one will attempt to read some text in a file. There it is. When I call/run/use the function "filetext" below it will print whatever is in the .txt file...i think lol
def filetext(text1):
    print "Now we attempt to open and read some text from a file."
    wife = open(text1).read()
    print wife
    
print_two("Brandon","Smith")
print_two_again("Brandon","Smith")
print_one("First!")
print_none()
in_a_row('apple', "bee", "cat", "dog", "eel", "fan", "git", "hat", "ick", "jack", "kick")
user_def("Noah")
filetext("ex18_sample.txt")