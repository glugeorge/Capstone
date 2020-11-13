from common_functions import *
from global_variables import *

# Takes in live data (from file), plots it
def live_plot(refresh_rate=1000, data_file, scroll=False): #default is 1 sample per second
    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    # animate function
    def animate(i):
        # Parse data file for x and y
        
        if scroll and len(x)> 20: # Arbitrary window length, tbd
            x, y = x[-20:], y[-20:]
        ax.clear()
        ax.plot(x,y)
    
    ani = animation.FuncAnimation(fig, animate, interval=refresh_rate)
    plt.show()
