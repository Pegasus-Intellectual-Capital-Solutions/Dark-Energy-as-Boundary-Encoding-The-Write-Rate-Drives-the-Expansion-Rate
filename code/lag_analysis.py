#!/usr/bin/env python3
"""
lag_analysis.py
================
Cross-correlates the bulk write rate (SFRD) with the horizon area growth rate
dA/dt to find the best-fit encoding lag. Tests the conjecture that the write rate
drives expansion with a delay.

Part of Paper 7: Dark Energy as Boundary Encoding
Charles Grant Smith Jr., March 2026
"""
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

# Constants
c = 3e8; G = 6.674e-11; hbar = 1.055e-34
lP = 1.616e-35; H0_si = 67.4e3 / 3.086e22
Gyr_s = 3.156e16; Om = 0.315; OL = 0.685; Or = 9.1e-5

def H(z): return H0_si * np.sqrt(Or*(1+z)**4 + Om*(1+z)**3 + OL)
def dHdz(z):
    dz = 0.001
    return (H(z+dz) - H(z-dz)) / (2*dz)

def cosmic_time(z):
    if z > 1e4: return 0
    result, _ = quad(lambda zp: 1.0/((1+zp)*H(zp)), z, 1e4, limit=500)
    return result / Gyr_s

# Horizon area A = 4π(c/H)²
def A_hor(z):
    return 4 * np.pi * (c / H(z))**2

# dA/dt: rate of horizon area growth
# A = 4πc²/H², so dA/dt = -8πc²/(H³) × dH/dt
# dH/dt = dH/dz × dz/dt = dH/dz × (-(1+z)H)
def dAdt(z):
    dhdz = dHdz(z)
    dhdt = dhdz * (-(1+z) * H(z))  # dH/dt in 1/s²
    return -8 * np.pi * c**2 / (H(z)**3) * dhdt

# Write rate: irreversible entropy production rate
# Dominated by SMBH growth at late times, stellar radiation throughout
# Use Madau & Dickinson SFRD as proxy for total write rate
def sfrd(z):
    return 0.015 * (1+z)**2.7 / (1 + ((1+z)/2.9)**5.6)

# BH accretion rate tracks SFRD with slight delay
# Total write rate ∝ SFRD + BH_accretion
# BH entropy production rate >> stellar photon rate per unit mass
# But track together as proportional for now
def write_rate(z):
    """Total bulk entropy production rate (arbitrary normalization)"""
    # Stellar: each Msun of stars → ~10^57 photon entropy bits
    # BH: each Msun accreted → ~10^77 bits (Bekenstein-Hawking for ~10^8 Msun BH)
    # BH accretion rate ~ 0.001 × SFRD
    # So entropy: stellar ~ SFRD × 10^57, BH ~ 0.001 × SFRD × 10^77 = SFRD × 10^74
    # BH dominates entropy production rate by ~10^17!
    # But both track SFRD proportionally, so shape is the same
    return sfrd(z)

# Build time-redshift mapping
z_grid = np.linspace(0, 6, 2000)
t_grid = np.array([cosmic_time(z) for z in z_grid])

# Interpolators: z(t) and t(z)
z_of_t = interp1d(t_grid, z_grid, kind='cubic', fill_value='extrapolate')
t_of_z = interp1d(z_grid, t_grid, kind='cubic', fill_value='extrapolate')

# Compute both curves as functions of cosmic time
t_eval = np.linspace(0.5, 13.5, 500)  # Gyr
z_eval = np.array([float(z_of_t(t)) for t in t_eval])

# 1. Horizon area growth rate (normalized)
dA_vals = np.array([dAdt(z) for z in z_eval])
dA_norm = dA_vals / np.max(np.abs(dA_vals))

# 2. Write rate (normalized)
wr_vals = np.array([write_rate(z) for z in z_eval])
wr_norm = wr_vals / np.max(wr_vals)

# 3. Lagged write rate: shift by τ_enc
# If expansion at time t is driven by writes at time (t - τ_enc),
# then dA/dt(t) should correlate with write_rate(t - τ_enc)
# which means write_rate curve shifted RIGHT by τ_enc

# Find best-fit lag by cross-correlation
from scipy.signal import correlate
lags_to_test = np.linspace(0, 4, 200)  # Gyr
correlations = []
for lag in lags_to_test:
    # Shift write rate by lag: wr(t - lag)
    wr_shifted = np.array([write_rate(float(z_of_t(max(t - lag, 0.5)))) for t in t_eval])
    wr_shifted_norm = wr_shifted / np.max(wr_shifted)
    # Correlation with dA/dt
    # Only use region where both are well-defined
    mask = (t_eval > 1.0 + lag) & (t_eval < 13.0)
    corr = np.corrcoef(dA_norm[mask], wr_shifted_norm[mask])[0, 1]
    correlations.append(corr)

best_lag_idx = np.argmax(correlations)
best_lag = lags_to_test[best_lag_idx]
best_corr = correlations[best_lag_idx]

print("=" * 80)
print("WRITE RATE vs EXPANSION RATE: LAG ANALYSIS")
print("=" * 80)

print(f"\nBest-fit lag: τ_enc = {best_lag:.2f} Gyr")
print(f"Peak correlation: r = {best_corr:.4f}")
print(f"Zero-lag correlation: r = {correlations[0]:.4f}")

# Print key epochs
print(f"\n{'Quantity':<35} {'Peak z':>8} {'Peak t (Gyr)':>12}")
print("-" * 60)

# Peak write rate
wr_peak_idx = np.argmax(wr_vals)
print(f"{'Write rate (SFRD proxy)':<35} {z_eval[wr_peak_idx]:>8.2f} {t_eval[wr_peak_idx]:>12.2f}")

# Peak dA/dt
dA_peak_idx = np.argmax(dA_vals[t_eval > 1])  # skip very early
dA_peak_idx += np.sum(t_eval <= 1)
print(f"{'Horizon area growth rate dA/dt':<35} {z_eval[dA_peak_idx]:>8.2f} {t_eval[dA_peak_idx]:>12.2f}")

# Acceleration onset (where deceleration parameter q changes sign)
# q = -1 - dH/dt / H^2
for i, z in enumerate(z_eval):
    dhdt = dHdz(z) * (-(1+z)*H(z))
    q = -1 - dhdt / H(z)**2
    if q < 0 and i > 10:
        print(f"{'Acceleration onset (q=0)':<35} {z:>8.2f} {t_eval[i]:>12.2f}")
        break

# κ minimum from previous calculation
print(f"{'κ minimum':<35} {'1.15':>8} {'5.30':>12}")

print(f"\n{'Lagged write rate peak':<35} {z_eval[wr_peak_idx]:>8.2f} → arrives at t = {t_eval[wr_peak_idx] + best_lag:>5.2f} Gyr")

# Now print the timeline
print("\n" + "=" * 80)
print("TIMELINE")
print("=" * 80)
events = [
    (t_eval[wr_peak_idx], "Peak write rate (cosmic noon)"),
    (5.30, "κ minimum (boundary overcapacity bottleneck)"),
    (t_eval[wr_peak_idx] + best_lag, "Lagged write rate peak (encoding complete)"),
    (7.29, "Acceleration onset (q = 0)"),
    (13.79, "Today"),
]
events.sort(key=lambda x: x[0])
for t, desc in events:
    z = float(z_of_t(t)) if t < 13.5 else 0
    print(f"  t = {t:>5.1f} Gyr  (z ≈ {z:>4.1f})  {desc}")

# Print lag scan results around best fit
print("\n" + "=" * 80)
print("LAG SCAN DETAIL")
print("=" * 80)
print(f"{'Lag (Gyr)':>10} {'Correlation':>12}")
print("-" * 25)
for i in range(0, len(lags_to_test), 10):
    marker = " ← best" if abs(lags_to_test[i] - best_lag) < 0.05 else ""
    print(f"{lags_to_test[i]:>10.2f} {correlations[i]:>12.4f}{marker}")

# Finally: what does this tell us about the deceleration->acceleration transition?
print("\n" + "=" * 80)
print("KEY PHYSICAL INTERPRETATION")
print("=" * 80)
print(f"""
Write rate (bulk decoherence) peaks at cosmic noon: z ≈ 2, t ≈ 3.3 Gyr
The boundary must encode these records with a lag of τ ≈ {best_lag:.1f} Gyr
The encoding completion peaks at t ≈ {t_eval[wr_peak_idx] + best_lag:.1f} Gyr (z ≈ {float(z_of_t(t_eval[wr_peak_idx] + best_lag)):.1f})
The boundary's overcapacity κ reaches its minimum at z ≈ 1.15 (t ≈ 5.3 Gyr)
The expansion accelerates at z ≈ 0.7 (t ≈ 7.3 Gyr)

The sequence is:
  cosmic noon → κ minimum → encoding peak → acceleration onset
  (z ≈ 2)      (z ≈ 1.1)   (z ≈ {float(z_of_t(t_eval[wr_peak_idx] + best_lag)):.1f})       (z ≈ 0.7)
""")

