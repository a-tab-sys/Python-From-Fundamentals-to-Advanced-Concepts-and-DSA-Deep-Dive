# 48 Abstract class
        #prevents user from creating an obect of that class
        #and compels user to override abstract methods in a child class
        #from abc import ABC, abstractmethod   : add this to beginning of program
            #Abstracts class: contains 1 or more abstract methods
            #Abstract method: methods has a declaraation but no implementation

#imagine that for a game you want the player to make an object of the car class 
#or mortorcycle class, but not from vehicle class because thats too generic.
#so we will make vehicle class abstract

class Vehicle(ABC):     #vehicle class inherits from ABC class. for all methods here add @abstractmethod
    @abstractmethod     #you cant remove this abstract method, bc then you can still create a vehicle object bc you need at least 1 abstract method
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

class Mortorcycle(Vehicle):
    def go(self):                     #if you forgot to add the go method to motorycle class you would get an error. child class must implement the parent abstract method
        print("You ride the mortorcycle")

#vehicle=Vehicle()      :gives error-TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract method 'go'  
car=Car()
motorcycle=Mortorcycle()

#vehicle.go()
car.go()
motorcycle.go()