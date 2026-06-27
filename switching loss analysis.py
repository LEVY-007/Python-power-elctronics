import numpy as np
import matplotlib.pyplot as plt

# Parameters
Vin = 24        # Input voltage (V)
Iload = 5       # Load current (A)
Ciss = 1e-9     # MOSFET input capacitance (1nF)

# Frequency range: 1kHz to 1MHz
fs = np.linspace(1e3, 1e6, 1000)

# Gate resistance values
Rg_values = [10, 47, 100]  # Ohms

# ── Figure with 2 subplots ──────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('MOSFET Switching Loss Analysis', fontsize=14, fontweight='bold')

# ── Plot 1: Switching Loss vs Frequency (for each gate resistance) ──
for Rg in Rg_values:
    tr = 2.2 * Rg * Ciss   # Rise time from RC theory
    tf = 2.2 * Rg * Ciss   # Fall time
    P = 0.5 * Vin * Iload * (tr + tf) * fs
    ax1.plot(fs/1e3, P, label=f'Rg={Rg}Ω')

ax1.set_xlabel('Switching Frequency (kHz)')
ax1.set_ylabel('Switching Loss (W)')
ax1.set_title('Switching Loss vs Frequency')
ax1.legend()
ax1.grid(True)

# ── Plot 2: Switching Loss vs Gate Resistance (at fixed frequency) ──
fs_fixed = 100e3            # Fixed at 100kHz
Rg_range = np.linspace(1, 200, 200)  # Gate resistance 1 to 200 Ohms

tr_range = 2.2 * Rg_range * Ciss
tf_range = 2.2 * Rg_range * Ciss
P_vs_Rg = 0.5 * Vin * Iload * (tr_range + tf_range) * fs_fixed

ax2.plot(Rg_range, P_vs_Rg, color='red')
ax2.set_xlabel('Gate Resistance (Ω)')
ax2.set_ylabel('Switching Loss (W)')
ax2.set_title('Switching Loss vs Gate Resistance (fs=100kHz)')
ax2.grid(True)

# ── Print numerical values ──────────────────────────────────────
print("Switching Loss at fs=100kHz:")
for Rg in Rg_values:
    tr = 2.2 * Rg * Ciss
    tf = 2.2 * Rg * Ciss
    P = 0.5 * Vin * Iload * (tr + tf) * fs_fixed
    print(f"  Rg={Rg}Ω → tr={tr*1e9:.1f}ns → Loss={P*1000:.2f}mW")

plt.tight_layout()
plt.show()