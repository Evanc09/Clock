import time
from tkinter import *



root =  Tk()
class funcs():
    def timer():
        length = 10
        while True:
            time.sleep(1)
            length = length -1
            print(f"Time left: {length} seconds")
            if length == 0:
                break
    def stopwatch():
        
        start = 0
        while True:

            time.sleep(1)
            start = start +1
            print(start)
        
Button(text="Timer(10 Seconds long)", command=lambda: [funcs.timer()]).pack()
Button(text="Stopwatch(No Exit or pause function)", command= lambda:[funcs.stopwatch()]).pack()

root.mainloop()
