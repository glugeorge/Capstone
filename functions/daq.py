from common_functions import * # don't need this if init in main/experiments
from global_variables import *

def set_sample_rate(device,channel,rate):
    device.write("SAMPle3:RATE {},(@{})".format(rate,channel))

def set_sample_count(device,channel,count):
    device.write("SAMPle3:COUNt {},(@{})".format(count,channel))

def take_measurement(device,channel,rate,count):
    set_sample_rate(device,channel,rate)
    set_sample_count(device,channel,count)
    device.write("INITiate3 (@{})".format(channel))
    #device.timeout = int(count)/int(rate)
# May need to do some conversion of sorts from their rate format to integer
    data = device.query("FETCh3? (@{})".format(channel))
    return data
