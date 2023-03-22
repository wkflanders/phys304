# William Flanders
# Homework 6

import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

def f(r,t):
    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y - delta*y
    return np.array([fx, fy], float)

a = 0
b = 30
N = 1000
h = (b-a)/1000

t_values = np.arange(a,b,h)
x_values = []
y_values = []

r = np.array([2,2], float)

for t in t_values:
    x_values.append(r[0])
    y_values.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h) 
    k3 = h*f(r+0.5*k2,t+0.5*h) 
    k4 = h*f(r+k3,t+h) 
    r += (k1+2*k2+2*k3+k4)/6

plt.plot(t_values, x_values, label=r'Prey Population')
plt.plot(t_values, y_values, label=r'Predator Population')
plt.suptitle(r'Predator-Prey Interaction')
plt.xlabel(r'$t$')
plt.ylabel(r'Population (in thousands)')
plt.legend()
plt.show()