# 61 Zip function - aggregates elements from 2 or more iterables(list, tuples, sets, etc.)
                    #creates a zip object with paired elemens stored in tuples for each element
                    # zip(*iterables)
usernames = ["Dude", "Bro", "Mister"]       #list of usernames
passwords = ("p@ssword", "abc123", "guest") #tuple of passwords
login_date=["1/1/2021", "1/2/2021", "1/3/2021"]

#users is the zip object. zip objects are iterable
users = zip(usernames, passwords)   #we have created a zip object of tuples, and each touple is storing a pair from the 2 iterables we provided

print(type(users))
for i in users:
    print(i)

users2 = list(zip(usernames, passwords))    #you can cast it to a list. now we have a list of tuples. each tuples is storing a pair

print(type(users2))
for i in users2:
    print(i)

users3 = dict(zip(usernames, passwords))    #since we are only passing in 2 iterables, we can cast as dictionary, so its storing key value pairs

print(type(users3))
for key, value in users3.items():
    #print(key, value)
    print(key+" : "+ value) #add colon for readability

#example with 3 iterables
users4=zip(usernames, passwords, login_date)
for i in users4:
    print(i)