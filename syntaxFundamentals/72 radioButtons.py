# 72 Radio Buttons = similar to checkbox but you can only select 1 from a group
from tkinter import*

#makeing a list
food=["pizza", "hamburger", "hotdog"]

def order():
    if (x.get()==0):
        print("you ordered pizza")
    elif (x.get()==1):
        print("you ordered hamburger")
    elif (x.get()==2):
        print("you ordered hotdog")
    else:
        print("huh?")

window=Tk()

x=IntVar()      #should be created within the instance of the window

pizzaImage=PhotoImage(file='image copy.png')
HamburgerImage=PhotoImage(file='image copy 2.png')
HotdogImage=PhotoImage(file='image copy 3.png')
foodImage=[pizzaImage, HamburgerImage, HotdogImage]

for index in range(len(food)):           #will iterate once through all lements in our list, will create 3 radiobuttions for us
    radiobutton=Radiobutton(window, 
    text=food[index],       #adds text to radio buttons
    variable=x,             #since x is associated with all the list elements, when you select 1 checkbox you automatically select them all, same thing when you deselect...Groups radiobuttons together if they share a variable
    value=index,            #asssigns each radiobutton a different value. we need to give each radion button its own value, so make value=index
    padx=25,                #adds padding on x axis
    font=("Impact", 50),
    image=foodImage[index],     #adds image to radiobutton
    compound = "left",     #adds image left of text
    indicatoron=0,      #eliminates circle indicators
    width=375,     #sets width of radiobuttons
    command=order   )    #set command of radiobuton to funtion
    radiobutton.pack(anchor='w')    #by default radiobuttons are centered, lets anchor them to the West

window.mainloop()