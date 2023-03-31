from numpy import array,arange,multiply,power,absolute,sqrt
import matplotlib.pyplot as plt
# Constants 
m = 9.1094e-31 
hbar = 1.0546e-34 
e = 1.6022e-19 
N = 1000 
alpha = (1*10**(-11))
V0 = 50*e
a = -5*alpha
b = 5*alpha
h = (b-a)/N 

def V(x): 
    return V0*(x**4/alpha**4)

def f(r,x,E): 
    psi = r[0] 
    phi = r[1]
    fpsi = phi 
    fphi = (2*m/hbar**2)*(V(x)-E)*psi 
    return array([fpsi,fphi] ,float) 

# # Calculate the wavefunction for a particular energy 
# def solve(E): 
#     psi = 0.0 
#     phi = 1.0 
#     r = array([psi,phi] ,float) 

#     for x in arange(a,b,h): 
#         k1 = h*f(r,x,E) 
#         k2 = h*f(r+0.5*k1,x+0.5*h,E) 
#         k3 = h*f(r+0.5*k2,x+0.5*h,E) 
#         k4 = h*f(r+k3,x+h,E) 
#         r += (k1+2*k2+2*k3+k4)/6 
#     return r[0] 

# Main program to find the energy using the secant method 
# E1 = 1446*e
# E2 = 2100*e
# psi2 = solve(E1) 

# target = e/1000 
# while abs(E1-E2)>target: 
#     psi1,psi2 = psi2,solve(E2) 
#     E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1) 

# print("E =" ,E2/e, "eV")

psi = 0.0 
phi = 1.0 
def solve(E): 
    phi_values = []
    r = array([psi,phi] ,float)
    for x in arange(a,b,h): 
        phi_values.append(r[0])
        k1 = h*f(r,x,E) 
        k2 = h*f(r+0.5*k1,x+0.5*h,E) 
        k3 = h*f(r+0.5*k2,x+0.5*h,E) 
        k4 = h*f(r+k3,x+h,E) 
        r += (k1+2*k2+2*k3+k4)/6 
    return phi_values

def normalize(phi):
    phi_values = array(phi)
    phi_sq_abs = absolute(power(phi_values, 2))
    for i in range(1, N):
        sum = phi_sq_abs[0] + phi_sq_abs[-1]
        if i%2 == 1:
            sum += 4 * phi_sq_abs[i]
        else:
            sum += 2 * phi_sq_abs[i]
    coeff = (h/(3))*sum
    coeff = 1/sqrt(coeff)
    return coeff


x_values = arange(a,b,h)
phi_1 = solve(205.307*e)
phi_2 = solve(735.691*e)
phi_3 = solve(1443.570*e)

norm_coef_1 = normalize(phi_1)
norm_coef_2 = normalize(phi_2)
norm_coef_3 = normalize(phi_3)

norm_phi_1 = multiply(phi_1, norm_coef_1)
norm_phi_2 = multiply(phi_2, norm_coef_2)
norm_phi_3 = multiply(phi_3, norm_coef_3)

plt.plot(x_values, norm_phi_1, label=r'Wavefunction for n=0')
plt.plot(x_values, norm_phi_2, '.',label=r'Wavefunction for n=1')
plt.plot(x_values, norm_phi_3, '_',label=r'Wavefunction for n=2')
plt.xlabel(r"x")
plt.ylabel(r"Wavefunction")
plt.title("Normalized Wavefunctions for Anharmonic Oscillator")
plt.legend()
plt.show()