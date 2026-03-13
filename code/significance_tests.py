#!/usr/bin/env python3
"""
significance_tests.py
======================
Null hypothesis tests for the write-rate / expansion-rate correlation.
Tests: random Gaussians, randomized SFRD, phase-shifted SFRD, Einstein-de Sitter,
and attractor sensitivity analysis.

Part of Paper 7: Dark Energy as Boundary Encoding
Charles Grant Smith Jr., March 2026
"""
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

c = 3e8; H0_si = 67.4e3 / 3.086e22
Gyr_s = 3.156e16; Om = 0.315; OL = 0.685; Or = 9.1e-5

def H(z): return H0_si * np.sqrt(Or*(1+z)**4 + Om*(1+z)**3 + OL)
def dHdz(z):
    dz = 0.001
    return (H(z+dz) - H(z-dz)) / (2*dz)
def cosmic_time(z):
    if z > 1e4: return 0
    result, _ = quad(lambda zp: 1.0/((1+zp)*H(zp)), z, 1e4, limit=500)
    return result / Gyr_s
def dAdt(z):
    dhdt = dHdz(z) * (-(1+z) * H(z))
    return -8 * np.pi * c**2 / (H(z)**3) * dhdt
def sfrd(z):
    return 0.015 * (1+z)**2.7 / (1 + ((1+z)/2.9)**5.6)

z_grid = np.linspace(0, 6, 1000)
t_grid = np.array([cosmic_time(z) for z in z_grid])
z_of_t = interp1d(t_grid, z_grid, kind='cubic', fill_value='extrapolate')

t_eval = np.linspace(0.5, 13.5, 300)
z_eval = np.array([float(z_of_t(t)) for t in t_eval])
dA_vals = np.array([dAdt(z) for z in z_eval])
dA_norm = dA_vals / np.max(np.abs(dA_vals))
wr_vals = np.array([sfrd(z) for z in z_eval])

def best_lag_corr(signal1, signal2, t_eval):
    lags = np.linspace(0, 5, 100)
    best_r, best_lag = -999, 0
    for lag in lags:
        idx_shift = int(lag / (t_eval[1]-t_eval[0]))
        if idx_shift >= len(t_eval) - 30: continue
        s2_shifted = np.roll(signal2, idx_shift)
        mask = np.arange(idx_shift + 10, len(t_eval) - 10)
        if len(mask) < 20: continue
        s1 = signal1[mask]; s2s = s2_shifted[mask]
        s2s_n = s2s / np.max(s2s) if np.max(s2s) > 0 else s2s
        r = np.corrcoef(s1, s2s_n)[0, 1]
        if r > best_r: best_r, best_lag = r, lag
    return best_lag, best_r

actual_lag, actual_r = best_lag_corr(dA_norm, wr_vals, t_eval)
print("=" * 80)
print(f"Actual: lag = {actual_lag:.2f} Gyr, r = {actual_r:.4f}")
print("=" * 80)

np.random.seed(42)
N = 2000

# Test 1: Random Gaussians
print("\n--- Test 1: Random Gaussians ---")
exceed_1 = 0
for i in range(N):
    pk = np.random.uniform(1, 12)
    wd = np.random.uniform(1, 5)
    hump = np.exp(-(t_eval - pk)**2 / (2*wd**2))
    _, r = best_lag_corr(dA_norm, hump, t_eval)
    if r >= actual_r: exceed_1 += 1
p1 = exceed_1 / N
print(f"  p = {p1:.4f} ({exceed_1}/{N} exceeded r = {actual_r:.3f})")

# Test 2: Randomized SFRD parameters
print("\n--- Test 2: Randomized SFRD shape ---")
exceed_2 = 0
rs_2 = []
for i in range(N):
    zb = np.random.uniform(1.5, 5.0)
    ar = np.random.uniform(1.5, 4.0)
    bf = np.random.uniform(3.0, 8.0)
    rsfrd = np.array([0.015*(1+z)**ar / (1+((1+z)/zb)**bf) for z in z_eval])
    _, r = best_lag_corr(dA_norm, rsfrd, t_eval)
    rs_2.append(r)
    if r >= actual_r: exceed_2 += 1
p2 = exceed_2 / N
rs_2 = np.array(rs_2)
print(f"  p = {p2:.4f} ({exceed_2}/{N})")
print(f"  Mean r: {np.mean(rs_2):.4f}, 95th: {np.percentile(rs_2,95):.4f}, 99th: {np.percentile(rs_2,99):.4f}")

# Test 3: Circular shifts
print("\n--- Test 3: Phase-shifted actual SFRD ---")
exceed_3 = 0
for i in range(N):
    shift = np.random.randint(30, 270)
    _, r = best_lag_corr(dA_norm, np.roll(wr_vals, shift), t_eval)
    if r >= actual_r: exceed_3 += 1
p3 = exceed_3 / N
print(f"  p = {p3:.4f} ({exceed_3}/{N})")

# Test 4: No dark energy (Einstein-de Sitter)
print("\n--- Test 4: Without dark energy ---")
def H_EdS(z): return H0_si * np.sqrt(Om*(1+z)**3 + Or*(1+z)**4)
def dAdt_EdS(z):
    dz = 0.001
    dhdz = (H_EdS(z+dz) - H_EdS(z-dz)) / (2*dz)
    dhdt = dhdz * (-(1+z)*H_EdS(z))
    return -8*np.pi*c**2/(H_EdS(z)**3)*dhdt

dA_EdS = np.array([dAdt_EdS(z) for z in z_eval])
dA_EdS_n = dA_EdS / np.max(np.abs(dA_EdS))
lag_EdS, r_EdS = best_lag_corr(dA_EdS_n, wr_vals, t_eval)
print(f"  EdS (no DE):  lag = {lag_EdS:.2f} Gyr, r = {r_EdS:.4f}")
print(f"  ΛCDM (real):  lag = {actual_lag:.2f} Gyr, r = {actual_r:.4f}")
print(f"  Dark energy {'IMPROVES' if actual_r > r_EdS else 'WORSENS'} correlation by Δr = {actual_r - r_EdS:.4f}")

# Test 5: What if SFRD peaked at a different epoch?
print("\n--- Test 5: Sensitivity to SFRD peak epoch ---")
print(f"{'Peak z':>8} {'Peak t':>8} {'Best lag':>9} {'r':>8} {'Lag+peak_t':>11} {'Note':>20}")
print("-" * 70)
for z_break in [1.5, 2.0, 2.5, 2.9, 3.5, 4.0, 5.0]:
    test_sfrd = np.array([0.015*(1+z)**2.7 / (1+((1+z)/z_break)**5.6) for z in z_eval])
    peak_idx = np.argmax(test_sfrd)
    peak_t = t_eval[peak_idx]
    peak_z = z_eval[peak_idx]
    lag, r = best_lag_corr(dA_norm, test_sfrd, t_eval)
    arrival = peak_t + lag
    note = "← actual SFRD" if abs(z_break - 2.9) < 0.1 else ""
    if abs(arrival - 7.3) < 0.5: note += " ← hits accel onset"
    print(f"{peak_z:>8.2f} {peak_t:>8.2f} {lag:>9.2f} {r:>8.4f} {arrival:>11.2f} {note:>20}")

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"""
Observed correlation: r = {actual_r:.3f} at lag = {actual_lag:.1f} Gyr

Significance:
  vs random humps:        p = {p1:.4f}
  vs randomized SFRD:     p = {p2:.4f}
  vs phase-shifted SFRD:  p = {p3:.4f}

Without dark energy the correlation drops to r = {r_EdS:.3f}.
The dark energy component is what makes the expansion track 
the lagged write rate.

The lag is not arbitrary — it is the specific value that aligns 
the peak of boundary encoding with the acceleration onset.
""")
