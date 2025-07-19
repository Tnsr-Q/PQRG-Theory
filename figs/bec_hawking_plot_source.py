# BEC Hawking Analog Plot Generation Script

import matplotlib.pyplot as plt
import numpy as np

# Parameters from PQRG simulations and BEC analogs
# Sim decay rate ~10^{-3} s^{-1}
# Analog Hawking temperature T_H ~10 nK (nanoKelvin)
# For comparison, plot decay rate vs. time, overlaid with T_H equivalent (scaled for visualization)

t = np.linspace(0, 10, 100)  # Time in arbitrary units

decay_rate_sim = 1e-3 * np.exp(-0.1 * t)  # Exponential decay ~10^{-3} s^{-1} initial
T_H_analog = 10 * np.ones_like(t)  # Constant 10 nK for BEC analog Hawking

# Equivalent scaling: Normalize T_H to decay units (arbitrary for comparison, e.g., T_H / 10^10 for rate match)
T_H_scaled = T_H_analog / 1e12  # Scaled to ~10^{-11} for visual overlap with decay

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(t, decay_rate_sim, label='PQRG Sim Decay Rate (~10^{-3} s^{-1})', color='blue', linewidth=2)
ax.plot(t, T_H_scaled, label='Scaled BEC Analog T_H (~10 nK)', color='red', linestyle='--', linewidth=2)

ax.set_xlabel('Time (arbitrary units)')
ax.set_ylabel('Rate / Temperature (scaled units)')
ax.set_title('Comparison of PQRG Sim Decay to BEC Analog Hawking Temperature')
ax.set_yscale('log')  # Log scale to highlight scale matching
ax.legend()
ax.grid(True)

# Save as bec_hawking_plot.png
plt.savefig('bec_hawking_plot.png')
plt.close()