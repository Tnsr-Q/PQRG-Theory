# Delayed-Choice Setup Protocol for ~5% Backward Flow in Cheshire Cat Experiments

## Introduction

This protocol outlines an experimental setup to test retrocausal influences in quantum systems, specifically probing ~5% backward flow in Cheshire Cat-like experiments where properties (e.g., polarization or spin) appear separated from the particle's path. Drawing from arXiv 2507.06362 ("Where Photons Have Been: Nowhere Without All Components of Their Wavefunctions" by R.E. Kastner), which emphasizes that photons are supported by all components of their wavefunctions (not truncated "first-order" portions) and highlights the Transactional Interpretation (TI) as accounting for nested interferometer phenomena, we extend this to delayed-choice scenarios. 

In PQRG theory, retrocausal handshakes (via RTI absorbers) predict measurable backward propagation (~5% influence on path signals), differing from conventional interpretations like TSVF by incorporating full wavefunction support and time-symmetric transactions.

The protocol uses a nested Mach-Zehnder interferometer with delayed measurement choices, simulating Cheshire Cat effects (e.g., photon "grinning" without the "cat"). **Expected**: ~5% backward flow manifests as anomalous signals in "cut-off" paths, quantifiable via weak measurements or photon counting statistics.

## Experimental Setup

### Required Components

- **Light Source**: Coherent laser (e.g., He-Ne at 633 nm) for single-photon or attenuated coherent states.
- **Beam Splitters (BS)**: Two 50/50 BS for outer interferometer; one additional for nested inner arm.
- **Mirrors and Phase Shifters**: Adjustable phase plates (e.g., liquid crystal retarders) for path modulation.
- **Polarization Controllers**: Half-wave plates (HWP) and quarter-wave plates (QWP) to separate properties (e.g., circular polarization as "grin").
- **Detectors**: Avalanche photodiodes (APDs) or single-photon counters at outputs; weak measurement probes (e.g., slight tilt mirrors for pointer shifts).
- **Delayed-Choice Mechanism**: Fast Pockels cell or electro-optic modulator (EOM) for post-path choice (e.g., insert/remove inner BS after photon passage).
- **Timing and Synchronization**: Picosecond-resolution timing system to ensure delayed choice (e.g., photon travel time ~ns, choice delay ~ps).

### Schematic

```
┌─────────────────────────────────────────────────────────────┐
│                    Nested Mach-Zehnder Setup               │
│                                                             │
│  Laser ──→ [Pol] ──→ [BS1] ──┬─→ Path A ("Cat Body")       │
│                              │   ┌─[HWP]─[Nested BS]─┐     │
│                              │   │                   │     │
│                              │   └─[Phase]──────────┘     │
│                              │                             │
│                              └─→ Path B ("Grin")          │
│                                  [QWP]─[Phase]            │
│                                                             │
│                     [BS2] ←──────┬──────────────────        │
│                      │           │                         │
│                     [D1]        [D2]                       │
│                                                             │
│  [Weak Probe] monitors "empty" path for ~5% backward flow  │
└─────────────────────────────────────────────────────────────┘
```

*[Insert diagram: Nested Mach-Zehnder with paths A (cat) and B (grin separation); delayed BS insertion in path A for choice; detectors D1/D2 for interference, weak probe in \"empty\" path.]*

## Procedure

### 1. Preparation
- Attenuate laser to single-photon level (~0.1 photons per pulse)
- Polarize input light circularly (e.g., |R⟩ for right-handed "grin")

### 2. Interferometer Configuration
- Photon enters outer BS, splitting into paths A and B
- **In path A ("cat body")**: Apply HWP to decouple polarization
- **In path B ("grin")**: Phase shift for property separation
- **Nested inner interferometer in path A**: Optional BS insertion for interference test

### 3. Delayed Choice
- After photon passes initial BS (verified by timing), randomly insert/remove inner BS via EOM (choice probability 50%)

### 4. Measurement
- **Weak probe** in "cut-off" path (e.g., slight mirror tilt for pointer shift, measuring ~5% anomalous flow)
- Count photons at D1/D2; compute visibility V = (I_max - I_min)/(I_max + I_min)
- Repeat ~10^6 trials for statistics

### 5. Data Analysis
- Bin results by choice timing
- Look for backward influence as ~5% signal in "empty" path when choice is "erase" (inner BS inserted post-passage)

## Expected Results

### Backward Flow (~5%)
In delayed-erase cases, ~5% anomalous pointer shift or count in cut-off path, indicating retrocausal handshake (full wavefunction support per arXiv 2507.06362).

### Difference from Orch-OR/TSVF
PQRG predicts φ-modulated flow (~0.618 damping), vs. TSVF's forward-backward vectors without entropy cost; RTI handshakes yield unique ~k_B ln(2) thermodynamic signature.

### Quantifiable Results
- **Interference visibility** V ~0.95 pre-choice
- **Drops ~5%** post-delayed erase due to backward propagation
- **PQRG signature**: φ^{-1} modulation in retrocausal signal strength

## PQRG-Specific Predictions

### Golden Ratio Modulation
```
Backward_flow_amplitude = A₀ × φ^{-1} × sin(ωt + δφ)
where φ^{-1} ≈ 0.618 (consciousness constant)
```

### RTI Entropy Cost
```
ΔS_RTI = k_B ln(2) per retrocausal handshake
Detectable as ~10^{-23} J/K thermodynamic signature
```

### Timing Constraints
```
Delay window: τ_delay > L/c (photon transit time)
Optimal: τ_delay ≈ φ × (L/c) for maximum retrocausal coupling
```

## Safety and Ethics

- Ensure laser safety (Class 1)
- Ethical review for any bio-analogs (e.g., if extending to MT-inspired probes)
- Follow standard quantum optics laboratory protocols

## Data Collection Protocol

### Statistical Requirements
- **Minimum trials**: 10^6 per configuration
- **Confidence level**: 95% (2σ)
- **Expected signal**: 5% ± 0.5%
- **Background**: <1% systematic error

### Control Experiments
- **No-delay control**: Immediate choice (classical behavior expected)
- **Empty-path monitoring**: Continuous weak measurement
- **Phase stability**: Monitor interferometer drift

## Implementation Timeline

1. **Week 1-2**: Setup assembly and alignment
2. **Week 3**: Timing system calibration
3. **Week 4-6**: Data collection (systematic parameter sweep)
4. **Week 7**: Analysis and PQRG comparison
5. **Week 8**: Results validation and publication prep

## References

- **Kastner, R.E. (2025)**. "Where Photons Have Been: Nowhere Without All Components of Their Wavefunctions." arXiv:2507.06362. (Supports full wavefunction in interferometers, TI accounting for nested phenomena).
- **Danan et al. (2013)**. Nested interferometer experiment (basis for Cheshire Cat).
- **Related**: arXiv 2406.14603 (BEC analogs for Hawking/retrocausality tests).
- **PQRG Theory**: See `../theory/retrocausal-foundations.md` for theoretical background.

## Simulation Support

For theoretical predictions and parameter optimization, see:
- `../simulations/delayed_choice_retro.py` (to be implemented)
- `../simulations/phi_convergence.py` (φ^{-1} convergence validation)

## Collaboration

Collaborate via GitHub issues for protocol refinements and experimental implementation discussions.

---

*This protocol provides a direct experimental test of PQRG retrocausal predictions, distinguishing them from conventional quantum interpretations through measurable φ^{-1} modulation and RTI entropy signatures.*