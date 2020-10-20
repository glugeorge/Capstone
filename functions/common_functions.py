from import_libraries import *

def init_device(device_name):
    rm = pyvisa.ResourceManager()
    device = rm.open_resource(device_name)
    device.read_termination = '\n'
    return device
