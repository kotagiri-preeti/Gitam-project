import threading 
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
print("current thread name is :",threading.current_thread().name)
t1 = threading.Thread(target=add,args=(12,23,)) 
t2 = threading.Thread(target=sub,args=(23,34,)) 
t1.start() 
t2.start() 


