# we can use a cue to simulate printing tasks being sent to a printer. tasks are to be placed into a cue to be processed first come, first serve.

# about 10 students are working at any given hour. 
# each student prints u to twice during that time. 
# they print about 1-20 pages. 
#printer is capable of processing 10 pages per minute of drat quality
# better quality prints would take 5 pages per minute
#we dont want students aiting too long

# there are 10 students in a lab and each prints twice, then there are 20 print tasks per hour on average. so lets find out whats the chance that at any given second, a print task will be created.

#20 tasks       1 hr        1min        1 task
#----------*-------------*-----------=----------
#1 hr           60 min      180 sec     180 sec

#so we have 1 tak every 180 seconds. so every 1 second you have a 1/180 chance of a print occuring. we can simulate this by gereating a random number btween 1 and 180 inclusive. if the number is 180 well say a task is created. it is possible that many tasks could be created in a row or we may wait quite a while for a task to appear. That is the nature of simulation. You want to simulate the real situation as closely as possible given that you know general parameters.

#todesign this we will create classes for the 3 real word objects: printer, task, printQueue



import random
from DSA.Queues.Queue_implement import Queue

# printer class tracks if it has a current task. need toidentify if its busy. needa to know amount of time needed to print based on number of pages.

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


#task class represents a single printing task. each task needs to keep a timestamp to be used to compute waiting time. timestamp will represent the time that the task was created and placed in the queue. wait time can be used to retieve the amount of time spent in the queue beofre printing begins
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


# Runs the simulation for a given number of seconds and printer speed.
def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            nexttask = print_queue.dequeue()
            waiting_times.append(nexttask.wait_time(current_second))
            lab_printer.start_next(nexttask)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    return num == 180


for i in range(10):
    simulation(3600, 5)