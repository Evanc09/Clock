import time
from tkinter import *



root =  Tk()
class funcs():
        def current_time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)
        lbl = Label(root, font=('calibri', 40, 'bold'),
                    background='black',
                    foreground='white')

        # of the tkinter window
    lbl.pack(anchor='center')
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
current_time()
root.mainloop()
