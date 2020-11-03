from common_functions import *
import daq, dc, multimeter


def take_measurement():
    dc.channel_on_off(dc_ps_dev, 1, 1)
    time.sleep(1)
    
    #dmm_dev.query("SYST:ERR?")
    volt_ascii = daq.take_measurement(daq_dev, 102, 1.5625E3, 512)
    curr_ascii = multimeter.measure_current(dmm_dev, 0.01)
    
    voltage = np.mean([float(s) for s in volt_ascii.split(',')])
    current = float(curr_ascii)
    
    dc.channel_on_off(dc_ps_dev, 1, 0)
    
    return voltage, current


if __name__ == "__main__":
    dc_ps_dev, daq_dev, dmm_dev = init_devices(['USB0::0x2A8D::0x1002::MY59001637::INSTR', 
                                      'USB0::0x2A8D::0x5101::MY58002845::0::INSTR',
                                      'USB0::0x2A8D::0x1301::MY59033786::INSTR'])
    
    dc.set_voltage_level(dc_ps_dev, 1, 1)
    dc.set_current_level(dc_ps_dev, 1, 0.2)
    
    dmm_dev.timeout = 20000
    daq_dev.timeout = 20000
    
    # V12I34, V13I42, etc.
    measurements = {}
    
    # Resistivity measurement
    for i in range(2):
        v_p = input("Voltage positive contact: ")
        v_n = input("Voltage negative contact: ")
        i_p = input("Current positive contact: ")
        i_n = input("Current negative contact: ")
        measurements[f"V{v_p}{v_n}I{i_p}{i_n}"] = take_measurement()
    
    # Hall measurement
    for i in range(2):
        v_p = input("Voltage positive contact: ")
        v_n = input("Voltage negative contact: ")
        B_pol = input("Magnetic field polarity (p/n): ")
        measurements[f"V{v_p}{v_n}{B_pol}"] = take_measurement()