from tkinter import *
master = Tk()
master.geometry('350x200')
var1 = IntVar() 
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W) 
var2 = IntVar() 
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W) 
mainloop() 
