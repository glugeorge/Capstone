"""High frequency measurement module.

Intended for longer continuous measurements on the DAQ system.
"""

from common_functions import *
from global_variables import *
import daq

def take_high_freq(filename, user_rate, user_time, channel=101):
    """Function to take higher frequency voltage measurement on the DAQ than is possible
    with the live plotter.
    
    Args:
        filename (str): Name of file with ``.txt`` extension.
        user_rate (float): Frequency in Hz at which to take the measurement.
        user_time (str): Time in seconds for which to take the measurement.
        channel (str, optional): Channel on which to take the measurement.
    
    Returns:
        None.
    
    """
    initiate_file(filename, 'voltage v time', 'time', 'voltage')
    daq_dev = init_devices([daq_name])[0]
    daq.initialize_device(daq_dev, channel, count=float(user_time)*1.5625E3)
    data_ascii= daq.take_measurement(daq_dev,channel)
    data_list = [float(s) for s in data_ascii.split(',')]
    rate_ratio = int(1.5625E3 / float(user_rate))
    to_save = 0
    time = 0
    item_count = 0
    
    f = open(filename, "a")
    for item in data_list:
        item_count += 1
        to_save += float(item)
        if item_count == rate_ratio:
            to_save = to_save/item_count
            save_to_file(f, time, to_save)
            time += 1/float(user_rate)
            item_count = 0
            to_save = 0
    
    f.close()

if __name__ == "__main__":
    # Test code
    data_list = take_high_freq('test.txt', 100, 5)