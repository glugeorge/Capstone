from common_functions import *
from global_variables import *
import daq, dc

def take_measurement(type, t_0, device, channel):
    if type == "random":
        return random.random(), random.random()
    if type == "random_vs_time":
        t = time.time() - t_0
        volt_ascii = daq.take_measurement(device, channel)
        voltage = np.mean([float(s) for s in volt_ascii.split(',')])
        return t, voltage

def choose_titles(type):
    if type == "random":
        return "random values", "random x", "random y"
    if type == "random_vs_time":
        return "random values vs time", "time", "random y"

# Takes in live data (from file), plots it
def live_plot(filename, type, scroll=True, refresh_rate=1000): #default is 1 sample per second
    
    dc_ps_dev, daq_dev, dmm_dev = init_devices(['USB0::0x2A8D::0x1002::MY59001637::INSTR', 
                                      'USB0::0x2A8D::0x5101::MY58002845::0::INSTR',
                                      'USB0::0x2A8D::0x1301::MY59033786::INSTR'])
    
    dc.set_voltage_level(dc_ps_dev, 1, 1)
    dc.set_current_level(dc_ps_dev, 1, 0.2)
    daq.initialize_device(daq_dev, 102, rate=800E3, voltage=18)


    chart_title, chart_x, chart_y = choose_titles(type)
    data_file = initiate_file(filename, chart_title, chart_x, chart_y)
    absolute_time = time.time()
    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = []
    y = []
    f = open(data_file, "r")
    lines = f.readlines()
    title = lines[0]
    x_axis, y_axis = lines[1].split(",")[0], lines[1].split(",")[1]
    f.close()

    # animate function
    def animate(i):
        item1, item2 = take_measurement(type, absolute_time, daq_dev, 104)
        save_to_file(data_file, item1, item2)
        # Parse data file for x and y
        f = open(data_file, "r")
        lines = f.readlines()
        f.close()
        if len(lines) > len(x)+2:
            for line in lines[len(x)+2:]:
                x.append(float(line.split(",")[0]))
                y.append(float(line.split(",")[1]))

        if scroll and len(x)> 20: # Arbitrary window length, tbd
            x_plot, y_plot = x[-20:], y[-20:]
        else:
            x_plot, y_plot = x,y
        ax.clear()
        ax.plot(x_plot,y_plot)
        plt.title(title)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)

    ani = animation.FuncAnimation(fig, animate, interval=refresh_rate)
    plt.show()

if __name__ == "__main__":
    live_plot("test.txt","random_vs_time",scroll=False, refresh_rate=100)
