#09 if statements
age=int(input("How old are you: "))

if age==100:
    print("you are a century old")
elif age>=18:
    print("you are an adult")
elif age<0:
    print("you have not been born")
else:
    print("you are a child")
