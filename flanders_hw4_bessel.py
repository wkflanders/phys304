# William Flanders
# Homework 4

import matplotlib.pyplot as plt
from math import *

# Integrand function for Bessel function 
def f(m, x, theta):
    return cos(m*theta - x*sin(theta))

# Using Simpson's Rule to find Bessel function
def J(m, x):
    # Initializing variables
    n = 1000
    a = 0
    b = pi
    h = (b-a)/n

    # Initalizing the sum
    sum = f(m, x, a) + f(m, x, b)

    # Looping through all values from 1 to N
    for i in range(1, n):
        # Defining theta
        theta = a + i * h
        # If the index is odd
        if i%2 == 1:
            sum += 4 * f(m, x, theta)
        # If the index is even
        else:
            sum += 2 * f(m, x, theta)
    # Dividing by 1/3 (from Simpson's) and 1/pi (from Bessel's)
    sum = (h/(3*pi))*sum
    # Returning the sum
    return sum

# Generating all the values for x, J_0, J_1, and J_2
x_values = []
J0 = []
J1 = []
J2 = []
for x in range(21):
    x_values.append(x)
    J0.append(J(0,x))
    J1.append(J(1,x))
    J2.append(J(2,x))

# Creating the plot
plt.plot(x_values, J0, label="$J_0(x)$")
plt.plot(x_values, J1, '--', label="$J_1(x)$")
plt.plot(x_values, J2, '-.', label="$J_2(x)$")
plt.xlabel("x")
plt.ylabel("$J_m$")
plt.legend()
plt.title("Bessel Functions of the First Kind")
plt.show()
