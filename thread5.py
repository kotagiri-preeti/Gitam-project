from threading import *
def display():
    print("hello")
t1=Thread(target=display,name="child-1") 
t2=Thread(target=display,name="child-2")
t1.start()
t2.start()
l=enumerate()
for i in l:
    print("thread name=",i.name)
    print("thread identification number:",i.ident)
    print()

