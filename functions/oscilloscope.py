from common_functions import *
from global_variables import *

def capture_waveform(device,channel,points):
    device.write(":WAV:SOUR CHAN{}".format(channel)) # Read from channel
    device.write(":WAV:FORMAT ASCII") # Read back data in ASCII format
    device.write(":WAVeform:POINts {}".format(points))
    wfm_ascii = scope.query(":WAV:DATA?") # Get the first amount of points of waveform data
    wfm_ascii = wfm_ascii[:-1] # Remove a trailing ','
    wfm_ascii = wfm_ascii.split(' ', maxsplit=1)[1]
    return wfm_ascii
