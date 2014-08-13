print "You enter a dark room with two doors. Do you go through door",
print "#1 or door #2?"


door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Take your time deciding."
    

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your leg off. Good job!"
    elif bear == "3":
        print "The bear's tummy rumbles loudly. Stop wasting time!",
        print "Quickly, do something funny!"
    
        print "1. Stick out tongue."
        print "2. Dance silly with arms out."
        print "3. Cross eyes."
        print "4. Dance for the bear."
    
    silly = raw_input("> ")
    
    if int(silly) in range(1, 3):
        print "Bear licks you...then nibbles on your ear. Ouch!"
    
    elif silly == "4":
        print "What dance will you distract the bear with?"
        
        dance = raw_input("> ")
        
        if dance == "a jig":
            print "Then get those feet a-movin' Michael Flatley!"
        
        else:
            print "\n%s, are you crazy?!?! The bear begins to gnaw" % (dance),
            print "on your (un)happy feet!"
            print "If only you'd done some form of Irish dance!\n"    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
        
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
        

        
        
else:
    print "You stumble around and fall on a knife and die. Good Job!"
    
    
    
    
    
    
    
    
    
    