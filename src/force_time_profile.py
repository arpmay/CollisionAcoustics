import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 0.5 * 0.025  # 2.5 cm diameter ball, so radius = 1.25 cm = 0.0125 m
E_star = 120e9 / (2 * (1 - 0.34**2))  # Using the earlier combined modulus of elasticity formula
k = (4/3) * np.sqrt(R) * E_star
delta_max = 4.42e-5  # from our previous calculations
t_max = 2.38e-4  # from our previous calculations

# Time array
t = np.linspace(0, 2*t_max, 1000)  # twice t_max to cover the full trapezoidal profile

# Indentation over time
delta_t = delta_max * (t/t_max - 0.5 * (t/t_max)**2)

# Force over time
F_t = k * delta_t

# Plotting
plt.figure(figsize=(10,6))
plt.plot(t, F_t)
plt.title("Force vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Force (N)")
plt.grid(True)
plt.tight_layout()
plt.show()
