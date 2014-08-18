print #blank line for spacing

def pennies(have_penny, need_penny):
    print "Have a penny? Give %d pennies." % have_penny
    print "Ah, Ol' Abe would be so proud."
    print "Need a penny? Take %d pennies." % need_penny
    print "Tut tut, GW never told a lie!\n"

    
print "I have pennies to give."
pennies(3, 0)


print "I need a penny, please."
pennies(0, 1)


you_give = int(raw_input("How many pennies can you give? "))
pennies(you_give, 0)


you_take = int(raw_input("How many pennies do you need? "))
pennies(0, you_take)


print "Let's add our pennies up and give the total sum."
my_pennies_give = 3
you_pennies_give = 6

pennies(my_pennies_give + you_pennies_give, 0)


print "Now, let's rob all the penny dish has."
my_pennies_take = 8
you_pennies_take = 13

pennies(0, my_pennies_take + you_pennies_take)


print "After giving and taking lets see how many pennies I have."

pennies(