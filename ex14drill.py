from sys import argv

script, user_name, current_mood = argv
prompt = "> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Though, they may be tough considering your %s mood." % current_mood
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, %r due to you being in a %r mood,
you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (user_name, current_mood, likes, lives, computer)