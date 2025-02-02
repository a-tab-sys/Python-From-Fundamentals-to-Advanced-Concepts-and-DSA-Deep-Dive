# 65 daemon threads
            #a thread that runs in the background, not important for the program to run
            #your program will not wait for daemon threads to complete before exiting
            #non daemon threads cannot normally be killed, stay alive until task is complete

            #ex. background tasks, grbage collection, waiting for input, long running process

#import threading
#import time

#we have 2 threads, our main thread will wait for user input, in the backgroud we will have a thread with a timer dislaying how long someone is logged in
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count,"seconds")

#x=threading.Thread(target=timer)       #normal thread
x=threading.Thread(target=timer, daemon=True)   #daemon thread
x.start()

#x.setDaemon(True)  this method lets you set false or true depending on if you want it to be daemon or non daemon
                    #you cant change it if its currently running, this needs to be set before the start function

#print(x.isDaemon)   #return whether or not the thread is a daemon thread


answer=input("do you wish to exit?")

#now with normal threads even if you put some input and hit enter, the main thread is complete
#but my background timer is still going
#what if i want to to close the program?
#non daemon threads cannot normally be killed, stay alive until task is complete
#for this i will need to use daemon threads