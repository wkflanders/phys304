import matplotlib.pyplot as plt

# Initializing variables
r = 1
x = 0.5

# First iteration to see if settles down to a limit cycle or fixed point
for i in range(1000):
    x = r * x * (1 - x)

# Creating the graph
plt.figure(figsize=(10,8))
plt.ylim(-0.5, 1)
plt.xlabel("r")
plt.ylabel("x")

# Using a while loop to increase r by float steps (range doesn't allow for decimal increments)
while r < 4:
    r += 0.01

    # Iterating 1000 values
    x_val = []
    for i in range(1000):
        x = r * x * (1 - x)
        x_val.append(x)

    # Plotting r vs. x for a given r value
    plt.plot([r]*len(x_val), x_val, 'ko', markersize=0.5)

plt.show()