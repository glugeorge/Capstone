from import_libraries import *

def init_devices(device_names): # Takes in array of devices
    rm = pyvisa.ResourceManager()
    devices = []
    for device_name in device_names:
        device = rm.open_resource(device_name)
        device.read_termination = '\n'
        devices.append(device)
    return devices

def initiate_file():
    filename = input("file name: ")
    title = input("title: ")
    x_axis = input("x-axis title: ")
    y_axis = input("y-axis title: ")
    f = open(filename, "a")
    text = title + "\n" + x_axis + "," + y_axis + "\n"
    f.write(text)
    f.close()
    return filename

def save_to_file(filename, x, y):
    f = open(filename, "a")
    text = str(x) + "," + str(y) + "\n"
    f.write(text)
    f.close()
    return filename
