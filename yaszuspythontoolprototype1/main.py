import tkinter as tk
import time
from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep
from time import localtime, strftime, struct_time
from datetime import datetime as dt
from tkinter import messagebox
import socket
def callback():
    print("bomb has been planted")
userbase = {"Yaszu":1,}
### Make Gui ###
root = Tk()
root.title("Yaszu's Python Tool")
### Specify Window Size Ang Make List Options
root.geometry("1080x520")
difference = 0
welframe= ttk.LabelFrame(root)
welframe.grid(column=2,row=1,sticky=(W, E),padx=10,pady=10)
welcomelabel = ttk.Label(welframe,text="Welcome to Yaszu's Python Tool!!")
welcomelabel.grid(column=1,row=1,sticky=(W, E),padx=10,pady=10)
listboxes = LabelFrame(root)
listboxes.grid(column=2,row=2,sticky=(W, E),padx=10,pady=10)
Listoptions = Listbox(listboxes)
### Create Items WITHIN List Options


Listoptions.grid(column=1,row=0,sticky=(W, E))
Listoptions.insert(1,"Start Server")
Listoptions.insert(2,"Start Client")

timeframe = ttk.LabelFrame(root)
timeframe.grid(column=1,row=2,sticky=(W, E),padx=10,pady=10)
timelbl = ttk.Label(timeframe)
timelbl.grid(column=3,row=1,sticky=(W, E),padx=10,pady=10)
label1 = ttk.Label(timeframe,text="Time until School Ends:")
label1.grid(column=1,row=1,sticky=(W, E),padx=10,pady=10)

#Calculate time until school ends
def calculateout():
    start = strftime("%H:%M:%S",localtime())
    t1 = dt.strptime(start,"%H:%M:%S")
    day = strftime("%A",localtime())
    if day == "Tuesday":
        target = "14:25:00"
    else:
        target = "15:25:00"
    targettime = dt.strptime(target, "%H:%M:%S")
    delta = targettime - t1
    print(delta)
    difference = delta
    return delta
    timelbl.update()




def update():
   timelbl['text'] = calculateout()
   root.after(1000, update) # run itself again after 1000 ms

update()

root.mainloop()