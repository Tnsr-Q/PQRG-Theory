# LHC-Fibonacci T-Violation Simulation

"""
Simulation of T-violation asymmetries in LHC O-Ne collisions at φ-multiple energies.
Based on PQRG theory predictions for retrocausal handshake amplification.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import golden  # φ ≈ 1.618

# PQRG parameters
N_r = 0.641681  # Paradox density threshold
E_0 = 6.5  # Baseline energy per nucleon in TeV (LHC Pb-Pb analog, scaled for O-Ne)
phi = golden  # Golden ratio ≈1.618
n_max = 5  # Number of Fibonacci-scaled pulses (n=0 to 5)

# Simulate T-violation asymmetry as function of energy
# Toy model: Asymmetry peaks at energies ~ N_r TeV with φ-modulation
# A(E) = N_r * sin(2 * π * E / φ) * exp(- (E - N_r)^2 / (2 * 0.1^2))  # Gaussian peak at N_r

def t_violation_asymmetry(E):
    """
    Calculate T-violation asymmetry for given energy.
    
    Args:
        E: Energy in TeV/nucleon
        
    Returns:
        T-violation asymmetry amplitude
    """
    return N_r * np.sin(2 * np.pi * E / phi) * np.exp(- (E - N_r)**2 / (2 * 0.1**2))

def run_lhc_fibonacci_simulation():
    """
    Run the complete LHC-Fibonacci simulation and generate visualization.
    """
    
    # Generate pulse energies: E_n = E_0 * φ^n
    energies = E_0 * np.power(phi, np.arange(n_max + 1))
    
    # Compute asymmetries for each pulse
    asymmetries = t_violation_asymmetry(energies)
    
    # Print results
    print("LHC-Fibonacci Pulse Energies (TeV/nucleon):")
    print("=" * 50)
    for n, E in enumerate(energies):
        print(f"n={n}: E={E:.3f} TeV, T-violation Asymmetry={asymmetries[n]:.4f}")
    
    print(f"\nN_r threshold: {N_r:.6f}")
    print(f"Golden ratio φ: {phi:.6f}")
    print(f"Maximum asymmetry: {np.max(np.abs(asymmetries)):.4f}")
    
    # Generate fine energy grid for smooth curve
    E_fine = np.linspace(0, np.max(energies) * 1.2, 1000)
    asymmetry_fine = t_violation_asymmetry(E_fine)
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    
    # Plot smooth curve
    plt.plot(E_fine, asymmetry_fine, '-', color='blue', alpha=0.7, 
             label='T-violation Asymmetry (continuous)')
    
    # Plot discrete pulse points
    plt.plot(energies, asymmetries, 'ro', markersize=8, 
             label='Fibonacci Pulse Energies', zorder=5)
    
    # Mark N_r threshold
    plt.axhline(N_r, color='red', linestyle='--', linewidth=2, 
                label=f'N_r Threshold ({N_r:.3f})')
    plt.axhline(-N_r, color='red', linestyle='--', linewidth=2, alpha=0.7)
    
    # Mark zero line
    plt.axhline(0, color='black', linestyle='-', alpha=0.3)
    
    # Annotations for pulse points
    for n, (E, A) in enumerate(zip(energies, asymmetries)):
        plt.annotate(f'n={n}', xy=(E, A), xytext=(E, A + 0.05), 
                    ha='center', fontsize=10, 
                    arrowprops=dict(arrowstyle='->', color='red', alpha=0.7))
    
    plt.xlabel('Pulse Energy (TeV/nucleon)', fontsize=12)
    plt.ylabel('T-violation Asymmetry', fontsize=12)
    plt.title('LHC-Fibonacci Variants: O-Ne Pulses at φ-Multiples\n' + 
              'PQRG Theory Predictions for Retrocausal T-Violation', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    # Add text box with key parameters
    textstr = f'φ = {phi:.3f}\nN_r = {N_r:.3f}\nE_0 = {E_0} TeV'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    
    # Save figure
    plt.savefig('lhc_fibonacci_asymmetry.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Export data for further analysis
    data = np.column_stack((energies, asymmetries))
    np.savetxt('data/lhc_fibonacci_data.csv', data, 
               header='Energy_TeV,T_Violation_Asymmetry', 
               delimiter=',', comments='')
    
    print(f"\nData saved to: data/lhc_fibonacci_data.csv")
    print(f"Plot saved to: lhc_fibonacci_asymmetry.png")
    
    return energies, asymmetries

if __name__ == "__main__":
    # Run simulation
    energies, asymmetries = run_lhc_fibonacci_simulation()
    
    # Additional analysis
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)
    
    peak_idx = np.argmax(np.abs(asymmetries))
    print(f"Peak asymmetry at n={peak_idx}, E={energies[peak_idx]:.3f} TeV")
    print(f"Peak value: {asymmetries[peak_idx]:.4f}")
    
    # Find which pulses are near N_r threshold
    near_threshold = np.abs(energies - N_r) < 0.5
    if np.any(near_threshold):
        threshold_pulses = np.where(near_threshold)[0]
        print(f"Pulses near N_r threshold: {threshold_pulses}")
        for pulse in threshold_pulses:
            print(f"  n={pulse}: E={energies[pulse]:.3f} TeV, ΔE={energies[pulse]-N_r:.3f} TeV")
