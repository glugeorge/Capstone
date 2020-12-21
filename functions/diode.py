"""Voltage varying diode measurement.

Example of modifications to live plotter for a diode measurement where voltage is
changed by the software. Run from command line.

"""

from common_functions import *
from global_variables import *
import daq, dc, multimeter

def take_measurement(t_0, device_1, device_2, channel=101):
    """Taking time, voltage, and current measurement across a diode.
    
     Args:
        t_0 (float): Anchor time for the start time of the measurement.
        device_1 (str): DAQ device ID on which to take voltage measurement.
        device_2 (str): Multimeter device ID on which to take current measurement.
        channel (str, optional): Channel on which to take a voltage measurement.
    
    Returns:
        A tuple of values of time, voltage, current.
    
    """
    t = time.time() - t_0
    volt_ascii = daq.take_measurement(device_1, channel)
    voltage = np.mean([float(s) for s in volt_ascii.split(',')])
    current = multimeter.measure_current(device_2, 0.01)
    return t, voltage, current

def initiate_measurement():
    """Function to initialize all devices for live plotting. Device IDs are specified in
    ``global_variables.py``.
    
    Args:
        None.
    
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
    
    Returns:
        Tuple of data filename and devices.
    
    """
    # Setting up chart titles
    chart_title = f"Current vs Voltage"
    data_file = initiate_file(filename, chart_title, "time", "voltage,current")
    dc_ps_dev, daq_dev, dmm_dev = initiate_measurement()

    return data_file, dc_ps_dev, daq_dev, dmm_dev

def diode_measurement(filename, refresh_rate=1000): #default is 1 sample per second
    """Function that takes live data measurements, saves to file, and plots it.
    
    Args:
        filename (str): Name of file with ``.txt`` extension.
        refresh_rate (int, optional): Delay between animation frames in milliseconds.
    
    Returns:
        None.
    
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
    f.close()
    voltage_input = 0
    dc.channel_on_off(dc_ps_dev, 1, 1)
    dc.set_voltage_level(dc_ps_dev,1,voltage_input)
    
    f = open(data_file, "a")
    def animate(i):
        """Sub-function that updates data for each new frame.
        
        """
        # Set power supply voltage level
        nonlocal voltage_input
        voltage_input += 0.1
        voltage_input = voltage_input%2
        dc.set_voltage_level(dc_ps_dev, 1, voltage_input)
        time.sleep(0.1)
        
        # Take measurements
        t, voltage, current = take_measurement(absolute_time, device_1, device_2)
        
        save_to_file(f, t, f"{voltage},{current}") # Save to file
        x.append(voltage)
        y.append(current)

        # Plot data
        x_plot, y_plot = x,y
        ax.clear()
        ax.plot(x_plot,y_plot)

        plt.title(title)
        plt.xlabel("Voltage (V)")
        plt.ylabel("Current (A)")
    
    ani = animation.FuncAnimation(fig, animate, interval=int(refresh_rate))
    plt.show()
    f.close()

if __name__ == "__main__":
    # Test code
    filename = input("Filename (include extension): ")
    diode_measurement(data_dir_name+filename)