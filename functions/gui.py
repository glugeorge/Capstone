import tkinter as tk
from tkinter import ttk
from plotter_syncronous import *
from high_freq_measurement import *
from import_libraries import *
from common_functions import *
from hall import *

def plot():
    refresh_rate = abs(1000/float(variable5.get()) - 95.01)
    live_plot(entry1.get(),variable2.get(),variable3.get(),check1.get(),refresh_rate)

def high_f_measurement():
    print("Take measurement at high speed with:")
    print(entry6.get(),variable7.get(),variable8.get())
    take_high_freq(entry6.get(),variable7.get(),variable8.get())

def hall_measurement():
    I_p, I_n = variable10.get(), variable11.get()
    V_p, V_n = variable12.get(), variable13.get()
    B_field_on = check2.get()
    B_field_orientation = variable16.get()
    take_hall_measurement(I_p, I_n, V_p, V_n, B_field_on, B_field_orientation, entry9.get())


r = tk.Tk()
r.title('Chart Recorder GUI')

tab_parent = ttk.Notebook(r)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Chart recorder")
tab_parent.add(tab2, text="High frequency voltage measurement")
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

label7 = tk.Label(tab2,text="Rate (Hz, max = 1000)", width=20)
label7.grid(column=1, row=2)
variable7 = tk.StringVar(tab2)
variable7.set(1) # default value
entry7 = tk.Entry(tab2, textvariable=variable7, width=15)
entry7.grid(column=1, row=3)

label8 = tk.Label(tab2,text="Sample Time (s)", width=20)
label8.grid(column=3, row=2)
variable8 = tk.StringVar(tab2)
variable8.set(1) # default value
entry8 = tk.Entry(tab2, textvariable=variable8, width=15)
entry8.grid(column=3, row=3)

button2 = tk.Button(tab2, text='Take Measurement', height = 2, width = 20, command=high_f_measurement)
button2.grid(column=1, columnspan=3, rowspan=2, sticky='N')


# Hall measurement tab


label9 = tk.Label(tab3,text="Filename")
label9.grid(column=1, columnspan=4, sticky='S')
entry9 = tk.Entry(tab3)
entry9.grid(column=1, columnspan=4, row = 1)

label10 = tk.Label(tab3,text="I_p", width=5)
label10.grid(column=1, row=2)
variable10 = tk.StringVar(tab3)
variable10.set("1") # default value
entry10 = tk.OptionMenu(tab3, variable10, "1", "2", "3", "4")
entry10.grid(column=1, row=3)

label11 = tk.Label(tab3,text="I_n", width=5)
label11.grid(column=2, row=2)
variable11 = tk.StringVar(tab3)
variable11.set("2") # default value
entry11 = tk.OptionMenu(tab3, variable11, "1", "2", "3", "4")
entry11.grid(column=2, row=3)

label12 = tk.Label(tab3,text="V_p", width=5)
label12.grid(column=3, row=2)
variable12 = tk.StringVar(tab3)
variable12.set("4") # default value
entry12 = tk.OptionMenu(tab3, variable12, "1", "2", "3", "4")
entry12.grid(column=3, row=3)

label13 = tk.Label(tab3,text="V_n", width=5)
label13.grid(column=4, row=2)
variable13 = tk.StringVar(tab3)
variable13.set("3") # default value
entry13 = tk.OptionMenu(tab3, variable13, "1", "2", "3", "4")
entry13.grid(column=4, row=3)

label15 = tk.Label(tab3,text="Hall measurement options")
label15.grid(column=1, columnspan=4, row=4)
check2 = tk.IntVar()
entry15 = tk.Checkbutton(tab3, text="Magnetic field", variable=check2)
entry15.grid(column=1, columnspan=2,row=5)
variable16 = tk.StringVar(tab3)
variable16.set("+") # default value
entry16 = tk.OptionMenu(tab3, variable16, "+", "-")
entry16.grid(column=3, columnspan=2, row=5)

button14 = tk.Button(tab3, text='Take Measurement', height = 2, width = 15, command=hall_measurement)
button14.grid(column=1, columnspan=4, rowspan=2, sticky='N')

r.mainloop()
