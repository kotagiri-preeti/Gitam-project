import tkinter as tk
def add(a,b):
    print(a+b)
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, image="C:\Users\vishwathsena\Pictures\Dinamic Wallpaper\ab.jpg", width=25, command=add(12,23)) 
button.pack() 
r.mainloop() 
