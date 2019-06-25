from threading import *
import time
def display():
    for i in range(5):
        print("thread-1")
        time.sleep(1)
t=Thread(target=display)
t.start()
t.join(3)
for i in range(5):
    print("thread-2")


