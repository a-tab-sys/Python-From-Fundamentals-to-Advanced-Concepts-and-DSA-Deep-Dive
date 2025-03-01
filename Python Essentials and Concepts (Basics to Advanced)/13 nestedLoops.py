#13 Nested loops - inner loop will finish all its iterations before finishing one iteration of outer loop

    #making  program that draws a rectangle of centain symbol - inner loop in charge of columns

rows=int(input("How many rows?: "))
columns=int(input("How many columns?: "))
symbol=input("enter a a symbol to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")       #once youve printed the collumn symbols, you dont want your cursor to move to next line so add this end="" to avoid that
    print()                         #this moves cursor to next line
