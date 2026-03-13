#!/usr/bin/env python3
"""
generate_figures.py
====================
Generates all four figures for Paper 7:
  Figure 1: QEC redundancy history κ(z)
  Figure 2: Write rate vs expansion rate with lag
  Figure 3: Attractor behavior + EdS comparison
  Figure 4: Cosmic timeline

Part of Paper 7: Dark Energy as Boundary Encoding
Charles Grant Smith Jr., March 2026
"""
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Constants
c = 3e8; H0_si = 67.4e3 / 3.086e22
Gyr_s = 3.156e16; Om = 0.315; OL = 0.685; Or = 9.1e-5
lP = 1.616e-35

def H(z): return H0_si * np.sqrt(Or*(1+z)**4 + Om*(1+z)**3 + OL)
def dHdz(z):
    dz = 0.001
    return (H(z+dz) - H(z-dz)) / (2*dz)
def cosmic_time(z):
    if z > 1e4: return 0
    result, _ = quad(lambda zp: 1.0/((1+zp)*H(zp)), z, 1e4, limit=500)
    return result / Gyr_s
def S_hor(z): return np.pi * c**2 / (lP**2 * H(z)**2)
def dAdt(z):
    dhdt = dHdz(z) * (-(1+z) * H(z))
    return -8 * np.pi * c**2 / (H(z)**3) * dhdt
def sfrd(z):
    return 0.015 * (1+z)**2.7 / (1 + ((1+z)/2.9)**5.6)

# Build time-redshift mapping
z_grid = np.linspace(0, 8, 2000)
t_grid = np.array([cosmic_time(z) for z in z_grid])
z_of_t = interp1d(t_grid, z_grid, kind='cubic', fill_value='extrapolate')
t_of_z = interp1d(z_grid, t_grid, kind='cubic', fill_value='extrapolate')

# SMBH entropy model
S_BH_today = 2.6e103
S_rad = 4e88

def cum_stellar_from_inf(z_to):
    result, _ = quad(lambda z: sfrd(z) / ((1+z)*H(z)) / Gyr_s * 1e9, z_to, 20, limit=200)
    return result

rho_star_total = cum_stellar_from_inf(0)

def frac_bh_formed(z):
    return cum_stellar_from_inf(z) / rho_star_total

def S_bulk(z):
    if z > 20: return S_rad
    f = frac_bh_formed(z)
    return S_rad + f**1.5 * S_BH_today

plt.rcParams.update({
    'font.size': 11, 'axes.labelsize': 13, 'axes.titlesize': 14,
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
    'axes.grid': True, 'grid.alpha': 0.3
})

# ===================================================================
# FIGURE 1: κ(z) trajectory - the QEC redundancy history
# ===================================================================
fig1, ax1 = plt.subplots(figsize=(10, 6))

zz = np.linspace(0, 6, 500)
kappa_vals = []
for z in zz:
    sh = np.log10(S_hor(z))
    sb = np.log10(S_bulk(z))
    kappa_vals.append(sh - sb)
kappa_vals = np.array(kappa_vals)

ax1.plot(zz, kappa_vals, 'b-', lw=2.5, label=r'$\log_{10}\kappa(z) = \log_{10}(S_{\rm hor}/S_{\rm bulk})$')

# Mark key epochs
min_idx = np.argmin(kappa_vals)
ax1.axvline(zz[min_idx], color='red', ls='--', lw=1.5, alpha=0.7, label=f'$\\kappa$ minimum: $z \\approx {zz[min_idx]:.1f}$')
ax1.axvline(0.7, color='green', ls='--', lw=1.5, alpha=0.7, label='Acceleration onset: $z \\approx 0.7$')
ax1.axvline(1.9, color='orange', ls='--', lw=1.5, alpha=0.7, label='Cosmic noon: $z \\approx 1.9$')

ax1.fill_between([0.7, zz[min_idx]], [17, 17], [22, 22], alpha=0.08, color='red',
                  label='$\\kappa$ recovery zone')

ax1.set_xlabel('Redshift $z$')
ax1.set_ylabel(r'$\log_{10}\kappa = \log_{10}(S_{\rm hor}/S_{\rm bulk})$')
ax1.set_title('Figure 1: QEC Redundancy History of the Observable Universe')
ax1.set_xlim(0, 6)
ax1.set_ylim(17.5, 22)
ax1.legend(loc='upper right', fontsize=10)
ax1.invert_xaxis()

# Add cosmic time on top axis
ax1_top = ax1.twiny()
t_ticks_z = [0, 0.5, 1, 1.5, 2, 3, 4, 5]
t_ticks_t = [cosmic_time(z) for z in t_ticks_z]
ax1_top.set_xlim(ax1.get_xlim())
ax1_top.set_xticks(t_ticks_z)
ax1_top.set_xticklabels([f'{t:.1f}' for t in t_ticks_t], fontsize=9)
ax1_top.set_xlabel('Cosmic time (Gyr)', fontsize=11)

# Annotate the minimum
ax1.annotate(f'$\\kappa_{{\\min}} = 10^{{{kappa_vals[min_idx]:.1f}}}$',
            xy=(zz[min_idx], kappa_vals[min_idx]),
            xytext=(zz[min_idx]+0.8, kappa_vals[min_idx]-0.3),
            fontsize=11, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# Add annotation about what's happening
ax1.text(4.5, 18.2, 'SMBH entropy\naccumulates\n→ $\\kappa$ drops', 
         fontsize=9, ha='center', style='italic', color='gray')
ax1.text(0.3, 19.2, 'DE accelerates\nexpansion\n→ $\\kappa$ recovers', 
         fontsize=9, ha='center', style='italic', color='gray')

plt.tight_layout()
plt.savefig('/home/claude/figure1_kappa_history.png', dpi=200, bbox_inches='tight')
print("Figure 1 saved")
plt.close()

# ===================================================================
# FIGURE 2: Write rate vs expansion rate with lag
# ===================================================================
t_eval = np.linspace(0.5, 13.5, 500)
z_eval = np.array([float(z_of_t(t)) for t in t_eval])

dA_vals = np.array([dAdt(z) for z in z_eval])
dA_norm = dA_vals / np.max(np.abs(dA_vals))
wr_vals = np.array([sfrd(z) for z in z_eval])
wr_norm = wr_vals / np.max(wr_vals)

# Lagged write rate (3.5 Gyr)
lag = 3.5
wr_lagged = np.array([sfrd(float(z_of_t(max(t - lag, 0.3)))) for t in t_eval])
wr_lagged_norm = wr_lagged / np.max(wr_lagged)

fig2, (ax2a, ax2b) = plt.subplots(2, 1, figsize=(10, 9), height_ratios=[3, 2])

# Top panel: the three curves
ax2a.plot(t_eval, wr_norm, 'b-', lw=2, label='Bulk write rate (SFRD)', alpha=0.9)
ax2a.plot(t_eval, wr_lagged_norm, color='darkorange', lw=2, ls='--',
          label=f'Lagged write rate ($\\tau$ = {lag:.1f} Gyr)', alpha=0.9)
ax2a.plot(t_eval, dA_norm, 'g-', lw=2.5, label='Horizon area growth $dA/dt$', alpha=0.9)

# Mark key epochs
for t_mark, label, color in [
    (3.5, 'Cosmic noon', 'blue'),
    (5.3, '$\\kappa_{\\min}$', 'red'),
    (7.0, 'Lagged peak', 'darkorange'),
    (7.3, 'Accel onset', 'green')
]:
    ax2a.axvline(t_mark, color=color, ls=':', lw=1, alpha=0.5)
    ax2a.text(t_mark, 1.05, label, fontsize=8, ha='center', color=color, rotation=0)

# Arrow showing the lag
ax2a.annotate('', xy=(7.0, 0.85), xytext=(3.5, 0.85),
             arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
ax2a.text(5.25, 0.88, f'$\\tau_{{\\rm enc}}$ ≈ {lag:.1f} Gyr', fontsize=11, 
         ha='center', color='purple', fontweight='bold')

ax2a.set_ylabel('Normalized rate')
ax2a.set_title('Figure 2: Write Rate Drives Expansion (with Encoding Lag)')
ax2a.legend(loc='upper right', fontsize=10)
ax2a.set_xlim(0.5, 13.5)
ax2a.set_ylim(-0.05, 1.15)

# Add redshift on top
ax2a_top = ax2a.twiny()
z_ticks_t = [1, 2, 3, 4, 5, 7, 9, 11, 13]
z_ticks_z = [float(z_of_t(t)) for t in z_ticks_t]
ax2a_top.set_xlim(ax2a.get_xlim())
ax2a_top.set_xticks(z_ticks_t)
ax2a_top.set_xticklabels([f'{z:.1f}' for z in z_ticks_z], fontsize=9)
ax2a_top.set_xlabel('Redshift $z$', fontsize=11)

# Bottom panel: lag correlation scan
lags = np.linspace(0, 5, 200)
correlations = []
for lg in lags:
    idx_shift = int(lg / (t_eval[1]-t_eval[0]))
    if idx_shift >= len(t_eval) - 30:
        correlations.append(np.nan)
        continue
    s2_shifted = np.roll(wr_vals, idx_shift)
    mask = np.arange(idx_shift + 10, len(t_eval) - 10)
    if len(mask) < 20:
        correlations.append(np.nan)
        continue
    s2n = s2_shifted[mask] / np.max(s2_shifted[mask])
    correlations.append(np.corrcoef(dA_norm[mask], s2n)[0, 1])

correlations = np.array(correlations)
ax2b.plot(lags, correlations, 'k-', lw=2)
best_idx = np.nanargmax(correlations)
ax2b.axvline(lags[best_idx], color='red', ls='--', lw=1.5,
            label=f'Best lag = {lags[best_idx]:.1f} Gyr ($r$ = {correlations[best_idx]:.3f})')
ax2b.axhline(0, color='gray', ls='-', lw=0.5)
ax2b.set_xlabel('Lag $\\tau$ (Gyr)')
ax2b.set_ylabel('Pearson $r$')
ax2b.set_title('Cross-correlation: $dA/dt$ vs lagged SFRD')
ax2b.legend(fontsize=10)
ax2b.set_xlim(0, 5)

plt.tight_layout()
plt.savefig('/home/claude/figure2_write_rate_expansion.png', dpi=200, bbox_inches='tight')
print("Figure 2 saved")
plt.close()

# ===================================================================
# FIGURE 3: The attractor + EdS comparison
# ===================================================================
fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left: Attractor behavior
z_breaks = [1.5, 2.0, 2.5, 2.9, 3.5, 4.0, 5.0]
colors_att = plt.cm.viridis(np.linspace(0.2, 0.9, len(z_breaks)))

for i, zb in enumerate(z_breaks):
    test_sfrd = np.array([0.015*(1+z)**2.7 / (1+((1+z)/zb)**5.6) for z in z_eval])
    peak_idx = np.argmax(test_sfrd)
    peak_t = t_eval[peak_idx]
    
    best_r, best_lag = -999, 0
    for lg in np.linspace(0, 5.5, 200):
        idx_shift = int(lg / (t_eval[1]-t_eval[0]))
        if idx_shift >= len(t_eval) - 30: continue
        s2_shifted = np.roll(test_sfrd, idx_shift)
        mask = np.arange(idx_shift + 10, len(t_eval) - 10)
        if len(mask) < 20: continue
        s2n = s2_shifted[mask] / np.max(s2_shifted[mask])
        r = np.corrcoef(dA_norm[mask], s2n)[0, 1]
        if r > best_r: best_r, best_lag = r, lg
    
    arrival = peak_t + best_lag
    marker = '*' if abs(zb - 2.9) < 0.1 else 'o'
    ms = 15 if abs(zb - 2.9) < 0.1 else 8
    ax3a.scatter(peak_t, arrival, color=colors_att[i], s=ms**2, 
                marker=marker, zorder=5, edgecolors='black', linewidths=0.5)
    ax3a.annotate(f'$z_{{break}}$={zb}', (peak_t, arrival), 
                 textcoords="offset points", xytext=(8, -5), fontsize=8, color=colors_att[i])

# The attractor line
ax3a.axhline(7.15, color='green', ls='--', lw=2, alpha=0.7, label='Acceleration onset ($t \\approx 7.2$ Gyr)')
ax3a.fill_between([1, 9], [6.8, 6.8], [7.5, 7.5], alpha=0.1, color='green')
ax3a.plot([1, 7], [1, 7], 'gray', ls=':', lw=1, alpha=0.4)  # diagonal reference

ax3a.set_xlabel('SFRD peak time $t_{\\rm peak}$ (Gyr)')
ax3a.set_ylabel('$t_{\\rm peak} + \\tau_{\\rm lag}$ (Gyr)')
ax3a.set_title('Attractor: lag always hits acceleration onset')
ax3a.legend(fontsize=10)
ax3a.set_xlim(1.2, 6.5)
ax3a.set_ylim(6, 9)

# Right: ΛCDM vs EdS
def H_EdS(z): return H0_si * np.sqrt(Om*(1+z)**3 + Or*(1+z)**4)
def dAdt_EdS(z):
    dz = 0.001
    dhdz = (H_EdS(z+dz) - H_EdS(z-dz)) / (2*dz)
    dhdt = dhdz * (-(1+z)*H_EdS(z))
    return -8*np.pi*c**2/(H_EdS(z)**3)*dhdt

dA_EdS = np.array([dAdt_EdS(z) for z in z_eval])
dA_EdS_n = dA_EdS / np.max(np.abs(dA_EdS))

# Compute correlations for both
corr_lcdm = []
corr_eds = []
for lg in lags:
    idx_shift = int(lg / (t_eval[1]-t_eval[0]))
    if idx_shift >= len(t_eval) - 30:
        corr_lcdm.append(np.nan); corr_eds.append(np.nan)
        continue
    s2_shifted = np.roll(wr_vals, idx_shift)
    mask = np.arange(idx_shift + 10, len(t_eval) - 10)
    if len(mask) < 20:
        corr_lcdm.append(np.nan); corr_eds.append(np.nan)
        continue
    s2n = s2_shifted[mask] / np.max(s2_shifted[mask])
    corr_lcdm.append(np.corrcoef(dA_norm[mask], s2n)[0, 1])
    corr_eds.append(np.corrcoef(dA_EdS_n[mask], s2n)[0, 1])

ax3b.plot(lags, corr_lcdm, 'b-', lw=2.5, label='$\\Lambda$CDM (our universe)')
ax3b.plot(lags, corr_eds, 'r--', lw=2.5, label='Einstein–de Sitter (no DE)')
ax3b.axhline(0, color='gray', ls='-', lw=0.5)
ax3b.fill_between(lags, corr_lcdm, corr_eds, alpha=0.1, color='blue',
                  label='Dark energy contribution')

ax3b.set_xlabel('Lag $\\tau$ (Gyr)')
ax3b.set_ylabel('Pearson $r$ (write rate vs $dA/dt$)')
ax3b.set_title('Dark energy is necessary for the correlation')
ax3b.legend(fontsize=10)
ax3b.set_xlim(0, 5)
ax3b.set_ylim(-0.5, 1.0)

plt.tight_layout()
plt.savefig('/home/claude/figure3_attractor_eds.png', dpi=200, bbox_inches='tight')
print("Figure 3 saved")
plt.close()

# ===================================================================
# FIGURE 4: The timeline
# ===================================================================
fig4, ax4 = plt.subplots(figsize=(12, 3.5))

events = [
    (0.38, 'Recombination\n$z=1100$', 'gray', 0.4),
    (3.5, 'Cosmic noon\n$z \\approx 2$\n(peak write rate)', 'blue', 0.9),
    (5.3, '$\\kappa$ minimum\n$z \\approx 1.15$', 'red', 0.6),
    (7.0, 'Encoding\ncompletes\n$z \\approx 0.7$', 'darkorange', 0.9),
    (7.3, 'Acceleration\nonset\n$z \\approx 0.67$', 'green', 0.7),
    (13.8, 'Today\n$z = 0$', 'black', 0.4),
]

ax4.axhline(0, color='black', lw=2)
for t, label, color, size in events:
    ax4.plot(t, 0, 'o', color=color, markersize=12*size, zorder=5)
    yoff = 0.35 if events.index((t, label, color, size)) % 2 == 0 else -0.55
    ax4.annotate(label, (t, 0), xytext=(0, 30 if yoff > 0 else -60),
                textcoords='offset points', ha='center', fontsize=9, color=color,
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

# Lag arrow
ax4.annotate('', xy=(7.0, -0.15), xytext=(3.5, -0.15),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=2.5))
ax4.text(5.25, -0.22, '$\\tau_{\\rm enc} \\approx 3.5$ Gyr', fontsize=12,
        ha='center', color='purple', fontweight='bold')

ax4.set_xlim(-0.5, 14.5)
ax4.set_ylim(-0.8, 0.8)
ax4.set_xlabel('Cosmic time (Gyr)', fontsize=13)
ax4.set_title('Figure 4: Timeline — Write Rate Drives Expansion', fontsize=13)
ax4.set_yticks([])
ax4.spines['top'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/home/claude/figure4_timeline.png', dpi=200, bbox_inches='tight')
print("Figure 4 saved")
plt.close()

print("\nAll 4 figures generated.")
