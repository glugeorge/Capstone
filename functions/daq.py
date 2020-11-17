from common_functions import * # don't need this if init in main/experiments
from global_variables import *

def set_sample_rate(device,channel,rate):
    device.write("SAMPle3:RATE {},(@{})".format(rate,channel))

def set_sample_count(device,channel,count):
    device.write("SAMPle3:COUNt {},(@{})".format(count,channel))

def initialize_device(device, channel, rate=1.562E3,count=512,voltage=3):
     device.write(f"ACQ3:VOLT {voltage},DEF,DEF,DEF,{count},{rate},(@{channel})")
     device.timeout = 20000

def take_measurement(device,channel,rate=1.562E3,count=512):
    #set_sample_rate(device,channel,rate)
    #set_sample_count(device,channel,count)
    #device.timeout = 20000
    device.write("INITiate3 (@{})".format(channel))
    data = device.query("FETCh3? (@{})".format(channel))
    return data

def live_acquisition(device,channel,rate=1.562E3,count=512,voltage=3):
    filename = initiate_file()
    initialize_device(device, channel, rate, count, voltage)
    start = time.time()
    while True:
        volt_ascii = take_measurement(device,channel)
        t = time.time() - start
        voltage = np.mean([float(s) for s in volt_ascii.split(',')])
        save_to_file(filename, t, voltage)
        time.sleep(0.05)