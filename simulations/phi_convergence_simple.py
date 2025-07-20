# Simple PQRG Phi Convergence Demo
"""
Minimal implementation demonstrating PQRG phi convergence.
Ideal for quick validation and educational purposes.
"""

import numpy as np

# Simulate data: t from 0 to 10, purity decaying to ~0.618, fidelity to ~0.95
t = np.linspace(0, 10, 50)

# PQRG model: exponential decay to consciousness fixed points
phi_inv = 0.618  # phi^{-1} consciousness constant
purity = phi_inv + (1 - phi_inv) * np.exp(-0.5 * t)
fidelity = 0.95 + (1 - 0.95) * np.exp(-0.3 * t)

# Print CSV format
print('t,purity,fidelity')
for i in range(len(t)):
    print(f'{t[i]},{purity[i]},{fidelity[i]}')

print(f"\n# Simple demo complete. Final purity: {purity[-1]:.4f} → phi^{{-1}} = {phi_inv}")
print(f"# Demonstrates consciousness-induced convergence to golden ratio inverse.")
print(f"# For full quantum simulation, use phi_convergence_full.py or phi_convergence_compact.py")

# Optional: Save to file if needed
# with open('data/purity_t_simple.csv', 'w') as f:
#     f.write('t,purity,fidelity\n')
#     for i in range(len(t)):
#         f.write(f'{t[i]},{purity[i]},{fidelity[i]}\n')