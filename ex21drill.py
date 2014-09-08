def my_skittles(a, b):
    print "I have %d + %d skittles" % (a, b)
    return a + b
    
def your_skittles(a, b):
    print "You have %d + %d skittles" % (a, b)
    return a + b 
    
print "Let's see how many skittles each of us have."

me = my_skittles(int(raw_input("# skittles in my hand "))
 , int(raw_input("# skittles in my bag ")))
 
you = your_skittles(int(raw_input("# skittles in your hand "
 )), int(raw_input("# skittles in your bag ")))
 
print "I have %d skittles and you have %d skittles" % (
 me, you)

print "Together we have %d skittles" % (me + you)

what = (me + you) - (1 * 28)

print "Eating one by one we have", what, ", Oops, now we have none"

# Now working Study Drill #2 