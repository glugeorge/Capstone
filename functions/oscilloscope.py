"""Functions to interface with the Keysight oscilloscope.

"""

from common_functions import *
from global_variables import *

def capture_waveform(device, channel, points):
    """Function to capture numerical data of the waveform shown on the oscilloscope.
    
    Args:
        device (str): Device ID of the oscilloscope.
        channel (str): Channel on the oscilloscope to read from.
        points (int or str): Number of waveform points to be transferred.
    
    Returns:
        Single ASCII string of all the data points separated by commas.
    
    """
    device.write(f":WAV:SOUR CHAN{channel}") # Read from channel
    device.write(":WAV:FORMAT ASCII") # Read back data in ASCII format
    device.write(f":WAVeform:POINts {points}")
    wfm_ascii = scope.query(":WAV:DATA?") # Get the first amount of points of waveform data
    wfm_ascii = wfm_ascii[:-1] # Remove a trailing ','
    wfm_ascii = wfm_ascii.split(' ', maxsplit=1)[1]
    return wfm_ascii