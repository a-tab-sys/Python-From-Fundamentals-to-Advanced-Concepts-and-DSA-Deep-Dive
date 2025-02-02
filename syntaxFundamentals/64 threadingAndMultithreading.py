# 64 threading, multithreading
        #thread - is a flow of execution. each thread can carry out a seperate order of instructions
        #multithreading allows us to run different parts of a program at different times
        #each thread takes a turn running due to GIL to achiece concurrency
        
        #GIL = global interpreter lock
        #allows only one theard to hold the control of the pythin interpreter at any one time

#programs and tasks can be divided into 2 caegores: cpu bound, io bound  
   
    #cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
    # use multiprocessing

    #io bound = program//task spends most of its time waiting for external events (user input, web scraping)
    # use multithreading

#import threading
#import time

#an example where mutithreading is used is in that quiz game you made earlier
#you could have had a count down going while waiting fro user input (io bound task)
#1 thread would be waitng for user input and 1 thread would be in charge of a countdown timer
#2 threads would be running concurrently in above example


#imagine you have 3 tasks to complete in the morning before work

def eat_breakfast():
    time.sleep(3)           #time takes 3 seconds
    print("you finished breakfast")

def drink_coffee():
    time.sleep(4)
    print("you finished coffee")

def study():
    time.sleep(5)
    print("you finished studies")

#these tasks are spending time waiting for externl events, waiting for the sleep functions to expire
#below we complete these tasks sequencially not concurrently
#we have 1 thread in charge of the three seperate functions here
#eat_breakfast()
#drink_coffee()
#study()


#lets get these function running concurrently: because humans can multitask
#lets create 3 thread, each thread in charge of each task with main thread reunning in background to complete the rest of the program
#main thread just runs like normal, start immediatly and runs like normal. its not taking care of these 3 function but its going to run the enumerate and active call, perf_counter functions normally

x=threading.Thread(target=eat_breakfast)
#x=threading.Thread(target=eat_breakfast, args=(1,))       if your function had arguments that need to be passed in, add in the arguments followed by a comma
x.start()       #to start the thread

y=threading.Thread(target=drink_coffee)
y.start()

z=threading.Thread(target=study)
z.start()

#there is something called thread synchronization, we can have the main thread wait for another thread to finish before completing its instruction
x.join()    #now main thread has to wait for these threads to synchronize to move on with its own instruction
y.join()
z.join()

#whenever we run a program we have one thread running that is in chanrge of executing our program
#we can count the number of threads currently active in the background
print(threading.active_count()) #prints number of active threads in program

print(threading.enumerate())    #prints a list of all threads that are running

print(time.perf_counter())  #tells us how long it takes our calling thread (main thread) to finish its set of instructions