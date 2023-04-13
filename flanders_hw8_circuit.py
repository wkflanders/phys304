# William Flanders

import numpy as np

A = [[4,-1,-1,-1],
     [1,-3,0,1],
     [1,0,-3,1],
     [1,1,1,-4]]
b = [5,0,-5,0]

voltages = np.linalg.solve(A, b)
V_1 = voltages[0]
V_2 = voltages[1]
V_3 = voltages[2]
V_4 = voltages[3]

print(V_1, V_2, V_3, V_4)