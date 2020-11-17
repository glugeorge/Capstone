import tkinter as tk
from plotter import *
from import_libraries import *
from common_functions import *
import random

def plot():
    live_plot(entry1.get())

r = tk.Tk()
r.title('Chart Recorder GUI')
label1 = tk.Label(r,text="Filename")
label1.pack()
entry1 = tk.Entry(r)
entry1.pack()
button2 = tk.Button(r, text='Live Plot', width=25, command=plot)
button2.pack()
button3 = tk.Button(r, text='Stop', width=25, command=r.destroy)
button3.pack()
r.mainloop()
