# William Flanders
# Homework 2

import numpy as np
import matplotlib.pyplot as plt

# Initializing theta variable that is an interval from 0 to 2pi
theta = np.linspace(0, 2*np.pi)

# Creating functions for x and y
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

# Plotting x against y
plt.plot(x, y)
plt.title("Deltoid")
plt.show()