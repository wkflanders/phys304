# William Flanders
# Homework 6

import numpy as np
import matplotlib.pyplot as plt
from math import *

# Initializing constants
g = 9.81 # a due to gravity
l = 0.1  # length of pendulum
C = 2
cap_omega = sqrt(g/l) # resonant frequency when driven freq is equal to the natural freq

# second order ode turned into coupled first order ode's
def f(r,t): 
    theta = r[0] 
    omega = r[1] # d theta/dt
    ftheta = omega 
    fomega = -(g/l)*sin(theta) + C*cos(theta)*sin(cap_omega*t)
    return np.array([ftheta,fomega],float) 

# Initializing parameters to solve ode
a = 0
b = 100
N = 10000
h = (b-a)/N

t_values = np.arange(a,b,h)
x_values = []

x = np.array([0,0], float) # initial condition when theta = 0 degrees and omega = 0

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
plt.suptitle(r'Driven Pendulum')
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$')
plt.show()