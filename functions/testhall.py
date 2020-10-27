from common_functions import *
import daq, dc

dc_ps_dev, daq_dev, dmm_dev = init_devices(['USB0::0x2A8D::0x1002::MY59001637::INSTR', 
                                  'USB0::0x2A8D::0x5101::MY58002845::0::INSTR',
                                  'USB0::0x2A8D::0x1301::MY59033786::INSTR'])

dc.set_voltage_level(dc_ps_dev, 1, 1)
dc.set_current_level(dc_ps_dev, 1, 0.2)
dmm_dev.write("CONF:CURR:DC 0.01")
dmm_dev.write("SAMPle:COUNt 10")
dmm_dev.timeout = 20000
daq_dev.timeout = 20000

dc.channel_on_off(dc_ps_dev, 1, 1)
time.sleep(1)

#dmm_dev.query("SYST:ERR?")
volt_ascii = daq.take_measurement(daq_dev, 102, 1.5625E3, 512)
curr_ascii = dmm_dev.query("READ?")

dc.channel_on_off(dc_ps_dev, 1, 0)