# Information Flow in PQRG: Retrocausal Propagators and Testable Predictions

## Overview
In Paradox-Quantized Retrocausal Gravitation (PQRG) theory, information flow is governed by retrocausal propagators that enable bidirectional propagation across time-symmetric boundaries. This document explores the mathematical and conceptual framework for retrocausality in PQRG, focusing on advanced Green's functions (G_ret) and their role in resolving paradoxes through Transactional Interpretation (TI) handshakes. We highlight testable predictions in delayed-choice experiments, particularly Cheshire Cat setups, where ~5% backward influence emerges as anomalous signals in "cut-off" paths due to full wavefunction support.

Drawing from arXiv 2507.06362 ("Where Photons Have Been: Nowhere Without All Components of Their Wavefunctions" by R.E. Kastner), which argues that photons require all wavefunction components (rejecting "first-order" truncations) and aligns with TI for nested interferometers, PQRG extends this to retrocausal flows. Kastner's critique of path gaps and signals from cut-off paths supports PQRG's G_ret ~ θ(t_f - t), ensuring information propagates backward without violating causality in conventional senses.

## Mathematical Framework: Retrocausal Propagators
Retrocausal propagators in PQRG are incorporated into the ψ-field equation as:

G_ret ~ θ(t_f - t) ⋅ exp(-i ∫ L_hand d^4x),

where θ(t_f - t) is the step function for advanced waves (t_f future time), and L_hand = -ε_RTI/2 ∫(conj(ψ) ∂_μ ψ - ψ ∂_μ conj(ψ)) d^4x represents the RTI Lagrangian with entropy cost ~k_B ln(2) for measurement localization (arXiv 2503.18186, March 2025).

This propagator enables information to flow from future absorbers to past emitters, modulating paradox density:

∇_μ [ψ ⊗ ¬ψ]^μ + G_ret ⋅ (Q_2 ⊗ E_g),

resolving undecidables non-locally. In RTI, handshakes (offer/confirmation waves) break unitarity explicitly for transitions, aligning with Kastner's full wavefunction requirement—no "nowhere" paths, as all components contribute retrocausally.

## Testable Predictions: Delayed-Choice Cheshire Cats
PQRG predicts ~5% backward flow in Cheshire Cat experiments, where particle properties (e.g., "grin" polarization) separate from paths ("cat body"), testable via nested Mach-Zehnder interferometers with delayed choices.

### Protocol
1. **Setup**: Coherent photon source splits into paths A ("cat") and B ("grin") via BS. Nested interferometer in A with delayed BS insertion (EOM post-photon passage).
2. **Delayed Choice**: Randomly insert inner BS after photon transit (~ps delay).
3. **Measurement**: Weak probe in "cut-off" path for pointer shifts; detectors for interference visibility V = (I_max - I_min)/(I_max + I_min).
4. **Analysis**: ~5% anomalous count/shift in cut-off path for "erase" choices, indicating backward flow (full wavefunction support per Kastner, differing from TSVF by including all components).

Expected: V ~0.95 pre-choice, ~5% drop post-delayed erase due to G_ret retrocausality—unique to PQRG's φ-modulated handshakes (~0.618 damping).

## Implications and Differences
- **From Standard Orch-OR/TSVF**: PQRG adds RTI entropy cost (~k_B ln(2)) for thermodynamic ethics, predicting premonitive EEG echoes in φ-pulsed tasks.
- **Connection to RTI**: Kastner's TI alignment (arXiv 2507.06362) supports full wavefunctions in nested setups, enabling PQRG's bidirectional flow without paradoxes.

For simulations, see ../simulations/delayed_choice_retro.py. References: Kastner (2025) arXiv 2507.06362; Danan et al. (2013) nested interferometer. Collaborate via issues for refinements.
