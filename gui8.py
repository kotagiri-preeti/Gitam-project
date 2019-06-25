from tkinter import *
root=Tk()
root.geometry("300x300")
def name():
    name1=input("enter name")
    print(name1)
def pwd():
    name1=input("enter password")
    print(name1)

b1=Button(root,text="button1",command=name)
l1=Label(root,text="name")
b2=Button(root,text="button2",command=pwd)
l2=Label(root,text="pwd")
l1.grid(row=0)
b1.grid(row=0,column=1)
l2.grid(row=1)
b2.grid(row=1,column=1)
b=Button(root,text="submit")
b.grid(row=150,column=150)

root.mainloop()