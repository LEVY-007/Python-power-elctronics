import numpy as np
import matplotlib.pyplot as plt

# Buck Converter Efficiency vs Load Current
Vin = 24        # Input voltage (V)
Vout = 12       # Output voltage (V)
R_on = 0.12      # On-resistance (Ohms)
fs = 50e3       # Switching frequency (50kHz)
tr = 1e-6     # Rise time (200ns) — directly defined
tf = 1e-6     # Fall time (200ns)
P_fixed = 0.5
# Load current range
IL = np.linspace(0.01, 50, 1000)

# Losses
P_conduction = IL**2 * R_on
P_switching = 0.5 * Vin * IL * (tr + tf) * fs
P_total = P_conduction + P_switching+P_fixed

# Crossover current
crossover = 0.5 * 24 * (1e-6 + 1e-6) * 50e3 / 0.12
print(f"Crossover current: {crossover:.2f}A")

# Efficiency
Pout = Vout * IL
Pin = Pout + P_total
efficiency = (Pout / Pin) * 100

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Buck Converter Efficiency Analysis', fontweight='bold')

ax1.plot(IL, efficiency, color='blue')
ax1.set_xlabel('Load Current (A)')
ax1.set_ylabel('Efficiency (%)')
ax1.set_title('Efficiency vs Load Current')
ax1.grid(True)

ax2.plot(IL, P_conduction, label='Conduction Loss', color='red')
ax2.plot(IL, P_switching, label='Switching Loss', color='green')
ax2.plot(IL, P_total, label='Total Loss', color='black', linestyle='--')
ax2.set_xlabel('Load Current (A)')
ax2.set_ylabel('Power Loss (W)')
ax2.set_title('Loss Breakdown')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

peak_idx = np.argmax(efficiency)
print(f"Peak efficiency: {efficiency[peak_idx]:.2f}% at IL={IL[peak_idx]:.2f}A")