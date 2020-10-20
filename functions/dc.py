from common_functions import *
from global_variables import *

def channel_on_off(device,channel,state):
    device.write("OUTPut {}, (@{})".format(state,channel))
# TODO: Add error handling

def set_voltage_level(device,channel,voltage):
    device.write("VOLT {}, (@{})".format(voltage,channel))

def set_current_level(device,channel,current)
    dc_ps.write("CURR {},(@{})".format(current,channel))

## Below is test code ##
if __name__ == "__main__":
    dc = init_device("USB0::0x2A8D::0x1002::MY59001637::INSTR")
    set_voltage_level(dc,1,0.5)
