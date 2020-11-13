from common_functions import *
from global_variables import *

# animate function
def animate(i,ax,x,y):
    ax.clear()
    ax.plot(x,y)


# Takes in live data (from file), plots it
def live_plot(refresh_rate, data_file):
    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # Parse data_file for x, y 
    
    ani = animation.FuncAnimation(fig, animate, fargs=(ax, x, y), interval=refresh_rate)
    plt.show()
