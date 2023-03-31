import numpy as np
import matplotlib.pyplot as plt
from math import *

g = 9.81
l = 0.4
m = 0.001

def f(r,t):
    theta_1 = r[0]
    theta_2 = r[1]
    omega_1 = r[2]
    omega_2 = r[3]
    
    ftheta_1 = omega_1
    ftheta_2 = omega_2
    fomega_1 = -((omega_1**2)*sin(2*theta_1 - 2*theta_2) + 2*(omega_2**2)*sin(theta_1 - theta_2) + (g/l)*(sin(theta_1 - 2*theta_2) + 3*sin(theta_1)))/(3 - cos(2*theta_1 - 2*theta_2))
    fomega_2 = (4*(omega_1**2)*sin(theta_1 - theta_2) + (omega_2**2)*sin(2*theta_1 - 2*theta_2) + 2*(g/l)*(sin(2*theta_1 - theta_2)-sin(theta_2)))/(3-cos(2*theta_1-2*theta_2))

    return np.array([ftheta_1, ftheta_2, fomega_1, fomega_2], float)

a = 0
b = 100
N = 1000000
h = (b-a)/N
t_values = np.arange(a,b,h)

theta_1 = []
theta_2 = []
omega_1 = []
omega_2 = []
E_values = []

r = np.array([0.5*np.pi, 0.5*np.pi, 0, 0], float)
for t in t_values:
    theta_1.append(r[0])
    theta_2.append(r[1])
    omega_1.append(r[2])
    omega_2.append(r[3])
    k1 = h*f(r,t) 
    k2 = h*f(r+0.5*k1,t+0.5*h) 
    k3 = h*f(r+0.5*k2,t+0.5*h) 
    k4 = h*f(r+k3,t+h) 
    r += (k1+2*k2+2*k3+k4)/6 

for i in range(len(t_values)):
    E_values.append((m*(l**2)*((omega_1[i]**2) + 0.5*(omega_2[i]**2) + omega_1[i]*omega_2[i]*cos(theta_1[i] - theta_2[i])))-(m*g*l*(2*cos(theta_1[i] + theta_2[i]))))

plt.plot(t_values, E_values)

plt.title(r'Energy of a Double Pendulum')
plt.xlabel(r't')
plt.ylabel(r'Energy')
plt.show()
