import matplotlib.pyplot as plt
import numpy as np

# Creating interval of values for x and y with 1000 steps in between
x_values = np.linspace(-2, 2, 1000)
y_values = np.linspace(-2, 2, 1000)

# Creating the emtpy NxN grid (where N = 1000)
grid = np.zeros([1000,1000])

# Looping across all values of x and y
for u, x in enumerate(x_values):
    for v, y in enumerate(y_values):
        # Initializing z
        z = 0 + 0j
        # Turning our x and y values into a complex number
        c = complex(x,y)
        # Performing 100 iterations
        for i in range(100):
            # Squaring z and then adding our created complex number
            z = z**2 + c
            # Checking if the absolute value is greater than 2
            if abs(z) > 2:
                # If it is, we change the zero to a one in the grid
                grid[u, v] = 1
                # We exit out the iteration
                break
# Creating the plot with our grid
plt.imshow(grid, origin = "lower", extent=(-2,2,-2,2))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fractal from Mandelbrot Set")
plt.gray()
plt.show()
