from import_libraries import *

def init_devices(device_names): # Takes in array of devices
    rm = pyvisa.ResourceManager()
    devices = []
    for device_name in device_names:
        device = rm.open_resource(device_name)
        device.read_termination = '\n'
        devices.append(device)
    return devices
