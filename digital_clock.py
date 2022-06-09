#Digital Clock Python Project
#This is Gui based project

from tkinter import *
from time import strftime               #We import strftime class from time package

def time():                             #In Function time() we are defining how to display the clock(format)  
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)             #Here we are using recursion to call the call after every second(1000ms)

#Here we are defining the gui of the cock
root = Tk()
root.title("Clock")
label=Label(root,font=("Congenial",80), background="black",foreground="cyan")
label.pack(anchor='center')

time()                                  #Calling time function

mainloop()                              #Closing the tkinter
