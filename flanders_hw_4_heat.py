# William Flanders
# Homework 4

import matplotlib.pyplot as plt
from gaussxw import gaussxwab
import numpy as np

# Integrand function
def f(x):
    return (x**4 * np.e**x)/((np.e**x - 1)**2)

# Defining heat capacity function that takes temperature
def cv(T):
    # Initializing variables
    V = 0.001
    boltzmann = 1.38*(10**-23)
    rho = 6.022*(10**28)
    debye = 428
    n = 50
    # Using Newman's Gaussian quadeture function to find x values x_p and weights w_p
    xp, wp = gaussxwab(n, 0, debye/T)
    sum = 0
    # Summing all the values
    for k in range(n):
        sum += wp[k]*f(xp[k])
    # Finding heat capcity
    return 9*V*rho*boltzmann*(T/debye)**3 * sum

# Creating empty lists for heat cap and temp
cap = []
temp = []
# Looping through temperatures from 5K to 500K
for i in range(5, 501):
    # Adding the temp to the list of temperatures
    temp.append(i)
    # Adding the evaluated heat capcity at that temp to cap
    cap.append(cv(i))

# Creating the plot
plt.plot(temp, cap)
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity (J/K)")
plt.title("Heat Capcity of Aluminum as Temperature Varies")
plt.show()



