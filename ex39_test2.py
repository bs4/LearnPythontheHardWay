import hashmap2
dashes = '-' * 10
# create a mapping of state to abbreviation
states = hashmap2.new()
hashmap2.set(states, 'Oregon', 'OR')
hashmap2.set(states, 'Florida', 'FL')
hashmap2.set(states, 'California', 'CA')
hashmap2.set(states, 'New York', 'NY')
hashmap2.set(states, 'Michigan', 'MI')
hashmap2.set(states, 'Washington', 'WA')
hashmap2.set(states, 'Nevade', 'NV')


# create a basic set of states and some cities in them
cities = hashmap2.new()
hashmap2.set(cities, 'CA', 'San Francisco')
hashmap2.set(cities, 'MI', 'Detroit')
hashmap2.set(cities, 'FL', 'Jacksonville')
hashmap2.set(cities, 'WA', 'Olympia')
hashmap2.set(cities, 'WA', 'Seattle')
hashmap2.set(cities, 'WA', 'Bothell')
hashmap2.set(cities, 'WA', 'Everett')

# add some more cities
hashmap2.set(cities, 'NY', 'New York')
hashmap2.set(cities, 'OR', 'Portland')

print len(cities)

# print out some cities
print dashes
print "NY State has: %s" % hashmap2.get(cities, 'NY')
print "OR State has: %s" % hashmap2.get(cities, 'OR')
print "WA State has: %s" % hashmap2.get(cities, 'WA')

# print some states
print dashes
print "Michigan's abbreviation is: %s" % hashmap2.get(states, 'Michigan')

print "Florida's abbreviation is: %s" % hashmap2.get(states, 'Florida')


# do it by using the state then cities dict
print dashes
print "Michigan has: %s" % hashmap2.get(cities, hashmap2.get(states, 
'Michigan'))
print "Florida has: %s" % hashmap2.get(cities, hashmap2.get(states, 
'Florida'))

# print every state abbreviation 
print dashes
hashmap2.list(states)

# print every city in state
print dashes
hashmap2.list(cities)

print dashes
# by default ruby says "nil" when something isn't in there
state = hashmap2.get(states, 'Texas')
state = hashmap2.get(states, 'Washington')
state = hashmap2.get(states, 'Alaska')

if not state:
    print "Sorry, no Texas."
    
# default values using ||= with the nil result
# can you do this on one line?
#city = hashmap2.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % hashmap2.get(cities, 'TX', 'Does Not Exist')

print "The city for the state 'WA' is: %s" % hashmap2.get(cities, 'WA', 'Does Not Exist')

print "The city for the state"