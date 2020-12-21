"""Global variables that are used by other modules.

These are intended to be read-only variables. Update the device IDs (and optionally the
data folder path) before using the software!
Add other device IDs here as needed.
"""

# DC power supply
dc_ps_name = 'USB0::0x2A8D::0x1002::MY59001637::INSTR'
# DAQ system
daq_name = 'USB0::0x2A8D::0x5101::MY58002845::0::INSTR'
# Digital multimeter
dmm_name = 'USB0::0x2A8D::0x1301::MY59033786::INSTR'

# Data folder path. Include the trailing backslash!
# All data files will be saved to this location.
data_dir_name = r"C:\Users\student\Documents\GitHub\Capstone\data" + "\\"