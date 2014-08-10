# The subject of this example will be Kristen's kids entering her classroom in the morning

print "*Mrs. Smith opens the door*"
print "Good morning everyone. Welcome to a good Monday morning."
print "How are you this morning Bobby?",
bobby = raw_input()
print "And how are you Sally?",
sally = raw_input()
print "What day is today Wajinabi?",
wajinabi = int(raw_input())
print "Noah can you tell me what day it is?",
noah = int(raw_input())
print "So Bobby is %s this morning, Sally is %s this morning, Wajinabi's days is %s, and Noah's day is %s." % (
    bobby, sally, wajinabi, noah)
print "Together Wajinabi and Noah have %r days." % (wajinabi + noah)
print "Great to hear everyone, let's get started."