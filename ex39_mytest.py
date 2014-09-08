import hashmap2

dashes = '-' * 14

states = hashmap2.new()
hashmap2.set(states, 'Washington', 'WA')
hashmap2.set(states, 'Oregon', 'OR')
hashmap2.set(states, 'Idaho', 'ID')

cities = hashmap2.new()
hashmap2.set(cities, 'WA', ['Seattle', 'Tacoma', 'Bothell'])
hashmap2.set(cities, 'WA', 'Tacoma')
hashmap2.set(cities, 'OR', 'Portland')
hashmap2.set(cities, 'OR', 'Salem')
hashmap2.set(cities, 'ID', 'Boise')
hashmap2.set(cities, 'ID', 'Twin Falls')

print 'states', states
print dashes
print 'cities', cities

print dashes
print "WA State has cities: %s" % ', '.join(hashmap2.get(cities, 'WA'))
print "WA State also has cities: %s" % hashmap2.get(cities, 'WA')

print "Washington State has: %s" % ', '.join(
    hashmap2.get(cities, hashmap2.get(states, 'Washington')))