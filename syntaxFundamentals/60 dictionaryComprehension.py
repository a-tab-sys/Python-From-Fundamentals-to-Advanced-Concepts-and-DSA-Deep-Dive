# 60 Dictionary Comprehension - create a dictionary using an expression
                                #can replace for loops and certain lambda functions
                                #dictionary = {key: expression for (key, value) in iterable}
                                #dictionary = {key: expression for (key, value) in iterable if conditional}
                                #dictionary = {key: (if/else) for (key, value) in iterable}
                                #dictionary = {key: function(value) for (key, value) in iterable}


cities_in_F = {'New York':32, 'Boston':75,'Los Angeles':100, 'Chicago':50 } #created dictionary. city names are keys. tem in farenheit are values

#we gonna create a seperate dictionary that has the tem in celcius using dictionary comprehension. also we added round function
cities_in_C={key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

#example using an if conditional
weather = {'New York': "snowing", 'Boston':"sunny", 'Los Angeles': "sunny"}
sunny_weather= {key: value for (key, value) in weather.items() if value =="sunny"}

print(sunny_weather)

#exaple with if/else conditional
cities = {'New York':32, 'Boston':75,'Los Angeles':100, 'Chicago':50 } #created dictionary. city names are keys. tem in farenheit are values
desc_cities={key: ("warm" if value >= 40 else "COLD") for (key, value) in cities.items()}

#emample calling a function
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69>=value>=40:
        return "WARM"
    else:
        return "COLD"

cities2 = {'New York':32, 'Boston':75,'Los Angeles':100, 'Chicago':50 } #created dictionary. city names are keys. tem in farenheit are values
desc_cities2={key: check_temp(value) for (key, value) in cities2.items()}

print(desc_cities2)