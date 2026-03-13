# Paper 7: Dark Energy as Boundary Encoding

**The Write Rate Drives the Expansion Rate**

Charles Grant Smith Jr.  
Pegasus Intellectual Capital Solutions, Chicago, Illinois, USA  
March 2026

## Conjecture

The expansion of the universe is driven by the rate at which irreversible processes in the bulk create classical records that must be encoded on the holographic boundary. Dark energy is not a substance, a field, or a vacuum energy. It is what expansion looks like from the bulk when the boundary accommodates new information.

## Key Results

1. **QEC redundancy history** — The boundary's error-correction overcapacity κ = S_hor/S_bulk, computed from independently measured quantities with no free parameters, reaches a minimum at z ≈ 1.15 — between cosmic noon and the acceleration onset. The boundary is never stressed (κ > 10^18.7 at all epochs), but the minimum sits at exactly the right place.

2. **Dark energy is necessary** — The horizon area growth rate dA/dt correlates with the lagged star formation rate (r = 0.91 at τ = 3.5 Gyr) only in a universe with dark energy. In a matter-only (Einstein–de Sitter) universe, the correlation is absent (r = −0.21). Dark energy is what makes the expansion track the lagged write rate.

3. **Attractor behavior** — Regardless of when the star formation rate peaks (z = 1 to z = 4), the best-fit lag always adjusts so that the lagged write peak coincides with the acceleration onset: t_peak + τ_lag ≈ 7.1 ± 0.3 Gyr.

## Falsifiable Predictions

- **w ≥ −1 at all redshifts** (no phantom crossing). Testable by DESI Year 5, Euclid, LSST.
- **Acceleration onset locked to entropy production peak.** Break the lag–acceleration alignment and the conjecture dies.
- **Fine structure in H(z)** correlated with lagged SFRD, not smooth ΛCDM. Requires sub-percent H(z) precision.

## Series Context

This is Paper 7 of the holographic decoherence series:

| Paper | Topic | Status |
|-------|-------|--------|
| 1–2 | Galaxy rotation curves: a_u = cH₀/(2π) vs 171 SPARC galaxies | [Zenodo DOI: 10.5281/zenodo.18806314](https://doi.org/10.5281/zenodo.18806314) |
| 3 | Cluster-scale phenomenology (Bullet Cluster, sterile neutrinos) | Manuscript complete |
| 4 | Ultralight scalar field scoping | Draft |
| 5 | Bullet Cluster / sterile neutrino approach | Held pending Paper 6 |
| 6 | Memory kernel: lensing-gas offset vs time-since-pericenter | In preparation |
| **7** | **Dark energy as boundary encoding (this paper)** | **v3 draft** |

## Repository Structure

```
paper/
  Paper7_DarkEnergy_v3.md      — Full manuscript
code/
  qec_redundancy_history.py    — Computes κ(z) = S_hor/S_bulk across cosmic history
  lag_analysis.py              — Cross-correlates write rate with expansion rate
  significance_tests.py        — Null hypothesis tests (random humps, EdS, attractor)
  generate_figures.py          — Generates all four paper figures
figures/
  figure1_kappa_history.png    — QEC redundancy trajectory
  figure2_write_rate_expansion.png — Write rate, lagged write rate, dA/dt
  figure3_attractor_eds.png    — Attractor behavior + EdS comparison
  figure4_timeline.png         — Cosmic timeline
data/
  summary_statistics.txt       — Key numerical results
```

## Requirements

```
numpy >= 1.24
scipy >= 1.10
matplotlib >= 3.7
```

No external data downloads required. All inputs (Planck 2018 cosmological parameters, Madau & Dickinson 2014 SFRD, Egan & Lineweaver 2010 entropy budget) are hardcoded from published values.

## Running

```bash
# Reproduce all results
python code/qec_redundancy_history.py
python code/lag_analysis.py
python code/significance_tests.py

# Regenerate figures
python code/generate_figures.py
```

## License

This work is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Acknowledgments

The author thanks Claude (Anthropic) for computational assistance. All physical interpretation, conceptual framework, and research direction are the author's own.
