from sys import argv

sprinkles = raw_input("How many sprinkles would you like? ")

script, ice, cream, cone, topping, sprinkle_multiplier = argv

print "The script is called:", script
print "Your first variable is:", ice
print "Your second variable is:", cream
print "Your third variable is:", cone
print "Your fourth variable is:", int(sprinkle_multiplier)

print "Then I'll multiply those sprinkles by 5!"
print "This gives you %r sprinkles! Ah hahahahahaha!" % (int(sprinkle_multiplier) * int(sprinkles))

cherry = raw_input("What is your favorite topping? ")

# I used 'python ex13drill.py ice cream cone topping 5' on cmd line