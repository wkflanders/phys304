# William Flanders
# Homework 1

import numpy as np

# Inputing values of object at perihelion
l1 = float(input("Enter object's distance at perihelion (in m): "))
v1 = float(input("Enter object's velocity at perihilion (in m/s): "))

# Defining constants
g = 6.6738*10**(-11)
m = 1.9891*10**(30)

# Calculating velocity at aphelion using the determinant
a = 1
b = -2*g*m/(v1*l1)
c = -(v1**2 - 2*g*m/l1)
det = (b**2) - 4*a*c
root1 = (-b - det**(1/2))/2
root2 = (-b + det**(1/2))/2
v2 = min([root1, root2])

# Calculating useful quantities
l2 = l1*v1/v2
semi_major = (1/2)*(l1+l2)
semi_minor = (l1*l2)**(1/2)
period = (2*np.pi*semi_major*semi_minor)/(l1*v1)/(24*60*60)/365
eccentricity = (l2-l1)/(l2+l1)

print("l2: " + str(l2))
print("v2: " + str(v2))
print("T: " + str(period))
print("e: " + str(eccentricity))

