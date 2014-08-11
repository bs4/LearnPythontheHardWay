people = 23
cars = 21
trucks = 22


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
    
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
    
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
    
# I think elif is "else if", meaning use another "if" statement if the
## first wasn't true
# I think "else" is a catch all for if none of the "if" or "elif" statements
## above it weren't true

if not(people < cars):
    print "Oops, more people than cars, let's walk."
elif not(people > cars):
    print "Ok, let's drive."
    
if people > cars + trucks:
    print "Too many bodies, not enough vehicles. Let's all walk!"
    
if cars > people and cars > trucks:
    print "Ok, let's drive cars."
elif trucks > people and cars > people:
    print "Trucks over cars this time."
elif trucks > people and cars < trucks:
    print "Yah-Hoo, Howdy, Ding-diddly-doink! Let's drive trucks."

else:
    print "Phooey, let's just walk."
    
# Did the study drills and answered the Common Questions (tested the
## "multiple elif's