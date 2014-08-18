def math_time(subject, name_1, num_1, name_2, num_2, name_3, num_3):
    print "Ahem, hmmhmm. Today's topic is %s." % subject
    print "We have %d %s." % (int(num_1), name_1)
    print "We have %d %s." % (int(num_2), name_2)
    print "We have %d %s." % (int(num_3), name_3)
    print "Whoa that's a lot!"
    print "It'll be more fun than a barrel of monkeys, or a barrel of %s\'s at any rate! Whooo! \n" % subject

subject = raw_input("What topic would you like to talk about today? ")
object1 = raw_input("What object within that subject interests you? ")
object1_num = raw_input("And how many of that object do we have? ")

math_time(subject, object1, object1_num, "blast", "4", "gloves", "5")