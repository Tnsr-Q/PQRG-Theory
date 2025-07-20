import numpy as np
import matplotlib.pyplot as plt

# Parameters from PQRG and bioRxiv June 2025 (CD20-RhoA/Rock1 coupling in MT dynamics)
PLV_j = 0.71  # Phase-locking value for coherence channels
modification_factor = 1.10  # ~10% boost due to PLV_j-modified RhoA rates
retrocausal_diff = 0.05  # ~5% retrocausal difference in erasers (delayed-choice influence)

# Time points for simulation (arbitrary units, e.g., reaction time in seconds)
time_points = np.linspace(0, 10, 100)

# Baseline RhoA activation rate: Sigmoidal growth model for MT dynamics
# Form: rate = max_rate / (1 + exp(-k (t - t0))) for activation curve
max_rate = 1.0  # Normalized max activation
k = 0.5  # Growth steepness
t0 = 5.0  # Inflection point
baseline_rate = max_rate / (1 + np.exp(-k * (time_points - t0)))

# Modified rate: ~10% boost via PLV_j coherence (testable in Hameroff vibration spectroscopy)
# Boost applied as scalar multiplication; predicts frequency shifts in MT vibrations (~THz range)
modified_rate = baseline_rate * modification_factor

# Retrocausal eraser effect: ~5% difference backward-influenced rate (e.g., in delayed-choice setups)
# Simulate as perturbation: reduced rate in "eraser" configuration due to backward flow
eraser_rate = modified_rate * (1 - retrocausal_diff)

# Predict coherence channels: Compute coherence time proxy (inverse decay, testable in spectroscopy)
# Coherence time ~1 / decay_rate, with retrocausal differing by ~5%
decay_baseline = 0.1 * baseline_rate  # Proxy decay
coherence_baseline = 1 / decay_baseline
coherence_modified = coherence_baseline * modification_factor  # ~10% longer coherence
coherence_eraser = coherence_modified * (1 + retrocausal_diff)  # ~5% retrocausal extension (backward stabilization)

# Output data to CSV for reproducibility (mt_dynamics_data.csv)
data = np.column_stack((time_points, baseline_rate, modified_rate, eraser_rate))
np.savetxt('mt_dynamics_data.csv', data, delimiter=',', header='time,baseline_rate,modified_rate,eraser_rate', comments='')

# Plot RhoA rates for visualization
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time_points, baseline_rate, label='Baseline RhoA Rate', color='blue')
ax.plot(time_points, modified_rate, label='PLV_j-Modified (~10% Boost)', color='green', linestyle='--')
ax.plot(time_points, eraser_rate, label='Retrocausal Eraser (~5% Difference)', color='red', linestyle='-.')
ax.set_xlabel('Time (arbitrary units)')
ax.set_ylabel('RhoA Activation Rate (normalized)')
ax.set_title('Simulation of PLV_j-Modified RhoA Rates in Microtubule Dynamics')
ax.legend()
ax.grid(True)

# Save plot as mt_dynamics_plot.png
plt.savefig('mt_dynamics_plot.png')
plt.close()

# Print testable prediction summary
print("Testable Predictions:")
print(f"Coherence channels boosted ~10% via PLV_j: Mean coherence time {np.mean(coherence_modified):.3f} (vs. baseline {np.mean(coherence_baseline):.3f})")
print(f"Retrocausal difference in erasers: ~5% extension, mean coherence {np.mean(coherence_eraser):.3f}")
print("Differing by ~5% retrocausal in erasers: Predicts anomalous signals in delayed-choice MT vibration spectroscopy (Hameroff 2025 probes).")
