# 66 THIS IS NOT WORKING FOR ME, RETURN TO THIS
# 66 Multiprocessing - running tasks in parallel on different cpu cores, bypasses GIL used for threading
                        #multiprocessing = better for cpu bound tasks (heavy cpu usage)
                        #mutithreading = better for io bound tasks(waiting around) - limited to running 1 thread at a time bc of GIL

#from multiprocessing import Process, cpu_count
#import time


def counter(num):       #this is the function we will call with the processes we create. child process
    count=0
    while count<num:
        count+=1

def main ():
    a= Process(target=counter, args=(10000,))  #create a process, for arguments you have to pass in  tuple. 
    a.start                                            #since we only have 1 rgument to pass in, to diffrenciate from an expression we add a comma at the end
    a.join()            #main process will wait for child process before continuing

    print("finished in: ",time.perf_counter(), "seconds")

# if you are running windows processing sytem, add the below line because
#when we run  program we have a main process that is runnning
#if we create a child process from that process, its going to copy the module we are working with
#that child process will create its own children process and this can be a problem
if __name__ == 'main':
    main()