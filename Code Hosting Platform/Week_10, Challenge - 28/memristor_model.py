import numpy as np
import matplotlib.pyplot as plt

# Constants from Biolek model paper (customize as needed)
D = 1e-9          # Thickness of memristor [m]
uv = 1e-14        # Ion mobility [m²/(V·s)]
Ron = 100         # On resistance [Ω]
Roff = 16e3       # Off resistance [Ω]
w0 = D / 10       # Initial width [m]

# Time and voltage for simulation
t = np.linspace(0, 1, 1000)  # 1 second duration
V = np.sin(2 * np.pi * 1 * t)  # 1 Hz sinusoidal voltage

dt = t[1] - t[0]
w = w0
W = [w]

# Memristor state update (Biolek model)
for v in V[:-1]:
    dw = uv * Ron * v / D * (1 - (2 * w - D)**2 / D**2)
    w += dw * dt
    w = min(max(w, 0), D)
    W.append(w)

W = np.array(W)
R = Ron * W / D + Roff * (1 - W / D)
I = V / R

# Plotting the pinched hysteresis loop
plt.figure(figsize=(8,6))
plt.plot(V, I)
plt.xlabel('Voltage [V]')
plt.ylabel('Current [A]')
plt.title('Memristor Pinched Hysteresis Loop (I-V)')
plt.grid(True)
plt.savefig('memristor_hysteresis.png')
plt.show()
