"""Functions to interface with the Keysight DC power supply.

"""

from common_functions import *
from global_variables import *

def channel_on_off(device, channel, state):
    """Function to turn a channel on/off on the DC power supply.
    
    Args:
        device (str): Device ID of the DC power supply.
        channel (str): Channel on the power supply to turn on/off.
        state (int): 1 for on, 0 for off.
    
    Returns:
        None.
    
    """
    device.write(f"OUTPut {state}, (@{channel})")

def set_voltage_level(device, channel, voltage):
    """Function to set output voltage level on the DC power supply.
    
    Args:
        device (str): Device ID of the DC power supply.
        channel (str): Channel on the power supply to set the voltage level.
        voltage (int): Voltage level to set in volts.
    
    Returns:
        None.
    
    """
    device.write(f"VOLT {voltage}, (@{channel})")

def set_current_level(device, channel, current):
    """Function to set output current level on the DC power supply.
    
    Args:
        device (str): Device ID of the DC power supply.
        channel (str): Channel on the power supply to set the current level.
        current (int): Current level to set in amperes.
    
    Returns:
        None.
    
    """
    device.write(f"CURR {current},(@{channel})")

## Below is test code ##
if __name__ == "__main__":
    dc = init_device("USB0::0x2A8D::0x1002::MY59001637::INSTR")
    set_voltage_level(dc,1,0.5)