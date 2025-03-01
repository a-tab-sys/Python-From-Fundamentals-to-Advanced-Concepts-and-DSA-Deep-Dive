#42 Inheritance - classes can inherit attributes or methods from another class
    # child class wil recieve eveyhting from parent class

class Animal:       #creating parent class
    alive=True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit (Animal):  # here you are saying Rabbbit is the child of Animal class, so it will inherit everyhting from animal class
    def run(self):
        print("this rabbit is runnning")
class Fish(Animal):
    def swim(self):
        print("this fish is swimming")
class Hawk(Animal):
    pass

rabbit=Rabbit()     #creating object rabbit from classes
fish=Fish()
hawk=Hawk()

print(rabbit.alive) #this has alive because we used inheritance
fish.eat()      #got this method from inheritance
hawk.sleep()    #got this method from inheritance

rabbit.run()
fish.swim()