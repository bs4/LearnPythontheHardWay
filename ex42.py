## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass
    
## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name of some sort
        self.name = name 
        
## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat has-a name of some sort
        self.name = name
        
## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## Person has-a name of some sort
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## Employee has-a name the same as Person
        super(Employee, self).__init__(name)
        ## Employee has a salary of some amount
        self.salary = salary
        
## Fish is-a object
class Fish(object):
    pass
    
## Salmon is-a Fish
class Salmon(Fish):
    pass
    
## Halibut is-a Fish
class Halibut(Fish):
    pass
    

## rover is-a Dog and has-a name "Rover"
rover = Dog("Rover")

## satan is-a Cat and has-a name "Satan"
satan = Cat("Satan")

## mary is-a Person and has-a name "Mary"
mary = Person("Mary")

## mary has a pet satan, see above 'satan'
mary.pet = satan

## frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover that is-a Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon 
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()









