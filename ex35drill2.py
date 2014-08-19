def red_corner():
    print "A red gurgling noise reaches your ears."
    t_in_path()
    
    choice = raw_input("> ") 
    if "right" in choice:
        print "Oh no, the way is barred by a waterfall of blood."
        red_around()
    elif "left" in choice:
        blue_corner()
        

def red_around():
    print "With drops of blood on your shirt, you turn around."
    print "Uh oh, the sanguine haze has gotten you mixed up."
    
    which_way()
    
    left_straight()
    
    choice = raw_input("> ")
    if "straight" in choice:
        blue_corner()
    elif "left" in choice:
        green_corner()
    else:
        dead("You are indecisive")
            
            
def blue_corner():
    print "You can see a blue light dancing and teeming with life."
    t_in_path()
    
    choice = raw_input("> ")
    if "right" in choice:
        print "Rounding the corner, a blue flame sets your eyebrows on fire."
        blue_around()
    elif "left" in choice:
        black_corner()
        
    
def blue_around():
    print "In danger of the rest of your face burning off, you turn around."
    print "Uh oh, your eyebrows on fire are blocking your vision."
    
    which_way()
    
    left_straight()
    
    choice = raw_input("> ")
    if "straight" in choice:
        black_corner()
    elif "left" in choice:
        red_corner()
    else:
        dead("The blue flame has jumped to your big grey beard")

def green_corner():
    print "The green colored walls in front of you make you uneasy."
    t_in_path()

    choice = raw_input("> ")
    if "right" in choice:
        print "Poison green darts shoot out at you from the both sides of the path."
        green_around()
    elif "left" in choice:
        red_corner()
        

def green_around():
    print "Groggily moving like a stuck pig, you turn around."
    print "Uh oh, the poison is starting to take effect."
    
    which_way()
    
    left_straight()
    
    choice = raw_input("> ")
    if "straight" in choice:
        red_corner()
    elif "left" in choice:
        black_corner()
    else:
        dead("Standing perfectly still makes the poison work 10x faster")


def black_corner():
    print "Something ahead is sucking all light from existence."
    t_in_path()
    
    choice = raw_input("> ")
    if "right" in choice:
        print "Darkness surrounds you, is this what death feels like?"
        black_around()
    elif "left" in choice:
        green_corner()

def black_around():
    print "Stumbling blindly, you turn around."
    print "Uh oh, the black hole you escaped from has sucked your eyeballs out."
    
    which_way()
    
    left_straight()
    
    choice = raw_input("> ")
    if "straight" in choice:
        green_corner()
    elif "left"in choice:
        blue_corner()
    else:
        dead("Missing eyeballs AND the ability to make decisions is troublesome")


def t_in_path():
    print "There is a T in the path ahead."
    print "Will you turn left or right?"
        
            
def which_way():
    print "Which way did you come from?"
    
    choice = raw_input("> ")
    if "left" in choice:
        print "Phew, you kept your bearings."
    elif "straight" in choice:
        dead("You are lost in the maze")
    else:
        print "Contemplating walking through a T from the top right,",
        print "one is faced with only two options: left or straight."
            
            
def left_straight():
    print "Back track and go left or continue on straight?"

    
def dead(why):
    print why, "\b and you will die. Good job!"
    exit(0)
    
def start():
    print """
    \n The labyrinth you are in seems to go on forever,
    endlessly going either right or left.
    Choosing to go one way or another could get you one step closer
    to the exit and fresh, air or send you that much deeper underground.
    One wrong turn could be your last, who knows what dangers
    lurk in the depths.
    You take your first steps into darkness,
    """
    red_corner()

start()    