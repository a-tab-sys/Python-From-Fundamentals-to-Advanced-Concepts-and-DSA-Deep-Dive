# 63 time module
    # import time module

print(time.ctime(0))        #print epoch - a date and time from which a computer measures system time
                            #kinda like the date/time your computer thinks time began, used as a reference point
                            #vary based on computer/OS
                    
                            #converts a time expressed in seconds since epoch to a readable string

print(time.ctime(1000000))  #returns the data/time 1000000 after epoch

print(time.time())          #return how many seconds passed since epoch at the time program is ran

print(time.ctime(time.time()))  #combine above 2 methds to get crrent date and time

#another way to get current date/time
time_object = time.localtime()      #localtime method creates a time object based on curent time so time_object is a time object variable
print(time_object)      #you can change formatting to be more readable, we will use strftime(format, timeObject) function to help

#time.strftime(format, time_object)   #takes format nd time object as arguments
                                    #format is a string of different directives: see python official documentation on time module strf time function
                                    # many different directives that represent different time formats, see documentation to pick the type of formatting you want
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) 
print(local_time)

#you can also get UTC time: Coordianted Universal TIme is the primary time standard by which the world regulates clocks and time
time_object2 = time.gmtime()
print(time_object2)

#strp time function - parses a string representation of a time and/or date and return a time object
time_string="20 April, 2020"
#time.strptime(string, format)          accepts 2 arguments(time represented as string, and telling the computer the formating directives of the time string, this function creates a time object
time_object3=time.strptime(time_string, "%d %B, %Y")
print(time_object3)      #output is not so east to read, you can change that as we learned earlier

#asctime(t) function - accepts 1 arument: a tuple representation of a time
#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst). dst is -1 or 0
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string=time.asctime(time_tuple)
print(time_string)

#mktime(t) function - accepts 1 arument: a tuple representation of a time or a time object and converts it to a seconds since epoch
#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst). dst is -1 or 0
time_string2=time.mktime(time_tuple)
print(time_string2)