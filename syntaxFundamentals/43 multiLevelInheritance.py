#43 Multi level inheritance - when a child class inherits another child class

class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print("this animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog=Dog()       #creating dog object
print(dog.alive)
dog.bark()
dog.eat()