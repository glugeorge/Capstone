"""Functions to interface with the Keysight digital multimeter.

"""

from common_functions import *
from global_variables import *

def initialize_device(device, range, ac_dc='DC', sample_count=1):
    """Function to set current measurement parameters on the multimeter.
    
    Args:
        device (str): Device ID of the multimeter.
        range (str): Range in Amperes to use on the multimeter.
        ac_dc (str, optional): AC or DC current measurement.
        sample_count (int, optional): Number of samples to take.
    
    Returns:
        None.
    
    """
    device.write(f"CONF:CURR:{ac_dc} {range}")
    device.write(f"SAMPle:COUNt {sample_count}")
    device.timeout = 20000

def measure_current(device, range):
    """Function to take a current measurement on the multimeter.
    
    Args:
        device (str): Device ID of the multimeter.
        range (str): Range in Amperes to use on the multimeter.
    
    Returns:
        Float value of the current measurement.
    
    """
    curr_ascii = device.query("READ?")
    return float(curr_ascii)


def measure_voltage(device, range, ac_dc='DC', sample_count=1):
    """Function to initialize and take a voltage measurement on the multimeter.
    
    Args:
        device (str): Device ID of the multimeter.
        range (str): Range in volts to use on the multimeter.
        ac_dc (str, optional): AC or DC voltage measurement.
        sample_count (int, optional): Number of samples to take.
    
    Returns:
        Float value of the voltage measurement.
    
    """
    device.write("CONF:VOLT:{} {}".format(ac_dc, range))
    device.write("SAMPle:COUNt {}".format(sample_count))
    device.timeout = 20000
    volt_ascii = device.query("READ?")
    return float(volt_ascii)