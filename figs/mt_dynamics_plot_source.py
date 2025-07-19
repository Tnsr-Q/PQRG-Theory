# Microtubule Dynamics Plot Generation Script

import matplotlib.pyplot as plt
import numpy as np

# Simulate RhoA rates: Baseline vs. Modified by PLV_j coupling (~10% boost)
# Data inspired by bioRxiv June 2025 CD20-RhoA/Rock1 coupling in MT dynamics

time_points = np.linspace(0, 10, 100)  # Time in arbitrary units (e.g., reaction time)

baseline_rate = 0.5 * (1 - np.exp(-0.2 * time_points))  # Baseline RhoA activation rate
modified_rate = baseline_rate * 1.10  # ~10% modification due to PLV_j coherence boost

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(time_points, baseline_rate, label='Baseline RhoA Rate (No PLV_j Modification)', color='blue', linewidth=2)
ax.plot(time_points, modified_rate, label='Modified RhoA Rate (~10% Boost via PLV_j)', color='green', linestyle='--', linewidth=2)

ax.set_xlabel('Time (arbitrary units)')
ax.set_ylabel('RhoA Activation Rate')
ax.set_title('Visualization of RhoA Rates ~10% Modifications in Microtubule Dynamics')
ax.legend()
ax.grid(True)

# Save as mt_dynamics_plot.png
plt.savefig('mt_dynamics_plot.png')
plt.close()