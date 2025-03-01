# 68 Labels = an rea widget that holds text and/or an image within a window
from tkinter import *       #imports everything related the tkinter module

my_other_window = Tk()

my_photo_image=PhotoImage(file='image.png')  #get your photo image to add image to your label

my_label=Label(my_other_window, 
               text="Hello World", 
               font=('Arial', 40, 'bold'), 
               fg='#00FF00', 
               bg='black', 
               relief=RAISED, 
               bd=10, 
               padx=20, 
               pady=20,
               image=my_photo_image     #adds our photo image to label, but replaces all our text so we need to use compound option to place it
               compound='top'           #compound='botton' : image appears underneath out text. compound='top' image is places above our text.
               )
                 

#label constructor. label only takes up the room it needs
#arguments are: (master/container(the name of the window that will contain the label), you can add more arguemnts for customization) 
#Sample arguments
#text="text you ant on label"
#font=('Arial', 40, bold)
#fg is foreground which is the font color. can add hex or text value here. fg='#00FF00'
#bg is background color
#relief sets the border style. add a border around label. there is RAISED and SUNKEN
#bd changes the border width, default is 1
#padx and pady :we can also add padding between text and border


my_label.pack()                 #by default places you widget/label to the top center of the container
#my_label.place(x=0, y=0)        #change the coordinates of where the label is placed

my_other_window.mainloop()