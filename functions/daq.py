"""Functions to interface with the Keysight DAQ system.

"""

from common_functions import * # don't need this if init in main/experiments
from global_variables import *

def initialize_device(device, channel, rate=1.5625E3, count=512, voltage=3):
    """Function to set voltage measurement parameters on the DAQ.
    
    Args:
        device (str): Device ID of the DAQ system.
        channel (str): Channel(s) on the DAQ on which to take the measurement.
        rate (int, optional): Sample rate in Hz (1.5625E3 to 800E3)
        count (int, optional): Number of samples to take (min. 512).
        voltage (int, optional): Maximum voltage range in volts on the DAQ (Can be 1, 3, or 18).
    
    Returns:
        None.
    
    """
    device.write(f"ACQ3:VOLT {voltage},DEF,DEF,DEF,{count},{rate},(@{channel})")
    device.timeout = 20000

def take_measurement(device, channel):
    """Function to take a voltage measurement on the DAQ.
    
    Args:
        device (str): Device ID of the DAQ system.
        channel (str): Channel(s) on the DAQ on which to take the measurement.
    
    Returns:
        Single ASCII string of all the data points separated by commas, or a list of such
        ASCII strings.
    
    """
    device.write(f"INITiate3 (@{channel})")
    channels = str(channel).split(',')
    datalist = []
    for c in channels:
        datalist.append(device.query(f"FETCh3? (@{c})"))
    
    return datalist[0] if len(datalist) == 1 else datalist

def live_acquisition(device, channel, rate=1.5625E3, count=512, voltage=3):
    """Function for live voltage acquisition on the DAQ. Saves to file.
    
    Args:
        device (str): Device ID of the DAQ system.
        channel (str): Channel(s) on the DAQ on which to take the measurement.
        rate (int, optional): Sample rate in Hz (1.5625E3 to 800E3)
        count (int, optional): Number of samples to take (min. 512).
        voltage (int, optional): Maximum voltage range in volts on the DAQ (Can be 1, 3, or 18).
    
    Returns:
        None.
    
    """
    filename = initiate_file('test.txt')
    initialize_device(device, channel, rate, count, voltage)
    start = time.time()
    while True:
        volt_ascii = take_measurement(device,channel)
        t = time.time() - start
        voltage = np.mean([float(s) for s in volt_ascii.split(',')])
        save_to_file(filename, t, voltage)
        time.sleep(0.05)