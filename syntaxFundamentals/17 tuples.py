#17 Tuples - similar to lists. collections which are ordered and unchangeable
#            used to group together related data

student = ("Bro", 21, "male")
print(student.count("Bro")) #shows how many times bro apperars in touple
print(student.index("male"))    #shows what index male is at

print(student)

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")