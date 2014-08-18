
def shanty(x):

    b = x
    beer = [1]
    beer.extend(range(2, (b + 1)))

    while b >= 1:
        print "\n%d bottles of beer on the wall" % b
        print beer, "bottles of beer!\n",
        
        beer.remove(b)
        
        print "Take one down, pass it around, %d" % int(b - 1),
        print "bottles of beer on the wall."
        
        b = b - 1
              
    else:
        return """
There were %d bottles of beer on the wall
There were %d bottles of beer!
But we've taken 'em down and passed them around
Now there are no more beers on the wall!
        """ % (x, x)
        
        
bottles = int(raw_input("How many bottles of beer on the wall?\n> "))

#people = int(raw_input("How many people drinking with you today?\n> "))


print shanty(bottles)

# the '#people' variable was a first (failed) try at multiplying
## people by bottles and getting how many bottles drank per round