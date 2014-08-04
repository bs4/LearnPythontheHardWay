# The below line gives the variable "cars" a value of 100;
# *NOTE* the variable has to be written outside the "" to not be printed as a word, but instead as the value given to it 
cars = 100
# The below line gives the variable "space_in_a_car" a value of 4.0
space_in_a_car = 4
# The below line gives the variable "drivers" a value of 30
drivers = 30.0
# The below line gives the variable "passengers" a value of 90
passengers = 90
# The below line gives the variable "cars_not_driven" a value of variable "cars" minus variable "drivers"
cars_not_driven = cars - drivers
# The below line gives the variable "cars_driven" the same value as variable "drivers"
cars_driven = drivers
# The below line gives the variable "carpool_capacity" a value of variable "cars_driven" multiplied by variable "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car
# The below line gives the variable "average_passengers_per_car" a value of variable "passengers" divided by variable "cars_driven"
average_passengers_per_car = passengers / cars_driven


print
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print

# Study Drills
# python kicked back an error in line 8 of Zed's first attempt in doing ex4.
# Zed made a couple mistakes
# One mistake was that he used the variable "car_pool_capacity" which wasn't defined, there is an extra _ between car and pool, so it doesn't exist
# Another mistake is that the math would be wrong for what we are looking for. Zed wanted average_passengers_per_car which should be passengers divided by cars_driven, like in the final draft of ex4
# Zed's first attempt in line 8 was figuring out total carpool_capacity divided by passengers, which returns a value of 1.33333333, giving us capacity divided by passengers, it doesn't tell us how many
# ...people we need to fit in each car to have them all transported.

# Study Drill 1
# In line 5, space_in_a_car = 4.0, if 4.0 is changed to 4, the only stuff affected are equations where the variable "space_in_a_car" is used...but does it go beyond one iteration?
# ...Yes, it does, if drivers is changed from 30 to 30.0, it effects "cars_driven" and then effects "carpool_capacity" and "average_passengers_per_car" making them all floating point numbers

