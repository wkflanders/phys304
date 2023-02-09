# William Flanders
# Homework 2

import numpy as np
import matplotlib.pyplot as plt

# Initializing theta variable as an interval from 0 to 24pi with 10000 steps
theta = np.linspace(0, 24*np.pi, 10000)

# Finding the value of r
r = np.e**(np.cos(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**5

# Finding the value of x and y
x = r*np.cos(theta)
y = r*np.sin(theta)

# Plotting x against y
plt.plot(x, y)
plt.title("Fey's Function")
plt.show()