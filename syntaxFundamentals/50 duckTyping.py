# 50 Ducktyping - concept where the class of an object is less important than
        # the methods or attributes of the class.
        #class type is not checked if minimum methods/attributes are present
        #if it walks like a duck, and quacks like a duck it must be a duck

class Duck:
    def walk(self):
        print("this duck is walking")
    
    def talk(self):
        print("this duck is qwacking")

class Chicken:
    def walk(self):
        print("this chicken is walking")
    
    def talk(self):
        print("this chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(duck)
person.catch(chicken)   #this works  bc python is seeing the same methods so it lets you pass an object of another class. chicken can walk and talk like duck so its basically a duck
                        #if chicken had different methods or was missing a method that duck has this would not work