# William Flanders
# Homework 1

for z in range(1, 101):
    # Looping through elements 1 to 100 (101 since range() is non inclusive)

    # Initializing variables for each element
    largest_b_per_n = 0
    largest_a = 0
    largest_z = 0

    for a in range(z, (3*z)+1):
        # Looping through all the possible mass values for an element from its atomic number to 3 times its atomic number
        
        # Initializing constant values
        const_1 = 15.8
        const_2 = 18.3
        const_3 = 0.714
        const_4 = 23.2

        # Constant 5 is dependent on the atomic number
        if a%2 == 0 and z%2 == 0:
            # If both atomic and mass number are even
            const_5 = 12.0
        elif a%2 == 0 and z%2 != 0:
            # If mass number is even but atomic number is odd
            const_5 = -12.0 
        else:
            # If both mass and atomic number are odd
            const_5 = 0

        # Breaking up the calculation into each seperate term 
        term_1 = const_1*a
        term_2 = const_2*(a**(2/3))
        term_3 = const_3*((z**2)/(a**(1/3)))
        term_4 = const_4*(((a-2*z)**2)/(a))
        term_5 = const_5/(a**(1/2))

        # Finding the binding energy
        b = term_1 - term_2 - term_3 - term_4 + term_5

        # Finding the binding energy per nucleon
        b_per_n = b/a

        # Testing to see if the current iteration of mass leads to a larger
        # binding energy per nucleon than the currently accepted binding energy per nucleon
        if b_per_n > largest_b_per_n:
            # If it does, setting the atomic number, mass number, and binding energy per nucleon to
            # "largest" variables
            largest_b_per_n = b_per_n
            largest_a = a
            largest_z = z

    # After each elemenet, printing out the atomic number and its corresponding largest
    # mass and binding energy per nucleon
    #print("The most stable mass is " + str(largest_a) + " for atomic number " + str(z) + " with bonding energy per nucleus " + str(largest_b_per_n))
    print("Z: " + str(largest_z) + " A: " + str(largest_a) + " B/A " + str(largest_b_per_n))

