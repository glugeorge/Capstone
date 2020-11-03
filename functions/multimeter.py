from common_functions import *
from global_variables import *

def measure_current(device,range,ac_dc='DC',sample_count=1):
    device.write("CONF:CURR:{} {}".format(ac_dc,range))
    device.write("SAMPle:COUNt {}".format(sample_count))
    curr_ascii = device.query("READ?")
    return curr_ascii


def measure_voltage(device,range,ac_dc='DC',sample_count=1):
    device.write("CONF:VOLT:{} {}".format(ac_dc,range))
    device.write("SAMPle:COUNt {}".format(sample_count))
    volt_ascii = device.query("READ?")
    return volt_ascii
