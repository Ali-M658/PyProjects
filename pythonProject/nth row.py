import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11   # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8         # Speed of light (m/s)
H0 = 70.0         # Hubble constant (km/s/Mpc)
H0 = H0 * 1e3 / 3.086e22  # Convert to s^-1

# Parameters
omega_m = 0.3  # Matter density parameter
omega_l = 0.7  # Dark energy density parameter
omega_k = 1.0 - omega_m - omega_l  # Curvature density parameter

def friedmann(a):
    """
    Friedmann equation to calculate the Hubble parameter squared.
    """
    return H0**2 * (omega_m / a**3 + omega_l + omega_k / a**2)

def equation_of_state(a):
    """
    Calculate the equation of state parameter w.
    """
    H2 = friedmann(a)
    rho_m = omega_m * H0**2 / a**3
    rho_l = omega_l * H0**2
    rho_total = rho_m + rho_l
    p_l = -rho_l * c**2  # Pressure of dark energy
    w = p_l / (rho_total * c**2)
    return w

# Time evolution parameters
a_values = np.linspace(0.01, 20.0, 1000)  # Scale factor range from very small to 2.0
w_values = equation_of_state(a_values)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(a_values, w_values, label='w(a)', color='blue')
plt.axhline(-1, color='red', linestyle='--', label='w = -1')
plt.xlabel('Scale factor a')
plt.ylabel('Equation of State Parameter w')
plt.title('Equation of State Parameter w vs Scale Factor a')
plt.legend()
plt.grid(True)
plt.show()

# Check if w goes below -1
if np.any(w_values < -1):
    print("The equation of state parameter w goes below -1.")
else:
    print("The equation of state parameter w does not go below -1.")