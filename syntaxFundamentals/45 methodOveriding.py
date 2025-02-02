# 45 Method Overiding - child class provides a specifir implementtion of a method it has inherited 
    #see the eat class is overwritten specifically in cls rabbit.
class Animal:
    def eat(self):
        print("this animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()