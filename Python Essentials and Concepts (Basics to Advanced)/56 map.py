#56 Map  - applies a function to each item in an iterable (list touple, etc)
# map()
# map (function, iterable)

store=[("shirts", 20.00),
       ("pants", 25.00),
       ("jacket", 50.00),
       ("socks", 10.00)]

    #to convert the above prices to euros or dollars
to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars=lambda data: (data[0], data[1]/0.82)
#store_euros=map(to_euros, store)   #map function will create a map object
store_euros=list(map(to_euros, store))  #but you could cast that to a different type of iterable
store_dollars=list(map(to_dollars, store)) 

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)