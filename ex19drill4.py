print #blank line for spacing

def penny_equation(penny_dish, have_penny, need_penny):
    print "The dish has %d pennies in it." % penny_dish
    print "You give %d pennies." % have_penny
    print "You take %d pennies." % need_penny
    print "This leaves %d pennies in the dish.\n" % (penny_dish + (have_penny - need_penny))
    
    
print "Let's look at the dish, our giving and taking."
penny_dish = int(raw_input("How many pennies are in the dish? "))
penny_give = int(raw_input("How many pennies can you give? "))
penny_need = int(raw_input("How many pennies do you need? "))

penny_equation(penny_dish, penny_give, penny_need)


print "Let's do something more complex, raw_input inside a variable."
print "AKA the magic penny dish of multiplicity!\n"
penny_multiplier = 2
dish_start = int(raw_input("How many pennies can you count in the dish? "))
you_give = int(int(raw_input("How many pennies can you donate? ")) * int(penny_multiplier))
you_take = int(raw_input("How many pennies will you take? "))
penny_equation(dish_start, you_give, you_take)
print "WHOA!!! The magic dish doubled your donation!!!"
