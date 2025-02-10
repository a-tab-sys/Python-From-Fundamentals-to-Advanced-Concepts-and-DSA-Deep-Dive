# Patterns - Require nested loops - 4 rules


# (1) outer loop is for the rows
# (2) inner loop is focus on the columns and connect them with rows
# (3) printing will occur inside inner loop
# (4) observe symmetry [optional]


# Pattern 1 --------------------------------
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# for i in range (5):
#     for j in range(5):
#         print("*", end=" ")   
#     print("")


# Pattern 2 --------------------------------
# *
# * *
# * * *
# * * * *
# * * * * *
#My method
# s="* "
# for j in range(5):
#     print(s)
#     s=s+"* "
# print(" ")

#Better method
# rows = 5
# for i in range(1, rows+1):
#     print("* " * i)



# Pattern 3 ---------------------------------
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5 
k=""
for i in range (5):
    for j in range(1, 6):
        s=k+str(j)
        print(s)
    print("")



    


