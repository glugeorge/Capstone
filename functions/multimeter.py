from common_functions import *
from global_variables import *

def initialize_device(device, range, ac_dc='DC', sample_count=1):
    device.write(f"CONF:CURR:{ac_dc} {range}")
    device.write(f"SAMPle:COUNt {sample_count}")
    device.timeout = 20000

def measure_current(device,range,ac_dc='DC',sample_count=1):
    #device.write("CONF:CURR:{} {}".format(ac_dc,range))
    #device.write("SAMPle:COUNt {}".format(sample_count))
    #device.timeout = 20000
    curr_ascii = device.query("READ?")
    return curr_ascii


def measure_voltage(device,range,ac_dc='DC',sample_count=1):
    device.write("CONF:VOLT:{} {}".format(ac_dc,range))
    device.write("SAMPle:COUNt {}".format(sample_count))
    device.timeout = 20000
    volt_ascii = device.query("READ?")
    return volt_ascii
