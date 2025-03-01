# 69 Buttons = you click it, then it does stuf
from tkinter import *       #imports everything related the tkinter module

count=0                     #variable to count number of times button is clicked

def click():
    global count            #you need to add that its global : im not sure why, find out
    count+=1
    print(count)

window=Tk()

photo=PhotoImage(file='image.png')

button = Button(window,                     #button constructor(master, other arguments)
                text="click me",            #add text on button
                command=click,              #we need to set a command to make the buton do something. we need to give command a function name. this is called a call back because you give it the function name without the parenthesis
                font=("Comic Sans", 30),    #change font of button, and size of button
                fg="#00FF00",               #set the foreground color (font color). put color name or hex code
                bg="black",                 #background color
                activeforeground="#00FF00", #activeforeground, activebackground. allow you to select color scheme for hile button is pressed. you have set some specifications for how the button color should look, when you click the button the color scheme changes while the button is pressed
                activebackground='black',
                state=ACTIVE,               #state can be ACTIVE or DISABLED. DISABLED if you need to disable someone from clicking on this button
                image=photo,                 #to add an image to a button, however this will replace the text                                           
                compound='bottom' #use to have text an image on the button
                )     

button.pack()       #displays the button

window.mainloop()