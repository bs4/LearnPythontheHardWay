# create a mapping of state to state abbreviation
dashes = '-' * 10 
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
        
# print every state abbreviation
print dashes
for state, abbrev in states.items(): # items returns list of dict's (key, value) pairs
    print"%s is abbreviated %s" % (state, abbrev)
        
# print every city in a state 
print dashes
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
    
# now do both at the same time
print dashes
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
   
print dashes
# safely get an abbreviation by state that might not be there
state = states.get('Texas') # return the value for key if key is in the dict, else return value of default
                            ## if no default, default == none, so that this method never raises a KeyError
                            ## get(key[, default])
        
if not state:
    print "Sorry, no Texas."
    
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city 
        
        
        
        
        
        
        

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
