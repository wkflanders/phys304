# William Flanders

import numpy as np
import matplotlib.pyplot as plt

M = 9.1094e-31     
hbar = 6.5821e-16  
e = 1.6022e-19   
L = 5.0e-10       
a = 10          

def H(m,n):
	if m == n:
		return (np.pi*hbar*n)**2/(2*M*L**2)*e+a/2
	elif (m+n)%2 == 1:
		return -8*a/(np.pi**2)*m*n/(m**2-n**2)**2
	else:
		return 0

hamiltonian = np.zeros((100,100), float)

for i in range(100):
	for j in range(100):
		hamiltonian[i,j] = H(i+1,j+1)

eigenvalues = np.linalg.eigvalsh(hamiltonian)
print(eigenvalues)

psi_n = np.linalg.eigh(hamiltonian)[1]

def psi(n,x):
    psi = sum([psi_n[n,i]*np.sin(np.pi*(i+1)*x/L) for i in range(100)])
    return np.sqrt(2.0/L)*psi

xvalues = np.linspace(0,L,1000)
pdf_ground = abs(psi(0, xvalues))**2
pdf_first = abs(psi(1, xvalues))**2
pdf_second = abs(psi(2, xvalues))**2

plt.plot(xvalues, pdf_ground, label=r"$|\psi_1|^2$")
plt.plot(xvalues, pdf_first, "_", label =r"$|\psi_2|^2$")
plt.plot(xvalues, pdf_second, ".", label=r"$|\psi_3|^2$")
plt.legend()
plt.xlabel(r"x")
plt.ylabel(r"$|\psi_n|^2$")
plt.title(r"Probability Density Functions")
plt.show()