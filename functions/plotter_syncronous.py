from common_functions import *
from global_variables import *


def take_measurement(type):
    if type == "random":
        return random.random(), random.random()        

def choose_titles(type):
    if type == "random":
        return "random values", "random x", "random y"

# Takes in live data (from file), plots it
def live_plot(filename, type, scroll=True, refresh_rate=1000): #default is 1 sample per second
    chart_title, chart_x, chart_y = choose_titles(type)
    data_file = initiate_file(filename, chart_title, chart_x, chart_y)
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
        item1, item2 = take_measurement(type)
        save_to_file(data_file, item1, item2)
        # Parse data file for x and y
        f = open(data_file, "r")
        lines = f.readlines()
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
    live_plot("test.txt","random",scroll=True, refresh_rate=1000)
