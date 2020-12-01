import tkinter as tk
from plotter_syncronous import *
from import_libraries import *
from common_functions import *

def plot():
    live_plot(entry1.get(),variable2.get())

r = tk.Tk()
r.title('Chart Recorder GUI')

label1 = tk.Label(r,text="Filename")
label1.pack()
entry1 = tk.Entry(r)
entry1.pack()

label2 = tk.Label(r,text="Type of plot")
label2.pack()
variable2 = tk.StringVar(r)
variable2.set("random") # default value
entry2 = tk.OptionMenu(r, variable2, "random", "random_vs_time", "voltage_vs_time")
entry2.pack()

label3 = tk.Label(r,text="Plot options")
label3.pack()
check1 = tk.IntVar()
entry3 = tk.Checkbutton(r, text="Scroll", variable=check1)
entry3.pack()
label4 = tk.Label(r,text="Refresh rate")
label4.pack()
entry4 = tk.Entry(r)
entry4.pack()

button2 = tk.Button(r, text='Live Plot', width=25, command=plot)
button2.pack()

button3 = tk.Button(r, text='Stop', width=25, command=r.destroy)
button3.pack()

r.mainloop()
