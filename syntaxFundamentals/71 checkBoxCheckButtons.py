# 71 Checkbox/Checkbuttons 

from tkinter import*

def display():
    if(x.get() == 1):          # if x was storing boolean do if(x.get()): this will return true or false. if x was storing string do if(x.get()=="YES"):
        print("You agree")
    else:
        print("You dont agree :(")

window=Tk()

x=IntVar()      #IntVar(). if the variable x returned a string we would do x=StringVar(). if returned boolean do x=BooleanVr(). you would use onvalue and offvalue in constructor to change it to store a string, by default it stores 1 and 0
                #IntVar() is a variable in clas Tkinter. holds integer values for varios widget operations
                #should be created within the instance of the window

photo_photoimage=PhotoImage(file="image.png")

check_button = Checkbutton (window,
                            text="I agree to smth",
                            variable=x,      #associating variable with checkbutton, checkbutton stores 1 or 0 by default
                            #onvalue=1,      #lets you change what value represents on. by default it uses 1 for on and 0 for off
                            #offvalue=0,
                            command=display,
                            font=('Arial', 20),
                            fg='#00FF00',
                            bg='black',
                            activeforeground='#00FF00',
                            activebackground='black',
                            padx=25,
                            pady=10,
                            image=photo_photoimage,
                            compound='left')        #placing image left of text

check_button.pack()

window.mainloop()