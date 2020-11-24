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
entry2 = tk.OptionMenu(r, variable2, "random", "random_vs_time", "breaks")
entry2.pack()

button2 = tk.Button(r, text='Live Plot', width=25, command=plot)
button2.pack()

button3 = tk.Button(r, text='Stop', width=25, command=r.destroy)
button3.pack()

r.mainloop()
