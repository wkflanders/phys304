# William Flanders
# Homework 2

import numpy as np
import matplotlib.pyplot as plt

# Initializing the value of theta as an interval from 0 to 10pi with 1000 steps
theta = np.linspace(0, 10*np.pi, 1000)

# Creating functions for x and y
x = (theta**2)*np.cos(theta)
y = (theta**2)*np.sin(theta)

# Plotting x against y
plt.plot(x, y)
plt.title("Galilean Spiral")
plt.show()