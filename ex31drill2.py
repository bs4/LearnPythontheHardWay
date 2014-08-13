# Hmm, working on this for my 3 year old, maybe she'll think this is fun

print """
In the far away land of My Home,
a tale of daring and bravery waits
to be told.
"""

print "Which of you adventurers is up to the challenge?"
print "1. Emma"
print "2. Noah"

adventurer = raw_input("> ")

if adventurer == "1":
    print "The brave hero Emma steps forward!"
    
    print"""
    Soon our hero will set out on a long and arduous
    journey to recover the fabled Frog Wand from the
    Farm People.
    This trek will take Emma all the way to Downstairs
    where she will have to find the Farm People village
    of Flat Coffee Table.
    """
    
    print "Which path will our hero decide to take?"
    print "1. Transport through the floor head first"
    print "2. Grasp desperately to the Hand Rail",
    print "on the way to Downstairs"
    
    path = raw_input ("> ")
    
    if path == "1":
        print "Bonk! The shortest path is not always the safest."
        
    elif path == "2":
        print "With hand muscles straining, Emma maneuvers",
        print "her way along the Hand Rail towards Downstairs."
        
        print """
        After hanging onto the Hand Rail for what
        seemed like ages, our hero Emma has finally arrived in
        the land of Downstairs and the village of Flat Coffee Table
        is within sight. To recover the Frog Wand,
        Emma must be true to herself in choosing how she will
        approach the village and take back the Frog Wand.
        How will Emma choose to behave?
        1. Ask nicely like a big girl
        2. Whine and throw a fit until the Farm People return it
        """
        
        choice = raw_input("> ")
        
        if choice == "1":
            print "Hurray, being polite did the trick. All is well!"
            
        elif choice == "2":
            print "Uh oh, the Farm People don't like whiny little girls. No Frog Wand for you!"
            
        else:
            print "Uh oh, if only our hero had been a big girl and asked nicely. No Frog Wand for you."
        
    else:
        print """
        Your indecision has proven fatal.
        Sitting in it's cozy home, looking cute,
        and waiting for a misstep by an
        aimlessly wandering hero,
        the vicious Mir Cat pounces.
        Hopefully another hero will rise and
        recover the Frog Wand of legend.
        """

elif adventurer == "2":
    print "The brave hero Noah steps forward!"
    
    print"""
    Oh no! The young hero Noah is but a
    squire and doesn't have the experience,
    nor the intuition to conquer quests or
    adventures such as this one, alone.
    Won't an older, wiser, more femanine
    hero take young Noah's place?
    """
    
else:
    print "Noone steps forward. Is there no one in the land",
    print "strong and daring enough to meet the challenge?"