from  tkinter import *
root =Tk( className="hello" )
root.geometry("400x400")
for r in range(3):
    for c in range(4):
        Label(root, text='R%s/C%s'%(r,c),borderwidth=5 ).grid(row=r,column=c)
root.mainloop(  )
