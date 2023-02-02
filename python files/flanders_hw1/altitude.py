# William Flanders
# Homework 1

import numpy as np

# Defining constants
g = 6.67 * 10**(-11)
r = 6371000
m = 5.97 * 10**(24)

# Taking input for period
t = int(input("Enter period in seconds: "))

# Calculating height 
h = ((g*m*t**2)/(4*(np.pi)**2))**(1/3) - r

print("The height is " + str(h) + " for an orbital period of " + str(t))