#44 multiple inheritance - child class is derived from more than 1 parent class

class Prey:

    def flee(self):
        print("This animanl flees")
    
class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()
#type fish. , hawk. , rabbit. to see all the classes it has access to