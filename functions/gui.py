import tkinter as tk
from plotter_syncronous import *
from import_libraries import *
from common_functions import *

def plot():
    live_plot(entry1.get(),variable2.get(),variable3.get(),check1.get(),)

r = tk.Tk()
r.title('Chart Recorder GUI')

label1 = tk.Label(r,text="Filename")
label1.pack()
entry1 = tk.Entry(r)
entry1.pack()

label2 = tk.Label(r,text="X Axis")
label2.pack()
variable2 = tk.StringVar(r)
variable2.set("random") # default value
entry2 = tk.OptionMenu(r, variable2, "random", "time", "voltage", "current")
entry2.pack()

label3 = tk.Label(r,text="Y_axis")
label3.pack()
variable3 = tk.StringVar(r)
variable3.set("random") # default value
entry3 = tk.OptionMenu(r, variable3, "random", "time", "voltage", "current", "two voltages")
entry3.pack()

label4 = tk.Label(r,text="Plot options")
label4.pack()
check1 = tk.IntVar()
entry4 = tk.Checkbutton(r, text="Scroll", variable=check1)
entry4.pack()
label5 = tk.Label(r,text="Refresh rate")
label5.pack()
variable5 = tk.StringVar(r, value='1000')
entry5 = tk.Entry(r, textvariable=variable5)
entry5.pack()

button2 = tk.Button(r, text='Live Plot', width=25, command=plot)
button2.pack()

button3 = tk.Button(r, text='Stop', width=25, command=r.destroy)
button3.pack()

r.mainloop()
