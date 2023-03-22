# William Flanders
# Homework 6

import numpy as np
from math import *
import matplotlib.pyplot as plt

# Initializing constants
g = 9.81 # a due to gravity
l = 0.1  # length of pendulum

# second order ode turned into coupled first order ode's
def f(r,t): 
    theta = r[0] 
    omega = r[1] # d theta/dt
    ftheta = omega 
    fomega = -(g/l)*sin(theta) 
    return np.array([ftheta,fomega] ,float) 

# Initializing parameters to solve ode
a = 0
b = 10
N = 1000
h = (b-a)/N

t_values = np.arange(a,b,h)
x_values = []

x = np.array([179*pi/180,0], float) # initial condition when theta = 179 degrees

# Runge-Kutta 4
for t in t_values: 
    x_values.append(x[0])  
    k1 = h*f(x,t) 
    k2 = h*f(x+0.5*k1,t+0.5*h) 
    k3 = h*f(x+0.5*k2,t+0.5*h) 
    k4 = h*f(x+k3,t+h) 
    x += (k1+2*k2+2*k3+k4)/6 

# Plotting the solution
plt.plot(t_values, x_values)
plt.suptitle(r'Nonlinear Pendulum')
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$')
plt.show()