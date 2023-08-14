import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Fundamental Constants & Assumptions
# ------------------------------

# Speed of sound in copper (m/s)
c = 4750

# Young's Modulus for copper (Pa)
E = 110e9

# Density of copper (kg/m^3)
rho = 8960

# Poisson's ratio for copper
nu = 0.34

# Assuming a 1 kg copper sphere, we'll first find its volume and then radius
# Volume = mass/density
V = 1.0 / rho

# Radius calculation for a sphere: V = (4/3)*pi*R^3
R = (3*V/(4*np.pi))**(1/3)

# Using the combined modulus of elasticity for two identical spheres
E_star = E / (2 * (1 - nu**2))

# Contact stiffness k for the collision of two spheres
k = (4/3) * np.sqrt(R) * E_star

# ------------------------------
# Calculating Fundamental Frequency
# ------------------------------

# Using the formula for the fundamental frequency of a spherical object:
f0 = c / (2*np.pi*R) * np.sqrt(3*E/rho)

# ------------------------------
# Indentation Over Time
# ------------------------------

# Constants for the indentation profile
delta_max = 4.42e-5  # m
t_max = 2.38e-4  # s
t = np.linspace(0, 2*t_max, 1000)  # time array

# Quadratic function representing the indentation over time
delta_t = delta_max * (t/t_max - 0.5 * (t/t_max)**2)

# ------------------------------
# Force-Time Profile
# ------------------------------

# Using Hertzian contact theory for two identical spheres
F_t = k * delta_t

# ------------------------------
# Sound Waveform Generation
# ------------------------------

# The waveform will be a sine wave (representing the fundamental frequency)
# modulated by the force-time profile
sound_waveform = np.sin(2 * np.pi * f0 * t) * F_t

# ------------------------------
# Plotting
# ------------------------------

plt.figure(figsize=(10, 6))
plt.plot(t, sound_waveform)
plt.title("Generated Sound Waveform vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

