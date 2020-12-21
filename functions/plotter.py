"""Real-time plotter module.

"""

from common_functions import *
from global_variables import *
import daq, dc, multimeter

def take_measurement(measurement, t_0, device=None, channel=101):
    """Function to take some sort of measurement, with the details determined by the
    specific parameters passed.
    
    Args:
        measurement (str): Type of measurement to obtain.
        t_0 (float): Anchor time for the start time of the measurement.
        device (str): Device ID on which to take measurement (required unless
         ``measurement`` is 'time').
        channel (str, optional): Channel on which to take a voltage measurement (for
         DAQ system only).
    
    Returns:
        A float measurement value, or a string containing two float measurement values.
    
    """
    if measurement == "random":
        return random.random()
    if measurement == "time":
        t = time.time() - t_0
        return t
    if measurement == "voltage":
        volt_ascii = daq.take_measurement(device, channel)
        voltage = np.mean([float(s) for s in volt_ascii.split(',')])
        return voltage
    if measurement == "current":
        current = multimeter.measure_current(device, 0.01)
        return current
    if measurement == "two voltages":
        volt_ascii1, volt_ascii2 = daq.take_measurement(device, "101,102")
        voltage1 = np.mean([float(s) for s in volt_ascii1.split(',')])
        voltage2 = np.mean([float(s) for s in volt_ascii2.split(',')])
        return f"{voltage1},{voltage2}"

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

def setup(filename, x_value, y_value):
    """Function to set up data file and axes for live plotting.
    
    Args:
        filename (str): Name of file with ``.txt`` extension.
        x_value (str): Measurement type for x-axis.
        y_value (str): Measurement type for y-axis.
    
    Returns:
        Tuple of data filename and devices.
    
    """
    # Setting up chart titles
    chart_title = f"{y_value} vs {x_value}"
    data_file = initiate_file(filename, chart_title, x_value, y_value)
    dc_ps_dev, daq_dev, dmm_dev = initiate_measurement()
    device_dict = {
        "random": None,
        "time": None,
        "voltage": daq_dev,
        "current": dmm_dev,
        "two voltages": daq_dev
        }
    return data_file, dc_ps_dev, device_dict[x_value], device_dict[y_value]

def live_plot(filename, x_value, y_value, scroll=True, refresh_rate=1000): #default is 1 sample per second
    """Function that takes live data measurements, saves to file, and plots it.
    
    Args:
        filename (str): Name of file with ``.txt`` extension.
        x_value (str): Measurement type for x-axis.
        y_value (str): Measurement type for y-axis.
        scroll (Boolean, optional): Enable scrolling window for live plot.
        refresh_rate (int, optional): Delay between animation frames in milliseconds.
    
    Returns:
        None.
    
    """
    data_file, dc_ps_dev, device_1, device_2 = setup(filename, x_value, y_value)
    absolute_time = time.time()
    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = []
    y = []
    y1 = []
    f = open(data_file, "r")
    lines = f.readlines()
    title = lines[0]
    x_axis, y_axis = lines[1].split(",")[0], lines[1].split(",")[1]
    f.close()
    
    f = open(data_file, "a")
    def animate(i):
        """Sub-function that updates data for each new frame.
        
        """
        # Take measurements
        item1, item2 = take_measurement(x_value, absolute_time, device_1, 102), take_measurement(y_value, absolute_time, device_2)
        save_to_file(f, item1, item2) # Save to file
        y_vals = str(item2).split(",") 
        x.append(item1)
        y.append(float(y_vals[0]))
        if len(y_vals)>1: # Handles case with two voltages vs. time
            y1.append(float(y_vals[1]))

        ## DEPRECATED: Slows down code
        # Parse data file for x and y
        #f = open(data_file, "r")
        #lines = f.readlines()
        #f.close()
        #if len(lines) > len(x)+2:
        #    for line in lines[len(x)+2:]:
        #        x.append(float(line.split(",")[0]))
        #        y.append(float(line.split(",")[1]))
        
        # Plot data
        if scroll and len(x)> 20: # Window length for scroll mode
            x_plot, y_plot = x[-20:], y[-20:]
            if len(y_vals)>1:
                y1_plot = y1[-20:]
        else:
            x_plot, y_plot, y1_plot = x,y,y1
        ax.clear()
        ax.plot(x_plot,y_plot)
        if len(y_vals)>1: # Handles case with two voltages vs. time
            ax.plot(x_plot,y1_plot)
        plt.title(title)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)

    ani = animation.FuncAnimation(fig, animate, interval=int(refresh_rate))
    plt.show()
    f.close()

if __name__ == "__main__":
    # Test code
    live_plot("test.txt", "random_vs_time", scroll=False, refresh_rate=100)
