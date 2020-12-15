from common_functions import * # don't need this if init in main/experiments
from global_variables import *

def initialize_device(device, channel, rate=1.562E3, count=512, voltage=3):
     device.write(f"ACQ3:VOLT {voltage},DEF,DEF,DEF,{count},{rate},(@{channel})")
     device.timeout = 20000

def take_measurement(device, channel):
    #set_sample_rate(device,channel,rate)
    #set_sample_count(device,channel,count)
    #device.timeout = 20000
    device.write("INITiate3 (@{})".format(channel))
    channels = str(channel).split(',')
    datalist = []
    for c in channels:
        datalist.append(device.query("FETCh3? (@{})".format(c)))
    
    return datalist[0] if len(datalist) == 1 else datalist

def live_acquisition(device, channel, rate=1.562E3, count=512, voltage=3):
    filename = initiate_file('test.txt')
    initialize_device(device, channel, rate, count, voltage)
    start = time.time()
    while True:
        volt_ascii = take_measurement(device,channel)
        t = time.time() - start
        voltage = np.mean([float(s) for s in volt_ascii.split(',')])
        save_to_file(filename, t, voltage)
        time.sleep(0.05)
