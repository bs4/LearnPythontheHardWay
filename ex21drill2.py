def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = add(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height
, weight, iq)


# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, add(iq, 2
))))

print "That becomes: ", what, "Can you do it by hand?"

# add(age, k(j, i(z, y(x, 2))))
x = iq # iq
y = add(x, 2) # add(iq, 2)
z = multiply(90, 2) # weight
i = multiply(z, y) # multiply(weight, add(iq, 2))
j = subtract(78, 4) #height
k = subtract(j, i) # subtract(height, multiply(
 # weight, add(iq, 2)))
l = add(30, 5) # age
m = add(l, k) # add(age, subtract(height, multiply(
 # weight, add(iq, 2))))


print "x= %d, y= %d, z= %d, i= %d, j= %d, k= %d, l= %d, m= %d" % (
 x, y, z, i, j, k, l, m)




