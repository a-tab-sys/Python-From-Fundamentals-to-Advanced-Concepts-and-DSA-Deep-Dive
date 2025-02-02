# 19 Dictionary - a changeable, unordeered collections of unique key: value pairs
#               - fast because they use hashing, allow us to access a value quickly
#               - (key: value)
capitals = {'USA' : 'Washington DC', 
            'India':'New Dehli', 
            'China': 'Beijing',
            'Russia' : 'Moscow'}
    
    #to print from dictionary using the key
    #if use a key that does not exist like Germany, you get error
    #use get method to avoid this
print(capitals['Russia'])
#print(capitals['Moscow'])  cant do this, you can only look up keys, moscow is a value

print(capitals.get('Germany')) #return None
print(capitals.keys())  #prints all the keys, not the values
print(capitals.values())    #prints all the values, not the keys

capitals.update({'Germany': 'Berlin'})      #add key, value pair to ditionary
capitals.update({'USA':'Las Vegas'})        #updates existing key with new value
capitals.pop('China')       #remove pair associated with china
capitals.clear()     #clears entire dictionary

print(capitals.items())     #displays everything in dictionary (keys and values)

for key,value in capitals.items():      #displays everything in dictionary (keys and values)
    print(key, value)