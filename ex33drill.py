def vari(x):

    i = 0
    numbers = []


    while i < x:
        print "At the top i is %d" % i 
        numbers.append(i)
        
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
        
    print "The numbers: "

    for num in numbers:
        print num
        
def vari_2(y):
    
    i = 0
    numies = []
    
    while i < y:
        print "Yo, Ho, Yo, Ho: %d" % i
        numies.append(i)
        
        i += 1
        print "A pirate's life:", numies
        print "For me: %d" % i
        
        
    print "For me: "
    
    for booku in numies:
        print booku

    
    
stop = int(raw_input("Stop counting at what number?\n> "))

if 8 <= stop <= 16 or stop >= 21:
    print vari(stop)

elif 0 <= stop <= 7 or 17 <= stop <= 20:
    print vari_2(stop)

    
ship1 = 'swim'   
ship2 = 'dingy'
ship3 = 'sailship'
ship4 = 'battleship'

if stop <= 2:
    print "\ncross ocean in: %s\n" % ship1
elif 3 <= stop <= 7:
    print "\ncross ocean in: %s\n" % ship2
elif 8 <= stop <= 20:
    print "\ncross ocean in: %s\n" % ship3
else:
    print "\ncross ocean in: %s\n" % ship4
    
    
quiz = raw_input("What will you be crossing the ocean in?\n> ")

if quiz == ship1 and stop != (stop > 2):
    print "\nReally gonna swim huh?\n"
elif quiz == ship2 and 3 <= stop <= 7:
    print "\nCan't believe you made it in that little ship, bananas!\n"
elif quiz == ship3 and 8 <= stop <= 20:
    print "\nOoh, CC style. 1492 called, they want their schooner back.\n"
elif quiz == ship4 and stop >= 21:
    print "\nNow we are talking! Bring sand to the beach!\n"
else:
    print "\nLiar! That's not how you'll get across the ocean.\n"

 


# for some reason, the last thing printed in PowerShell is the word "none"
 
# NOTE: I tried range on line 44, but had to use what's written instead, hm

# can you do a countdown also?
