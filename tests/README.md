# PQRG Theory Tests

Unit tests for PQRG simulations ensuring reproducibility and correctness.

## Test Files

- `test_phi_convergence.py` - Validates φ^{-1} convergence without parameter tuning
- `test_mt_dynamics.py` - Tests microtubule PLV_j coupling calculations
- `test_rg_flows.py` - Verifies RG-β flow computations

## Running Tests

Run all tests with pytest:
```bash
pytest tests/
```

Run specific test:
```bash  
pytest tests/test_phi_convergence.py -v
```

## Test Coverage

Tests verify:
- Numerical convergence to φ^{-1} ≈ 0.618
- Parameter-free results (no fine-tuning)
- Consistency with theoretical predictions
- Data format and structure

---

*Tests ensure simulation reliability for the 2026 singularity validation.*