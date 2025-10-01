import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# System parameters (same as motor demo)
k = 10.0     # stiffness [Nm/rad]
c = 5.0     # damping [Nms/rad]
m = 1.0     # mass [kg*m^2]

omega_n = np.sqrt(k / m)             # rad/s
zeta = c / (2 * np.sqrt(k * m))      # dimensionless

print(f"Natural frequency ω_n = {omega_n:.2f} rad/s")
print(f"Damping ratio ζ = {zeta:.2f}")

# Transfer function: X(s)/U(s) = 1 / (m s^2 + c s + k)
num = [1.0]
den = [m, c, k]
system = signal.TransferFunction(num, den)

# Time vector for simulation
t = np.linspace(0, 20, 1000)

# 1) Step response
t_step, x_step = signal.step(system, T=t)
x_scaled = x_step * k

# --------------------
# Plot results
# --------------------
plt.figure(figsize=(12, 8))

# Step response
plt.subplot(1, 1, 1)
plt.plot(t_step, x_scaled)
plt.title(f"Step Response (ω_n={omega_n:.2f} rad/s, ζ={zeta:.2f})")
plt.xlabel("Time [s]")
plt.ylabel("Displacement [rad]")

plt.tight_layout()
plt.show()
