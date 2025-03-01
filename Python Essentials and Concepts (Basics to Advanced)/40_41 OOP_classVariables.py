#40 Object Oriented Programming, #41 Class Variables
    # an object is an instance of a class
    #you can create a new class here or you could create it in a seperate module and import it here
    #objects hve attributes and methods(what object can do)
    #class variable set all instances of the class, all car objects. so all car objects will have 4 wheels. 
    #Instance variable are deined inside the constructor(inside this: def __init__(self, make, model, year, color):), can differ for all objects, class variable dont differ
class Car:         #object

    wheels= 4   #class variable

    def __init__(self, make, model, year, color):      #special method that constructs objects for us
        self.make=make   #attribute. Instance variable. self. refers to the object we are surrently woking on/creating
        self.model=model    #instance variable
        self.year=year  #instance variable
        self.color=color    #instance variable

    def drive(self):        #Method. self is 1 argument, it refers to the object using this method
        print("This " +self.model+ " is driving")
    
    def stop(self):
        print("This "+self.model+" has stopped")


car_1 = Car ("Chevy", "Corvette", 2021, "blue") #you dont need to pass anyhting for the self argument, this is done automatically
car_2 = Car ("Ford", "Mustang", 2022, "red") #you dont need to pass anyhting for the self argument, this is done automatically

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()           #see how () is empty you did not call self
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()           #see how () is empty you did not call self
car_2.stop()

car_1.wheels = 2        #you can change the clas variable for a particular object
print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)       #(name of class, name of class variable) to display its value
#print(Car.color)       #cant do this because its an instance varioable

Car.wheels=2 #this will change the class variable for all instances of the class
print(car_1.wheels)
print(car_2.wheels)