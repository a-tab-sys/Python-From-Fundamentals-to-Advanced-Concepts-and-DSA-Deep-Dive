#46 Method Chaining - calling multiple methods sequencially
    #each call performs an action on the same object and returns self
    #if you want to use method cahining you have to return something, because pyhon automatically returns none

class Car:
    def turn_on(self):
        print("you start the engine")
        return self
    
    def drive(self):
        print("you drive the car")
        return self

    def brake(self):
        print("you step on the brake")
        return self
    
    def turn_off(self):
        print("you turn off the engine")
        return self

car=Car()
car.turn_on()
car.drive()

    #i want to call these 2 sequencially, but to do below i will have to add return statements
car.turn_on().drive()   #without adding the return stemements you get this error: AttributeError: 'NoneType' object has no attribute 'drive'