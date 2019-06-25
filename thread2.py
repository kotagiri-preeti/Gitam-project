from threading import *
def display():
    print("child thread is:",current_thread().getName(),end="")
t=Thread(target=display)
t.start()
print("main thread is:",current_thread().getName())

