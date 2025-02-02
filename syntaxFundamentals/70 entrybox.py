# 70 Entrybox
#       entry widget = textbox that accepts a single line of user input
from tkinter import * 

def submit():
    username=entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)            #this allows you to disable the entry box after 1 username input, you can also set ACTIVE or DISABLED in constructor, see button example above

def delete():
    entry.delete(0, END)     #this delete function takes 2 arguments (whats the firsrt character to remove, last character to remove) so (0,END) takes first character to the end nd deletes it. <Name of entry box>.delete

def backspace():
    #entry.delete(END-1, END)
    entry.delete(len(entry.get())-1, END)      #get the second to last character by get the length of all characters in entry box and -1 from it

window=Tk() #creating window

entry = Entry(window,#constructor(master, other arguments)
            font=("Arial", 50),
            fg='#00FF00',       #foreground color, test color
            bg="black"          #background color
            show="*"            #when user put input in entrybox, you cn set it so that only a specific character shows on screen, if hey enter a password, only asterisks are visible
            )

#adding default text to entry box (<Positional argument:where to start the text>, "<text to display>" )
entry.insert(0, "Spongebob")



entry.pack(side=LEFT)       #displays the entrybox. side left you position it on left or right side

submit_button= Button(window, text="submit", command=submit)    #creating a submit buton to make use of entrybox
submit_button.pack(side=RIGHT)

delete_button= Button(window, text="delete", command=delete)    #creating a submit buton to make use of entrybox
delete_button.pack(side=RIGHT)

delete_backspace= Button(window, text="backspace", command=backspace)    #creating a submit buton to make use of entrybox
delete_backspace.pack(side=RIGHT)

window.mainloop()