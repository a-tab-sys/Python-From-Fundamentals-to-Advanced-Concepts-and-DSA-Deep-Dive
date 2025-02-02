#10 logical operators (and, or, not)
temp=int(input("What is the temprature outside?: "))

if not(temp>=0 and temp<=30):
    print("Stay in, bad temp")
elif not(temp<0 or temp>30):
    print("Go out, good temp")