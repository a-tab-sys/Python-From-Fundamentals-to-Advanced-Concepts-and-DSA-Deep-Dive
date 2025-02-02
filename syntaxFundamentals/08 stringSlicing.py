#08 String Slicing - create  substring by extracting elements from another spring
#   indexing[] or slice[]
#   [start:stop:step]       indexing starts at 0. start index num is inclusive, end index number is exclusive, default for step is 1, that just normal writing

name='Bro Code'
print(name[0])

first_name=name[:3]         #[0:3]      , leave start index empty=default is index 0

last_name=name[4:]          #[4:8]      , leave stop index empty=default is end of string

funky_name=name[::2]        #[0:8:2]

    #reverse string in python
reversed_name=name[::-1]    #[0,8,-1]   , because step of 1 is just regular writing, so -1 is reverse writing

print(first_name)
print(last_name)
print(funky_name)

    #create a substring based on website name indexing (0...1...2...) (3...2...1)
website="http://google.com"
slice = slice(7, -4,)
print(website[slice])
