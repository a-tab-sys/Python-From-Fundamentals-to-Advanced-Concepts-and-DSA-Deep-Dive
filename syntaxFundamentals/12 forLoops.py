#12 For Loops - will execute a limited amount of times
for i in range(10):  #Excecutes 10 times
    print(i)         #shows 0-9

for index in range(10):
    print(index+1)    #shows 1-10

    #you can work index in a specific range
for index1 in range(50, 100):
    print(index1)           #shows 50-99.runs 50 times. first number is inclusive, second is exclusive

    #you can add a third number to this range to specify how much you want to count up or down by
for index2 in range(50, 100+1,2):   #shows 50-100 because of the +1, skips up by 2.
    print(index2)

for index3 in "Bro Code":
    print(index3)               #prints Bro Code   
  
    #For example below we will cound down and then say happy new year. need to import time module at start of program
for seconds in range(10, 0,-1):
    print(seconds)
    time.sleep (1)      #tells to sleep 1 sec between each iteration of for loop
print("happy new year")