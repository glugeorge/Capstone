from common_functions import *
from global_variables import *
import daq

def take_high_freq(filename,user_rate,user_time,channel=101):
    initiate_file(filename,'voltage v time','time','voltage')
    daq_dev = init_devices(['USB0::0x2A8D::0x5101::MY58002845::0::INSTR'])[0]
    daq.initialize_device(daq_dev, channel, count = float(user_time)*1.562E3)
    data_ascii= daq.take_measurement(daq_dev,channel)
    data_list = [float(s) for s in data_ascii.split(',')]
    rate_ratio = int(1.562E3 / float(user_rate))
    to_save = 0
    time = 0
    item_count = 0
    for item in data_list:
        item_count += 1
        to_save += float(item)
        if item_count == rate_ratio:
            to_save = to_save/item_count
            save_to_file(filename, time, to_save)
            time += 1/float(user_rate)
            item_count = 0
            to_save = 0

if __name__ == "__main__":
    data_list = take_high_freq('test.txt', 100, 5)