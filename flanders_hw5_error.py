# William Flanders
# Homework 5

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


# Using Recursion to find Bessel function
def J_rec(n, x):
    
    # Initializing J_0 and J_1 using Simpson's rule
    J_0 = J(0, x)
    J_1 = J(1, x)

    # Base cases for when n = 0 or n = 1, return the initialized values
    if(n == 0):
        return J_0
    elif(n== 1):
        return J_1
    else:
    # Recursive case for when n > 1    
        for i in range(1, n):
            # Stepping through all values of n, moving upwards, and calculating the n+1th order until we reach our target n
            J_n_plus_1 = ((2*n)/x)*J_1 - J_0
            J_0 = J_1
            J_1 = J_n_plus_1
    return J_n_plus_1


# Generating plots and values for Simpson's rule Bessel and Recursive Bessel
for i in range(2,5):
    x_values = []
    Jn = []
    Jn_rec = []
    error = []

    # Looping through a range of x values, and using both methods to calculate the value of the bessel function
    for x in range(10, 71):
        x_values.append(x)
        Jn.append(J(i ,x))
        Jn_rec.append(J_rec(i, x))

    # Finding the error between Simpson's and recursion 
    for k in range(len(x_values)):
        error.append(abs(Jn[k] - Jn_rec[k]))

    # Plotting Simpson's vs. recurssion
    plt.plot(x_values, Jn, label="Simpson's Rule")
    plt.plot(x_values, Jn_rec, '--', label = "Recursion")
    plt.xlabel("x")
    plt.ylabel("$J_n$")
    plt.title("Recursion vs. Simpson's Rule for J" + str(i))
    plt.legend()
    plt.show()
    plt.clf()

    # Plotting the error between the two methods
    plt.plot(x_values, error)
    plt.xlabel("x")
    plt.ylabel("Error")
    plt.title("Error Between Recursion and Simpson's Rule for J" + str(i))
    plt.show()
    plt.clf
    

    

