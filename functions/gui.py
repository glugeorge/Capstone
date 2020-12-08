import tkinter as tk
from tkinter import ttk
from plotter_syncronous import *
from import_libraries import *
from common_functions import *

def plot():
    refresh_rate = 1000/variable5.get()
    live_plot(entry1.get(),variable2.get(),variable3.get(),check1.get(),refresh_rate)

def high_f_measurement():
    print("Take measurement at high speed with:")
    print(entry6.get(),variable7.get(),variable8.get())


r = tk.Tk()
r.title('Chart Recorder GUI')
r.geometry("300x240")

tab_parent = ttk.Notebook(r)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Chart recorder")
tab_parent.add(tab2, text="High frequency measurement")
tab_parent.add(tab3, text="Hall effect")

tab_parent.pack(expand=1, fill="both")


# Chart recorder tab


label1 = tk.Label(tab1,text="Filename")
label1.grid(column=1, columnspan=3, sticky='S')
entry1 = tk.Entry(tab1)
entry1.grid(column=1, columnspan=3, row = 1)

label2 = tk.Label(tab1,text="X axis", width=10)
label2.grid(column=1, row=2)
variable2 = tk.StringVar(tab1)
variable2.set("random") # default value
entry2 = tk.OptionMenu(tab1, variable2, "random", "time", "voltage", "current")
entry2.grid(column=1, row=3)

label3 = tk.Label(tab1,text="Y axis", width=10)
label3.grid(column=3, row=2)
variable3 = tk.StringVar(tab1)
variable3.set("random") # default value
entry3 = tk.OptionMenu(tab1, variable3, "random", "time", "voltage", "current", "two voltages")
entry3.grid(column=3, row=3)

label4 = tk.Label(tab1,text="Plot options")
label4.grid(column=1, columnspan=3, row=4)
check1 = tk.IntVar()
entry4 = tk.Checkbutton(tab1, text="Scroll", variable=check1)
entry4.grid(column=1, row=5)
label5 = tk.Label(tab1,text="(Hz) Refresh rate")
label5.grid(column=3, row=5)
variable5 = tk.StringVar(tab1, value='1') # default value
entry5 = tk.Entry(tab1, textvariable=variable5, width=5)
entry5.grid(column=2, row=5)

button2 = tk.Button(tab1, text='Live Plot', height = 2, width = 20, command=plot)
button2.grid(column=1, columnspan=3, rowspan=2, sticky='N')


# High frequency measurement tab


label6 = tk.Label(tab2,text="Filename")
label6.grid(column=1, columnspan=3, sticky='S')
entry6 = tk.Entry(tab2)
entry6.grid(column=1, columnspan=3, row = 1)

label7 = tk.Label(tab2,text="X axis", width=10)
label7.grid(column=1, row=2)
variable7 = tk.StringVar(tab2)
variable7.set("random") # default value
entry7 = tk.OptionMenu(tab2, variable7, "random", "time", "voltage", "current")
entry7.grid(column=1, row=3)

label8 = tk.Label(tab2,text="Y axis", width=10)
label8.grid(column=3, row=2)
variable8 = tk.StringVar(tab2)
variable8.set("random") # default value
entry8 = tk.OptionMenu(tab2, variable8, "random", "time", "voltage", "current", "two voltages")
entry8.grid(column=3, row=3)

button2 = tk.Button(tab2, text='Take Measurement', height = 2, width = 20, command=high_f_measurement)
button2.grid(column=1, columnspan=3, rowspan=2, sticky='N')

# Hall measurement tab



r.mainloop()
