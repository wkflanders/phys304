# William Flanders
# Homework 4

import matplotlib.pyplot as plt
from math import *
import numpy as np

# Using Simpson's Rule to find value of Bessel function of first kind 
def f(m, x, theta):
    return cos(m*theta - x*sin(theta))

def J(m, x):
    n = 1000
    a = 0
    b = pi
    h = (b-a)/n

    sum = f(m, x, a) + f(m, x, b)
    for i in range(1, n):
        theta = a + i * h
        if i%2 == 1:
            sum += 4 * f(m, x, theta)
        else:
            sum += 2 * f(m, x, theta)
    sum = (h/(3*pi))*sum
    return sum

# Intensity function
def I(r):
    lmbda = 0.5
    k = (2*pi)/lmbda
    intensity = (J(1,k*r)/(k*r))**2
    return intensity

# Number of pixels
pixels = 500
# Seperation between pixels on the grid
sepration = 0.008
# Creating an N x N grid 
grid = np.empty([pixels,pixels],float)

# Looping through all x and y coordinates
for i in range(pixels):
    # Starting from the center of x and y
    y = sepration*(i - pixels/2) 
    for j in range(pixels):
        x = sepration*(j - pixels/2)
        # Finding r
        r = sqrt(x**2 + y**2)
        # Plugging in r for the intensity function
        # We know that the lim r-> 0 (J(x)/x) = 1/2
        # So we incorporate this into the code and set a soft limit of when r < 10^-8
        if r < 10**-8:
            grid[i,j] = 0.5
        else:
            grid[i,j] = I(r)

# Plotting the density plot 
plt.imshow(grid,vmax=0.1,cmap='hot')
plt.gray()
plt.show()

