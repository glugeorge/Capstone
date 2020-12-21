"""Main GUI for software.

Inputs to the GUI are passed to other modules like the plotter where the actual
functionality is implemented.

"""

import tkinter as tk
from tkinter import ttk
from plotter import *
from high_freq_measurement import *
from import_libraries import *
from common_functions import *
from hall import *

### FUNCTIONS ###
# When adding new functionality, add the function callers here
def plot():
    """Function for real-time plotting. See ``plotter.py``.

    """
    refresh_rate = abs(1000/float(refresh_rate_raw.get()) - 95.01)
    live_plot(data_dir_name+chart_file_name.get(), chart_x_name.get(), chart_y_name.get(), scroll_on_off.get(), refresh_rate)

def high_f_measurement():
    """Function for high frequency measurement. See ``high_freq_measurement.py``.

    """
    print(f"Taking measurement at {measure_rate.get()} Hz for {measure_time.get()} seconds")
    take_high_freq(data_dir_name+measure_file_name.get(), measure_rate.get(), measure_time.get())
    print("Done taking high frequency voltage measurement")

def hall_measurement():
    """Function for implementation of the Hall experiment. See ``hall.py``.

    """
    I_p, I_n = pos_curr_position.get(), neg_curr_position.get()
    V_p, V_n = pos_v_position.get(), neg_v_position.get()
    B_field_on = mag_field_on_off.get()
    B_field_orientation = mag_field_polarity.get()
    print(f"Taking Hall measurement at positions:\nI_p={I_p}\nI_n={I_n}\nV_p={V_p}\nV_n={V_n}")
    take_hall_measurement(I_p, I_n, V_p, V_n, B_field_on, B_field_orientation, data_dir_name+hall_file_name.get())
    print("Done taking Hall measurement")
######

r = tk.Tk()
r.title('Chart Recorder GUI')

### TABS ###
tab_parent = ttk.Notebook(r)
tab_chart_recorder = ttk.Frame(tab_parent)
tab_high_freq_measure = ttk.Frame(tab_parent)
tab_hall = ttk.Frame(tab_parent)

tab_parent.add(tab_chart_recorder, text="Chart recorder")
tab_parent.add(tab_high_freq_measure, text="High frequency voltage measurement")
tab_parent.add(tab_hall, text="Hall effect")
# Add new tabs here

tab_parent.pack(expand=1, fill="both")


# Chart recorder tab
chart_file_label = tk.Label(tab_chart_recorder,text="Filename (include extension)")
chart_file_label.grid(column=1, columnspan=3, sticky='S')
chart_file_name = tk.Entry(tab_chart_recorder)
chart_file_name.grid(column=1, columnspan=3, row = 1)

chart_x_label = tk.Label(tab_chart_recorder, text="X axis", width=10)
chart_x_label.grid(column=1, row=2)
chart_x_name = tk.StringVar(tab_chart_recorder)
chart_x_name.set("random") # default value
chart_x_entry = tk.OptionMenu(tab_chart_recorder, chart_x_name, "random", "time", "voltage", "current")
chart_x_entry.grid(column=1, row=3)

chart_y_label = tk.Label(tab_chart_recorder, text="Y axis", width=10)
chart_y_label.grid(column=3, row=2)
chart_y_name = tk.StringVar(tab_chart_recorder)
chart_y_name.set("random") # default value
chart_y_entry = tk.OptionMenu(tab_chart_recorder, chart_y_name, "random", "time", "voltage", "current", "two voltages")
chart_y_entry.grid(column=3, row=3)

plot_options = tk.Label(tab_chart_recorder, text="Plot options")
plot_options.grid(column=1, columnspan=3, row=4)
scroll_on_off = tk.IntVar()
scroll_on_off_entry = tk.Checkbutton(tab_chart_recorder, text="Scroll", variable=scroll_on_off)
scroll_on_off_entry.grid(column=1, row=5)
refresh_rate_label = tk.Label(tab_chart_recorder, text="(Hz) Refresh rate")
refresh_rate_label.grid(column=3, row=5)
refresh_rate_raw = tk.StringVar(tab_chart_recorder, value='1') # default value
refresh_rate_entry = tk.Entry(tab_chart_recorder, textvariable=refresh_rate_raw, width=5)
refresh_rate_entry.grid(column=2, row=5)

live_plot_submit = tk.Button(tab_chart_recorder, text='Live Plot', height = 2, width = 20, command=plot)
live_plot_submit.grid(column=1, columnspan=3, rowspan=2, sticky='N')
tab_chart_recorder.grid_columnconfigure(1, weight=1)
tab_chart_recorder.grid_columnconfigure(2, weight=1)
tab_chart_recorder.grid_columnconfigure(3, weight=1)


# High frequency measurement tab
measure_file_label = tk.Label(tab_high_freq_measure, text="Filename (include extension)")
measure_file_label.grid(column=1, columnspan=3)
measure_file_name = tk.Entry(tab_high_freq_measure)
measure_file_name.grid(column=1, columnspan=3, row = 1)

measure_rate_label = tk.Label(tab_high_freq_measure, text="Rate (Hz, max = 1000)", width=20)
measure_rate_label.grid(column=1, row=2)
measure_rate = tk.StringVar(tab_high_freq_measure)
measure_rate.set(1) # default value
measure_rate_entry = tk.Entry(tab_high_freq_measure, textvariable=measure_rate, width=15)
measure_rate_entry.grid(column=1, row=3)

measure_time_label = tk.Label(tab_high_freq_measure,text="Sample Time (s)", width=20)
measure_time_label.grid(column=2, row=2)
measure_time = tk.StringVar(tab_high_freq_measure)
measure_time.set(1) # default value
measure_time_entry = tk.Entry(tab_high_freq_measure, textvariable=measure_time, width=15)
measure_time_entry.grid(column=2, row=3)

measure_submit = tk.Button(tab_high_freq_measure, text='Take Measurement', height = 2, width = 20, command=high_f_measurement)
measure_submit.grid(column=1, columnspan=3, rowspan=2)
tab_high_freq_measure.grid_columnconfigure(1, weight=1)
tab_high_freq_measure.grid_columnconfigure(2, weight=1)


# Hall measurement tab
hall_file_label = tk.Label(tab_hall, text="Filename (include extension)")
hall_file_label.grid(column=1, columnspan=4, sticky='S')
hall_file_name = tk.Entry(tab_hall)
hall_file_name.grid(column=1, columnspan=4, row = 1)

pos_curr_label = tk.Label(tab_hall, text="I_p", width=5)
pos_curr_label.grid(column=1, row=2)
pos_curr_position = tk.StringVar(tab_hall)
pos_curr_position.set("1") # default value
pos_curr_entry = tk.OptionMenu(tab_hall, pos_curr_position, "1", "2", "3", "4")
pos_curr_entry.grid(column=1, row=3)

neg_curr_label = tk.Label(tab_hall, text="I_n", width=5)
neg_curr_label.grid(column=2, row=2)
neg_curr_position = tk.StringVar(tab_hall)
neg_curr_position.set("2") # default value
neg_curr_entry = tk.OptionMenu(tab_hall, neg_curr_position, "1", "2", "3", "4")
neg_curr_entry.grid(column=2, row=3)

pos_v_label = tk.Label(tab_hall, text="V_p", width=5)
pos_v_label.grid(column=3, row=2)
pos_v_position = tk.StringVar(tab_hall)
pos_v_position.set("4") # default value
pos_v_entry = tk.OptionMenu(tab_hall, pos_v_position, "1", "2", "3", "4")
pos_v_entry.grid(column=3, row=3)

neg_v_label = tk.Label(tab_hall, text="V_n", width=5)
neg_v_label.grid(column=4, row=2)
neg_v_position = tk.StringVar(tab_hall)
neg_v_position.set("3") # default value
neg_v_entry = tk.OptionMenu(tab_hall, neg_v_position, "1", "2", "3", "4")
neg_v_entry.grid(column=4, row=3)

hall_options = tk.Label(tab_hall, text="Hall measurement options")
hall_options.grid(column=1, columnspan=4, row=4)
mag_field_on_off = tk.IntVar()
mag_field_entry = tk.Checkbutton(tab_hall, text="Magnetic field", variable=mag_field_on_off)
mag_field_entry.grid(column=1, columnspan=2,row=5)
mag_field_polarity = tk.StringVar(tab_hall)
mag_field_polarity.set("+") # default value
mag_field_polarity_entry = tk.OptionMenu(tab_hall, mag_field_polarity, "+", "-")
mag_field_polarity_entry.grid(column=3, columnspan=2, row=5)

hall_submit = tk.Button(tab_hall, text='Take Measurement', height = 2, width = 15, command=hall_measurement)
hall_submit.grid(column=1, columnspan=4, rowspan=2, sticky='N')
tab_hall.grid_columnconfigure(1, weight=1)
tab_hall.grid_columnconfigure(2, weight=1)
tab_hall.grid_columnconfigure(3, weight=1)
tab_hall.grid_columnconfigure(4, weight=1)

### ADD NEW TABS BELOW ###

r.mainloop()
