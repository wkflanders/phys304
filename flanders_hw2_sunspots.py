# William Flanders
# Homework 2

import matplotlib.pyplot as plt
import numpy as np

# Initializing constants and importing data
r = 5
data = np.loadtxt("sunspots.txt", float)

# Taking the first column of the data and saving it to time
time = data[:,0]
# Taking second column and saving it to sunspots
sunspots = data[:,1]

# Slicing time and sunspots to only the first 1000 elements
time_1000 = time[:1000]
sunspots_1000 = sunspots[:1000]

# Creating a running average variable that is the size of sunspots and is currently filled
# with zeros
running_av = np.zeros(len(sunspots_1000))
# Running a for loop where we are averageing the r previous points and the r next points
# and then saving in the running_av variable
for i in range(len(running_av)):
    running_av[i] = np.average(sunspots_1000[i:i+2*r+1])

# Making a scatter plot for the time and sunspots data
plt.scatter(time_1000, sunspots_1000, linewidth = 1, marker = '.')
# Overlayering the running average on the scatter plot
plt.plot(time_1000, running_av, 'k')
plt.xlabel("Time")
plt.ylabel("Sunspots")
plt.title("Sunspots Over Time")
plt.show()