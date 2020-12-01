from common_functions import *
from global_variables import *
import daq, dc, multimeter

def take_measurement(measurement, t_0, device=None, channel=101):
    if measurement == "random":
        return random.random()
    if measurement == "time":
        t = time.time() - t_0
        return t
    if measurement == "voltage":
        volt_ascii = daq.take_measurement(device, channel)
        voltage = np.mean([float(s) for s in volt_ascii.split(',')])
        return voltage
    if measurement == "current":
        current = multimeter.measure_current(device, 0.01)
        return current
    if measurement == "two voltages":
        volt_ascii1, volt_ascii2 = daq.take_measurement(device, "101,102")
        voltage1 = np.mean([float(s) for s in volt_ascii1.split(',')])
        voltage2 = np.mean([float(s) for s in volt_ascii2.split(',')])
        return f"{voltage1},{voltage2}"

def initiate_measurement():
    dc_ps_dev, daq_dev, dmm_dev = init_devices(['USB0::0x2A8D::0x1002::MY59001637::INSTR',
                                          'USB0::0x2A8D::0x5101::MY58002845::0::INSTR',
                                          'USB0::0x2A8D::0x1301::MY59033786::INSTR'])
    dc.set_voltage_level(dc_ps_dev, 1, 1)
    dc.set_current_level(dc_ps_dev, 1, 0.2)
    daq.initialize_device(daq_dev, 102, rate=800E3, voltage=18)
    return dc_ps_dev, daq_dev, dmm_dev

def setup(filename, x_value, y_value):
    # Setting up chart titles
    chart_title = f"{y_value} vs {x_value}"
    data_file = initiate_file(filename, chart_title, x_value, y_value)
    dc_ps_dev, daq_dev, dmm_dev = initiate_measurement()
    device_dict = {
        "random": None,
        "time": None,
        "voltage": daq_dev,
        "current": dmm_dev,
        "two voltages": daq_dev
        }
    return data_file, dc_ps_dev, device_dict[x_value], device_dict[y_value]

# Takes in live data (from file), plots it
def live_plot(filename, x_value, y_value, scroll=True, refresh_rate=1000): #default is 1 sample per second
    data_file, dc_ps_dev, device_1, device_2 = setup(filename, x_value, y_value)
    absolute_time = time.time()
    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = []
    y = []
    y1 = []
    f = open(data_file, "r")
    lines = f.readlines()
    title = lines[0]
    x_axis, y_axis = lines[1].split(",")[0], lines[1].split(",")[1]
    f.close()

    # animate function
    def animate(i):
        item1, item2 = take_measurement(x_value, absolute_time, device_1, 102), take_measurement(y_value, absolute_time, device_2)
        save_to_file(data_file, item1, item2)
        y_vals = str(item2).split(",")
        x.append(item1)
        y.append(float(y_vals[0]))
        if len(y_vals)>1:
            y1.append(float(y_vals[1]))

        """
        # Slows down code, consider replacing with append statement above
        # Parse data file for x and y
        f = open(data_file, "r")
        lines = f.readlines()
        f.close()
        if len(lines) > len(x)+2:
            for line in lines[len(x)+2:]:
                x.append(float(line.split(",")[0]))
                y.append(float(line.split(",")[1]))
        """

        if scroll and len(x)> 20: # Arbitrary window length, tbd
            x_plot, y_plot = x[-20:], y[-20:]
            if len(y_vals)>1:
                y1_plot = y1[-20:]
        else:
            x_plot, y_plot, y1_plot = x,y,y1
        ax.clear()
        ax.plot(x_plot,y_plot)
        if len(y_vals)>1:
            ax.plot(x_plot,y1_plot)
        plt.title(title)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)

    ani = animation.FuncAnimation(fig, animate, interval=int(refresh_rate))
    plt.show()

if __name__ == "__main__":
    live_plot("test.txt","random_vs_time",scroll=False, refresh_rate=100)
