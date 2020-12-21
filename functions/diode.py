"""Real-time plotter module.

"""

from common_functions import *
from global_variables import *
import daq, dc, multimeter

def take_measurement(t_0, device_1, device_2, channel=101):
    """
        Taking time, voltage, and current measurement across a diode
    """
    t = time.time() - t_0
    volt_ascii = daq.take_measurement(device_1, channel)
    voltage = np.mean([float(s) for s in volt_ascii.split(',')])
    current = multimeter.measure_current(device_2, 0.01)
    return t,voltage,current

def initiate_measurement():
    """Function to initialize all devices for live plotting. Device IDs are specified in
    ``global_variables.py``.
    
    Args:
        None
    
    Returns:
        List of initialized devices.
    
    """
    dc_ps_dev, daq_dev, dmm_dev = init_devices([dc_ps_name, daq_name, dmm_name])
    dc.set_voltage_level(dc_ps_dev, 1, 1)
    dc.set_current_level(dc_ps_dev, 1, 0.2)
    daq.initialize_device(daq_dev, 102, rate=800E3, voltage=18)
    multimeter.initialize_device(dmm_dev, 0.01)
    return dc_ps_dev, daq_dev, dmm_dev

def setup(filename):
    """Function to set up data file and axes for live plotting.
    
    Args:
        filename (str): Name of file with ``.txt`` extension.
        x_value (str): Measurement type for x-axis.
        y_value (str): Measurement type for y-axis.
    
    Returns:
        Tuple of data filename and devices.
    
    """
    # Setting up chart titles
    chart_title = f"Current vs Voltage"
    data_file = initiate_file(filename, chart_title, "current", "voltage")
    dc_ps_dev, daq_dev, dmm_dev = initiate_measurement()

    return data_file, dc_ps_dev, daq_dev, dmm_dev

def diode_measurement(filename, refresh_rate=1000): #default is 1 sample per second
    """Function that takes live data measurements, saves to file, and plots it.
    
    Args:
        filename (str): Name of file with ``.txt`` extension.
        x_value (str): Measurement type for x-axis.
        y_value (str): Measurement type for y-axis.
        scroll (Boolean, optional): Enable scrolling window for live plot.
        refresh_rate (int, optional): Delay between animation frames in milliseconds.
    
    Returns:
        List of initialized devices.
    
    """
    data_file, dc_ps_dev, device_1, device_2 = setup(filename)
    absolute_time = time.time()
    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = []
    y = []
    f = open(data_file, "r")
    lines = f.readlines()
    title = lines[0]
    x_axis, y_axis = lines[1].split(",")[0], lines[1].split(",")[1]
    f.close()
    voltage_input = 0
    dc.channel_on_off(dc_ps_dev, 1, 1)
    dc.set_voltage_level(dc_ps_dev,1,voltage_input)
    def animate(i):
        """Sub-function that updates data for each new frame.
        
        """
        # Take measurements
        voltage_input +=0.1
        voltage_input = voltage_input%2
        dc.set_voltage_level(dc_ps_dev,1,voltage_input)
        t, voltage, current = take_measurement(t_0, device_1, device_2)
        
        save_to_file(data_file, time, f"{voltage},{current}") # Save to file
        y_vals = str(item2).split(",") 
        x.append(voltage)
        y.append(current)

        # Plot data
        x_plot, y_plot, y1_plot = x,y
        ax.clear()
        ax.plot(x_plot,y_plot)

        plt.title(title)
        plt.xlabel("Voltage (V)")
        plt.ylabel("Current (A)")
    
    ani = animation.FuncAnimation(fig, animate, interval=int(refresh_rate))
    plt.show()

if __name__ == "__main__":
    # Test code
    live_plot("test.txt", "random_vs_time", scroll=False, refresh_rate=100)
