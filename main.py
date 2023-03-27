#import modules 
from time import *
from tkinter import *


# create tkinter application 
root =  Tk()
class funcs():
    #define functions 
    def timer():
        #10 second timer 
        length = 10
        while True:
            sleep(1)
            length = length -1
            print(f"Time left: {length} seconds")
            if length == 0:
                break
    def stopwatch():
        #stopwatch (runs infinitely)
        start = 0
        while True:

            sleep(1)
            start = start +1
            print(start)
#create buttons
Button(text="Timer(10 Seconds long)", command=lambda: [funcs.timer()]).pack()
Button(text="Stopwatch(No Exit or pause function)", command= lambda:[funcs.stopwatch()]).pack()
def time():
    """current time function
    Has to stay out of class or will cause errors"""
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white')

lbl.pack(anchor="center")
time()
#start the loop
root.mainloop()
