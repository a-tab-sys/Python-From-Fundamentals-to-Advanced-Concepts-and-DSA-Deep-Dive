# 55 sort iterables
        #sort() method= used for lists only
        #sort() funtion= used with iterables (lists, touples, etc)

#sort method
students = ["Squidward", "Sandy", "Parick", "Spongebob", "Mr.Krabs"]    #list
 
    #sort list in alphabetical order
students.sort()
for i in students:
    print(i)

    #sort list in reverse alphabeticaal order
students.sort(reverse=True)
for i in students:    
    print(i) 

#sort function
students2=("Squidward", "Sandy", "Parick", "Spongebob", "Mr.Krabs")   #touple

sorted_students=sorted(students2)   #returns a list: sorted_students=, but allows you to sort a touple
for i in sorted_students:    
    print(i) 

sorted_students=sorted(students2, reverse=True)   #sorts in everse order
for i in sorted_students:    
    print(i) 

#more complicated example- list of touples (name, grade, age)
students3=[("Squidward", "F", 60),
           ("Sandy", "A", 33),
           ("Squidward", "D", 36),
           ("Squidward", "B", 20),
           ("Squidward", "C", 78)]


students3.sort()    #sort alphabetically. by default sorts by first column which is the name here

    #if we want to sort by grade or name we can use keyword arguments. here we sort by grade
grade=lambda grades:grades[1]       #set index of 1 for first column. index 0 is the name, 1 is the grade, 3 is the age
students3.sort(key=grade)

for i in students3:    
    print(i) 

#sort by age
age=lambda ages:ages[2]       #set index of 1 for first column. index 0 is the name, 1 is the grade, 3 is the age
students3.sort(key=age)
#students3.sort(key=age, reverse=True)

for i in students3:    
    print(i) 


#more complicated example- touple of touples (name, grade, age)
#since its ouple, cant use sort function as that belongs to lists only
students4=(("Squidward", "F", 60),
           ("Sandy", "A", 33),
           ("Squidward", "D", 36),
           ("Squidward", "B", 20),
           ("Squidward", "C", 78))
age=lambda ages:ages[2]
sorted_students=sorted(students4, key=age)

for i in sorted_students:
    print(i)