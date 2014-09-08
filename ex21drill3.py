def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "Going reverse, starting with #'s and making functions fit"

print "equation we are shooting for is:"
print "  12 + 16 * 3 / 4 - 5"

w = multiply(16, 3)
x = divide(w, 4)
y = add(12, x)
z = subtract(y, 5)

print "That way returns us %d" % z 

print "By hand returns us 19\n"

print "Woo Woo!\n"