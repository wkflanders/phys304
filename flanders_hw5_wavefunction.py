# William Flanders
# Homework 5

from scipy.integrate import *
import numpy as np
import matplotlib.pyplot as plt
from math import *

# Hermite polynomial function
def H(n, x):
    # Initializing constants
    H_0 = 1
    H_1 = 2*x

    # Base cases of n=0 and n=1
    if(n == 0):
        return H_0
    elif(n==1):
        return H_1
    else:
        # Recursive case that moves upward for the n+1th case
        for i in range(1, n):
            H_n_plus_1 = 2*x*H_1 - 2*n*H_0
            H_0 = H_1
            H_1 = H_n_plus_1
    return H_n_plus_1

# Wavefunction function
def psi(n, x):
    wavefunc = 1/(sqrt((2**n)*factorial(n)*sqrt(pi))) * e**((-x**2)/2) * H(n, x)
    return wavefunc

# Mean square position function
def f(x):
    return (x**2) * (abs(psi(5, x)))**2

def root_mean_square_pos():
    # Using scipy's quadrature function to calculate the integral
    res = quad(f, -np.Infinity, np.Infinity)
    # Taking the square root
    return sqrt(res[0])

# Printing the result
print(root_mean_square_pos())


# # For the plot of the n=30th energy level from -10 < x < 10
# x_values = []
# wavefunc = []
# for x in range(-10,10):
#     x_values.append(x)
#     wavefunc.append(psi(30, x))

# plt.plot(x_values, wavefunc, label="$\Psi_{30}$")
# plt.xlabel("x")
# plt.ylabel("$Psi_n$")
# plt.legend()
# plt.title("Wavefunction of the 30th Energy Level")
# plt.show()


# # For the plot of n=0,1,2,3 energy levels from -4 < x  < 4
# for n in range(0,4):
#     x_values = []
#     wavefunc = []
#     for x in range(-4, 4):
#         x_values.append(x)
#         wavefunc.append(psi(n,x))
#     plt.plot(x_values, wavefunc, label="$\Psi_" + str(n) + "$")

# plt.xlabel("x")
# plt.ylabel("$Psi_n$")
# plt.legend()
# plt.title("Wavefunctions of the nth Energy Level")
# plt.show()
