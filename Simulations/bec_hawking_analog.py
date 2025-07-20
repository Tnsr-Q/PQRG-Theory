import numpy as np
import matplotlib.pyplot as plt

# Parameters from PQRG simulations and BEC analogs (ref: arXiv 2410.02700)
# Sim decay rate ~10^{-3} s^{-1} (phonon emission in correlation functions)
# Analog Hawking temperature T_H ~10 nK (traces in BEC acoustic black holes)

# Time array for simulation
t = np.linspace(0, 10, 100)  # Arbitrary time units

# Simulated decay rate: Exponential form approximating phonon emission decay
decay_rate_sim = 1e-3 * np.exp(-0.05 * t)  # Initial ~10^{-3} s^{-1}, tuned for visualization

# Analog T_H: Constant ~10 nK, scaled to rate units for comparison (e.g., via k_B T / hbar ~ frequency)
# Scaling factor arbitrary (e.g., T_H / 1e12 to match decay order ~10^{-11} to 10^{-3})
T_H_analog = 10 * np.ones_like(t)  # nK
scaling_factor = 1e-12  # Adjust to overlay orders (nK to s^{-1} proxy)
T_H_scaled = T_H_analog * scaling_factor

# Plot comparison
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, decay_rate_sim, label='PQRG Sim Decay Rate (~10^{-3} s^{-1})', color='blue', linewidth=2)
ax.plot(t, T_H_scaled, label='Scaled BEC Analog T_H (~10 nK)', color='red', linestyle='--', linewidth=2)
ax.set_xlabel('Time (arbitrary units)')
ax.set_ylabel('Rate / Scaled Temperature (units)')
ax.set_title('Comparison of PQRG Decay to BEC Analog Hawking T_H (arXiv 2410.02700)<grok-card data-id="f8eca7" data-type="citation_card"></grok-card>')
ax.set_yscale('log')  # Log scale to highlight matching orders
ax.legend()
ax.grid(True)

# Save as bec_hawking_plot.png
plt.savefig('bec_hawking_plot.png')
plt.close()
