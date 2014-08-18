def kid_qs(girl_name, boy_name, num_kids):
    print "Your daughter is %s." % girl_name
    print "Your son is %s." % boy_name
    print "You have %d children." % int(num_kids)
    
girl = raw_input("Who is your daughter? ")
boy = raw_input("Who is your son? ")
num = raw_input("How many kiddos' do you have? ")

kid_qs(girl, boy, num)