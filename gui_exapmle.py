#!/usr/bin/python

#################################
#      File : gui_exapmles using tkinker
#      Name : Sifa Gakeni
#      Date : 07 / 06 /2022
#################################

#buttons
#labels - txt
from cProfile import label
from tkinter import *

window = Tk()
window.title("HELLO welcome to your happy place")
window.configure(bg='teal')
window.geometry("400x400") #fix the window size
#setting labels
f_name = Label(window, text="First name", font=("Georgia",20))
s_name = Label(window, text= "Second name", font=("Georgia",20))

f_name.grid(column = 60, row = 100)
s_name.grid(column = 60, row = 120)

#how to put a popup
def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up window")
    top.configure(bg='lightorange')
    msg= label(top,text="Welcome to pop up",font=('mistral 18')).place(x=150,y=150)

#placing buttons
button = Button(window,text = "Click Me",bg='navyblue',fg='lightblue',command=open_popup().pack())
button.grid(column =100,row= 180)
#insering a textbox
f_name_box = Entry(window,width=12)
f_name_box.grid(column=100,row=100)

f_name_box = Entry(window,width=30)
f_name_box.grid(column=100,row=120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up window")
    top.configure(bg='lightorange')
    msg= label(top,text="Welcome to pop up",font=('mistral 18')).place(x=150,y=150)

window.mainloop()