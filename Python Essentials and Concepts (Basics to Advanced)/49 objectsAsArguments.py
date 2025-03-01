# 49 Objects as Arguments
        # you can pass objects as arguments

class Car:
    color = None

class Mortorcycle:
    color = None

def change_color(car, color):      #seperate function (not method of clar class) outside of car class. want 2 parameters: car object and color. the name of parameter that accepts the car object (car) can be named smething else. just keep it lowercase, argument names should be lowercase
    car.color=color

car_1=Car()
car_2=Car()
car_3=Car()

bike_1=Mortorcycle()

print(car_1.color)
print(car_2.color)
print(car_3.color)

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)