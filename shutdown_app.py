#Shutdown App Python Project
#This is a GUI based project

from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown -l")

def shut_down():
    os.system("shutdown /s /t 1")

st=Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st, text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st, text="Restart Time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st, text="Log-Out",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=log_out)
lg_button.place(x=150,y=270,height=50,width=200)

sd_button = Button(st, text="ShutDown",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shut_down)
sd_button.place(x=150,y=370,height=50,width=200)

st.mainloop()
