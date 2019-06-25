from threading import *
import time 
def display():
    print(current_thread().name,"...started")
    time.sleep(3)
    print(current_thread().name,"...ended")
print("the no.of active threads:",active_count())
t1=Thread(target=display,name="child-1") 
t2=Thread(target=display,name="child-2")
t1.start()
t2.start()
print("the no.of active threads:",active_count())
time.sleep(10)
print("the no.of active threads:",active_count())

