# Roadtrip
# How fast can you get from Seattle to Las Vegas?
# How many hitchhikers can you arrive with?


# variable list

prompt = "> "

vehicle = "\nYour %s seats %d passenger(s) and goes %d miles before fillup.\n"
scooter = "\nRiding a %s, you and %s are off, gas for %d miles, next stop %s. %d miles to Vegas!"
multi_seat = "\nDriving a %s, you and %s are off,\n gas needed in %d miles, next stop %s. %d miles to Vegas!"
tesla = "\nDriving a %s, you and %s are off, gas for %d miles, next stop %s. %d miles to Vegas!"

seattle_hitchhikers = ['a hobo', 'a bum', 'a louse', 'Paul Allen']
oly_hitchhikers = ['a hippy with a guitar']
port_hitchhikers = ['a student', 'a Trailblazer', 'a professor']
yreka_hitchhikers = ['Jessie Spano']
sf_hitchhikers = ['a hipster', 'a jogging nudist', 'Dirty Harry']
bakers_hitchhikers = ['a man named "Mule"']

gas_stop = "\nYour %s has traveled %d miles and the fuel gauge is on E, time to stop for gas.\n"
gas_full = "All fueled up. Anyone have to pee? No? Ok, let's hit the road."

battery_stop = "\nYour %s has traveled %d miles and the battery is dead, time to stop for a charge.\n"
battery_full = "All charged up. Anyone else excited about the 8 year warranty on this battery?\nJust me? Ok, let's hit the road."

scootscoot = ('scooter', 1, 300)
# jalopy
# sedan
# van
# tesla

# hobo
# paul_allen
# hippy
# college_student
# trailblazer
# showgirl
# hipster
# nudist
# dirty_harry
# mule

# seattle
# portland
# sf
# vegas


def seattle():
    miles = 1400
    print "\n---Welcome to Seattle---\n"
    print 'Start journey with a scooter or a truck?'
    start = raw_input(prompt)
    
    if 'scooter' in start:
        seattle_hitch('scooter', 1, 300, miles)
    
    elif 'truck' in start:
        seattle_hitch('truck', 3, 150, miles)
        
    else:
        print "What car is that? You're stuck with the jalopy."
        seattle_hitch('jalopy', 3, 150, miles)
        
        
def seattle_hitch(car, people, range, miles):
      
    print vehicle % (car, people, range)
    
    if miles - range > 1200:
        next = 'gas station'
        
    else:
        next = 'Portland'
  
    if car == 'scooter':
        print "Take which hitchhiker: a hobo, a bum, a louse, or Paul Allen?"
        hitch_sea = raw_input(prompt)
        print scooter % (car, hitch_sea, range, next, miles)
        olympia(car, people, range, hitch_sea, miles)
    
    elif car == 'truck' or car == 'jalopy':
        print "Choose which of the 4 hitchhikers won't be going to Vegas:",
        print "a hobo, a bum, a louse, or Paul Allen?"
        
        while True:
            try:
                kick = raw_input(prompt)
                seattle_hitchhikers.remove(kick)
                hitch_sea = seattle_hitchhikers
                break
            except ValueError:
                print "Even hitchhikers like their name spelled correctly."
                print "Try again."
        
        print multi_seat % (car, ', '.join(hitch_sea), range, next, miles)
        
        gas_sea_to_port(car, people, range, hitch_sea, miles)
        
  
def gas_sea_to_port(car, people, range, hitch_sea, miles):
    miles = miles - range
    print "gas_sea_to_port test for miles = %d" % miles
    print gas_stop % (car, range)
    
    if miles - range > 1200:
        print "IF test miles = %d" % miles
      
        next = 'gas station'
        print gas_full
        print multi_seat % (car, ', '.join(hitch_sea), range, next, miles)
        gas_sea_to_port(car, people, range, hitch_sea, miles)
    
    elif miles - range <= 1200:
        print "ELIF test miles = %d" % miles
        next = 'Olympia'
        print gas_full
        print multi_seat % (car, ', '.join(hitch_sea), range, next, miles)
        olympia(car, people, range, hitch_sea, miles)
        
    else:
        print "Broken at gas_sea_to_port"
        
    

def olympia(car, people, range, hitch_sea, miles):
    print " Olympia Test for miles = %d" % miles
    print "\n---Bonus Round---\n-----Olympia-----\n"
    print "Passing thru Olympia, you see a hippy with a guitar from",
    print "Evergreen College."
    next = 'Portland'
    
    if car == "scooter":
        print "Trade %s for a hippy with a guitar?" % hitch_sea
        swap = raw_input(prompt)
        
        if swap == 'yes':
            hitch_oly = 'a hippy'
            print scooter % (car, hitch_oly, range, next, miles)
            portland(car, people, range, hitch_oly, miles)
        
        elif swap == 'no':
            print scooter % (car, hitch_sea, range, next, miles)
            hitch_oly = hitch_sea
            portland(car, people, range, hitch_oly, miles)
            
        else:
            print "%s? Sorry, you're stuck with %s." % (swap, hitch_sea)
            hitch_oly = hitch_sea
            portland(car, people, range, hitch_oly, miles)
        
#    elif car == "truck" or car == 'jalopy':


def portland(car, people, range, hitch_oly, miles):
    print "Portland test for miles = %d" % miles
    miles = 1200
    print "\n---Welcome to Portland---\n"
    print "Upon arrival in Portland, you have the option to switch vehicles."
    print "Would you like to continue your trip with a sedan, a van,",
    print "or your %s?" % car
    car_change = raw_input(prompt)

    if car_change == car:
        port_hitch(car, people, range, hitch_oly, miles)
        
    elif 'van' in car_change:
        print 'going with the big mover'
        
    elif 'sedan' in car_change:
        print 'gonna go with the sedan'
        
    else:
        print "Oh sorry, we are all out of %s, choose another vehicle." %(
        car_change)
        portland(car, people, range, hitch_oly, miles)
        
        
def port_hitch(car, people, range, hitch_oly, miles):
    print vehicle % (car, people, range)
    print "Hooray, you found more hitchhikers in Portland."
    
    if miles - range <= 600:
        next = 'San Francisco'
        
    else:
        next = 'gas station'
    
    if car == 'scooter':
        print "Would you like to trade %s for a new hitchhiker?" % hitch_oly
        swap = raw_input(prompt)
        
        if 'yes' in swap:
            print "Ok, will you now take a student, a trailblazer,",
            print "or a professor?"
            new = raw_input(prompt)
            hitch_port = new
            print scooter % (car, hitch_port, range, next, miles)
            gas_port_to_sf(car, people, range, hitch_port, miles)
         
        elif 'no' in swap:
            hitch_port = hitch_oly
            print scooter % (car, hitch_port, range, next, miles)
            gas_port_to_sf(car, people, range, hitch_port, miles)
            
        else:
            print "Error in port_hitch 'scooter'"
    
    
    else:
        print "Available hitchhikers are %s and %s." % (', '.join(hitch_oly), ', '.join(port_hitchhikers))
        oly_hitch.extend(port_hitchhikers)
        
        
        while oly_hitch.count() > 3:
            try:
                print "Pick a hitchhiker to stay in Portland."
                new = raw_input(prompt)
                oly_hitch.remove(new)
                print "Remaining hitchhikers are %s." % ', '.join(hitch_oly)
                break
            except ValueError:
                print "Even hitchhikers like their name spelled correctly."        
        
        print multi_seat % (car, ', '.join(hitch_port), range, next, miles)
        
        while True:
            try:
                oly_hitch.remove(new)
                hitch_sea = seattle_hitchhikers
                break
            except ValueError:
                print "Even hitchhikers like their name spelled correctly."
                print "Try again."
        
        print multi_seat % (car, ', '.join(hitch_sea), range, next, miles)
        
        gas_sea_to_port(car, people, range, hitch_sea, miles)
    
       
def gas_port_to_sf(car, people, range, hitch_port, miles):
    miles = miles - range
    print "gas_port_to_sf test for miles = %d" % miles
    print gas_stop % (car, range)

    if miles - range > 600:
        next = 'gas station'
        print gas_full
        if car == 'scooter':
            print scooter % (car, hitch_port, range, next, miles)
            gas_port_to_sf(car, people, range, hitch_port, miles)
        else:
            print multi_seat % (car, ', '.join(hitch_port), range, next, miles)
            gas_port_to_sf(car, people, range, hitch_port, miles)
        
    
    elif miles - range <= 600:
        next = 'San Francisco'
        print gas_full
        if car == 'scooter':
            print scooter % (car, hitch_port, range, next, miles)
            yreka(car, people, range, hitch_port, miles)
        else:
            print multi_seat % (car, ', '.join(hitch_port), range, next, miles)
            yreka(car, people, range, hitch_port, miles)
        
    else:
        print "Broken at gas_port_to_sf"


def yreka(car, people, range, hitch_port, miles):
    print "\n---Bonus Round---\n------Yreka------\n"
    print "Passing thru Yreka, you see a showgirl hopeful",
    print "looking for a ride to Las Vegas."
    
    next = 'San Francisco'
    
    print "Ditch a current hitchhiker and help Jessie Spano get to Vegas?"
    
    new = raw_input(prompt)
    
    if new == 'yes' and people > 1:
        print "Yreka Test for Yes and multi seat vehicles"
        
    elif new == 'no' and people > 1:
        print "Yreka Test for No and multi seat vehicles"
        
    elif new == 'yes' and people == 1:
        hitch_yreka = ['Jessie Spano']
        print scooter % (car, ', '.join(hitch_yreka), range, next, miles)
        sf(car, people, range, hitch_yreka, miles)
        
    elif new == 'no' and people == 1:
        print scooter % (car, hitch_yreka, range, next, miles)
        sf(car, people, range, hitch_yreka, miles)
        
    else:
        print "Yreka Else statement...broken?"        
        

def sf(car, people, range, hitch_yreka, miles):
    print "SF test for miles = %d" % miles
    print "\n---Welcome to San Franscisco---\n"
    miles = 600
    print "Upon arrival in San Franscisco you are given the option to\n",
    print "trade-in your %s for a Tesla Roadster." % car, "Go electric?"
    car_change = raw_input(prompt)
    
    if car_change == 'yes':
        car = 'Tesla Roadster'
        people = 1
        range = 245
        sf_hitch(car, people, range, hitch_yreka, miles)
    
    elif car_change == 'no':
        sf_hitch(car, people, range, hitch_yreka, miles)


def sf_hitch(car, people, range, hitch_yreka, miles):
    print vehicle % (car, people, range)
    
    if miles - range > 0:
        next = 'gas station'
    
    else:
        next = 'Las Vegas'
    
    print "Driving down Lombard Street, %s jump into\n" % ', '.join(sf_hitchhikers),
    print "your %s, but \'Oh Noes!\' there's not enough room!" % car
    print "\nCurrent hitchhikers are: %s." % ', '.join(hitch_yreka)
    print "Available hitchhikers from Frisco are: %s." % ', '. join(sf_hitchhikers)
    
    hitch_yreka.extend(sf_hitchhikers)
    
    while True and len(hitch_yreka) > people:
        try:
            print "\nWho to kick from your merry, traveling band:\n",
            print "%s?" % ', '.join(hitch_yreka)
            
            kick = raw_input(prompt)
            
            print "\nYou're outta here, %s!\n" % kick
            
            hitch_yreka.remove(kick)
                       
        except ValueError:
            print "Even hitchhikers like their name spelled correctly."
            print "Try again."
    
    hitch_sf = hitch_yreka
    
    if 'scooter' in car:
        print scooter % (car, hitch_sf, range, next, miles)
        
    elif 'Tesla' in car:
        print tesla % (car, ', '.join(hitch_sf), range, next, miles)
        
    elif people > 1:
        print multi_seat % (car, ', '.join(hitch_sf), range, next, miles)
        
    else:
        print "Broke dittely broken @ sf_hitch"
        
    gas_sf_to_vegas(car, people, range, hitch_sf, miles)
    
    
    
def gas_sf_to_vegas(car, people, range, hitch_sf, miles):
    print "gas_sf_to_vegas PRE test for miles = %d" % miles
    miles = miles - range
    print "gas_sf_to_vegas POST test for miles = %d" % miles
    
    if miles - range > 0:
        next = 'gas station'
        if 'Tesla' in car:
            print battery_stop % (car, range)
            print battery_full
            print tesla % (car, ', '.join(hitch_sf), range, next, miles)
            gas_sf_to_vegas(car, people, range, hitch_sf, miles)
            
        elif car == 'scooter':
            print gas_stop % (car, range)
            print gas_full
            print scooter % (car, ', '.join(hitch_sf), range, next, miles)
            gas_sf_to_vegas(car, people, range, hitch_sf, miles)
            
        else:
            print gas_stop % (car, range)
            print gas_full
            print multi_seat % (car, hitch_sf, range, next, miles)
            gas_sf_to_vegas(car, people, range, hitch_sf, miles)
            
    elif miles - range <= 0:
        next = 'Las Vegas'
        if 'Tesla' in car:
            print battery_stop % (car, range)
            print battery_full
            print tesla % (car, ', '.join(hitch_sf), range, next, miles)
            bakers(car, people, range, hitch_sf, miles)
            
        elif car == 'scooter':
            print gas_stop % (car, range)
            print gas_full
            print scooter % (car, hitch_sf, range, next, miles)
            bakers(car, people, range, hitch_sf, miles)
            
        else:
            print gas_stop % (car, range)
            print gas_full
            print multi_seat % (car, hitch_sf, range, next, miles)
            bakers(car, people, range, hitch_sf, miles)
    
    else:
        "Error in gas_sf_to_vegas"


def bakers(car, people, range, hitch_sf, miles):
    print "\n---Bonus Round---\n---Bakersfield---\n"
    print "A guy named \"Mule\" joins your party wagon in",
    print "Bakersfield, CA. He claims to be packing the good shit."
    print "\nCurrent hitchhikers are: %s" % ', '.join(hitch_sf)
    print "Available hitchhikers in Bakersfield are: %s" % ', '. join(bakers_hitchhikers)
    
    hitch_sf.extend(bakers_hitchhikers)
    
    while True and len(hitch_sf) > people:
        try:
            print "Which hitchhikers to leave in the Mojave:",
            print "%s?" % ', '.join(hitch_sf)
            
            kick = raw_input(prompt)
            
            hitch_sf.remove(kick)
            
        except ValueError:
            print "Even hitchhikers like their name spelled correctly."
            print "Try again."

    hitch_bakers = hitch_sf
    
    if 'scooter' in car:
        print scooter % (car, ', '.join(hitch_bakers), range, next, miles)
        
    elif 'Tesla' in car:
        print tesla % (car, ', '. join(hitch_bakers), range, next, miles)
        
    elif people > 1:
        print multi_seat % (car, ', '.join(hitch_bakers), range, next, miles)
        
    else:
        print "Error at bakers"
        
    vegas(car, people, range, hitch_bakers, miles)
    

def vegas(car, people, range, hitch_bakers, miles):
    print "\n---Welcome to Las Vegas---\n"
    print "Time to give Big Daddy the ol' rain man sweep."
    
    
def dead(why):
    print why, "your ill-fated road trip is over. Visions of cards",
    print "and bottles and sugar plum strippers dance in your head."
    

def start():
    print """
                *** Roadtrip ***
    
    A Seattle-ite, a vehicle(s), and 1400 miles to Las Vegas.
    More coin to spend at the tables if you get there fast.
    More coin to spend on booze if you arrive with lots of people.
    Your roadtrip begins in Seaattle. 200 miles to first stop, Portland.
    Let the trip begin!
    """
    seattle()
    
    
start()

