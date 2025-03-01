#67 GUI Windows
from tkinter import *       #imports everything related the tkinter module

#windows = serves as a container to hold or contain these widgets
#widgets = GUI elements: buttons, textboxs, labels, images

#we will create a new window
my_window=Tk() #instanciate an instance of a window for us

#we want to customize the appearance of the window
my_window.geometry("420x420")       #set the size of the window

my_window.title("Bro Code first GUI program")       #retitles the window from tk

#change the icon of the window bar at the top from feather icon
#copy paste image into your project folder. the image format is currently unreadable for Tkinter
#we need to convert our image into a photo image
icon_photoimage=PhotoImage(file='image.png')        #converts our image to  photo image, can also get image from desktop with file path
my_window.iconphoto(True, icon_photoimage)      #this sets the icon image, 2 arguments(True, name of your photoimage). true is always set to true.

my_window.config(background='Black')                   #change the background color of the window
my_window.config(background="#5cfcff")                  #can also change backgroung clor with a hex value, add a # before the hex color code

my_window.mainloop()       #to display the window, place window on computer screen, listen for events