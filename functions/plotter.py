from common_functions import *
from global_variables import *

# Takes in live data (from file), plots it
def live_plot(refresh_rate=1000, data_file, scroll=False): #default is 1 sample per second
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
        # Parse data file for x and y
        f = open(data_file, "r")
        lines = f.readlines()
        if len(lines) > len(x)+2:
            for line in lines[len(x)+2:]:
                x.append(line.split(",")[0])
                y.append(line.split(",")[1])
    
        if scroll and len(x)> 20: # Arbitrary window length, tbd
            x_plot, y_plot = x[-20:], y[-20:]
        else:
            x_plot, y_plot = x,y
        ax.clear()
        ax.plot(x_plot,y_plot)
    
    ani = animation.FuncAnimation(fig, animate, interval=refresh_rate)
    plt.show()
