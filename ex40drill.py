class Song(object):

    def __init__(self, lyrics):
#        print "TEST 1"
#        print lyrics
        self.lyrics = lyrics
#        print "TEST 2"
        
    def sing_me_a_song(self):
#        print "TEST 3"
        for line in self.lyrics:
#            print "TEST 4"
            print line
#            print "\nnewline\n"
#            print "TEST 5\n"
            
    happy = "If you're happy and you know it, clap your hands."

            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
                   
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
                        
                        
just_strings = Song(['A', 'B', 'C', 'D'] + [1, 2, 3])                        


var_pass = ['A', 'B', 'C', 'D', 1, 2, 3]

                        
happy_bday.sing_me_a_song()

print '-' * 10

bulls_on_parade.sing_me_a_song()

print '-' * 10

print Song.happy

print '-' * 10

print just_strings.sing_me_a_song()

print '-' * 10

v = Song(var_pass)

v.sing_me_a_song()

print '-' * 10

# pass a variable to the class

nirvana_come = ['Come as you are, as you were', # here's the variable
                'As I want you to be',
                'As a friend, as a friend',
                'As an old enemy.'
                'Take your time, hurry up',
                'The choice is yours',
                'Don\'t be late',
                'Take a rest as a friend',
                'As an old memory']
                
come_as_you = Song(nirvana_come) # here's passing the variable (object)
                                 # to the class
                             

come_as_you.sing_me_a_song() # here's using second function in class


























