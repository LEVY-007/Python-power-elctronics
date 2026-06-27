import numpy as np
import matplotlib.pyplot as plt

Vin = 24
Iload = 5
fs = np.linspace(1e3, 1e6, 1000)

# Three gate resistances — affect rise/fall times
gate_configs = [
    {'Rg': '10Ω', 'tr': 30e-9, 'tf': 30e-9},
    {'Rg': '47Ω', 'tr': 50e-9, 'tf': 50e-9},
    {'Rg': '100Ω', 'tr': 80e-9, 'tf': 80e-9},
]

for config in gate_configs:
    P = 0.5 * Vin * Iload * (config['tr'] + config['tf']) * fs
    plt.plot(fs/1e3, P, label=f"Rg={config['Rg']}")

plt.xlabel('Switching Frequency (kHz)')
plt.ylabel('Switching Loss (W)')
plt.title('Switching Loss vs Frequency for Different Gate Resistances')
plt.legend()
plt.grid(True)
plt.show()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1 — Loss vs Frequency (fixed Rg=47Ω)
ax1.plot(fs/1e3, P_middle, color='red')
ax1.set_xlabel('Frequency (kHz)')
ax1.set_ylabel('Switching Loss (W)')
ax1.set_title('Loss vs Frequency')
ax1.grid(True)

# Plot 2 — Loss vs Gate Resistance (fixed fs=100kHz)
ax2.plot(...)
ax2.set_title('Loss vs Gate Resistance')
ax2.grid(True)

plt.tight_layout()
plt.show()