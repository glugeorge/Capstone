"""Common functions that are used by other modules.

Add other general (i.e. not device specific) functions here as needed.
"""

from import_libraries import *

def init_devices(device_names): # Takes in array of devices
    """Function to initialize a list of device IDs through PyVISA. Device IDs should be
    specified in ``global_variables.py``.
    
    Args:
        device_names (list): List of device IDs to initialize.
    
    Returns:
        List of initialized devices.
    
    """
    rm = pyvisa.ResourceManager()
    devices = []
    for device_name in device_names:
        device = rm.open_resource(device_name)
        device.read_termination = '\n'
        devices.append(device)
    return devices

def initiate_file(filename, title="y(x)", x_axis="x", y_axis="y"):
    """Function to create the text file where data will be saved, and initialize it with
    the appropriate title and data labels at the top of the file.
    
    Args:
        filename (str): Name of file with ``.txt`` extension.
        title (str, optional): Title of data plot.
        x_axis (str, optional): Label for x-axis.
        y_axis (str, optional): Label for y-axis.
    
    Returns:
        Filename.
    
    """
    f = open(filename, "w")
    text = title + "\n" + x_axis + "," + y_axis + "\n"
    f.write(text)
    f.close()
    return filename

def save_to_file(f, x, y):
    """Function to save a line of data to ``filename``. This is formatted as the x-value
    followed by any y-values, separated by a comma.
    
    Args:
        f (file object): File object of data file.
        x (float or str): x data value to be saved.
        y (float or str): y data value(s) to be saved.
    
    Returns:
        None.
    
    """
    #f = open(filename, "a")
    text = str(x) + "," + str(y) + "\n"
    f.write(text)
    # No need to close until possibly the end, slows down code
    #f.close()
    #return filename
